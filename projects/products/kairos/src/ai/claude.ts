import Anthropic from '@anthropic-ai/sdk';
import type { Env } from '../env';
import { RetryableError } from '../lib/errors';
import { meter } from '../lib/db';

export type Effort = 'low' | 'medium' | 'high' | 'xhigh' | 'max';

export interface GenerateRequest {
  /**
   * System blocks in stability order: the invariant operating instructions
   * first, then the creator's strategy, then anything volatile. Caching is a
   * prefix match, so a single reordered block costs the whole cache entry.
   */
  stableSystem: string;
  creatorSystem: string;
  volatileSystem?: string;
  userPrompt: string;
  model?: string;
  effort?: Effort;
  maxTokens?: number;
  /** When present, the model is constrained to emit JSON matching this schema. */
  schema?: Record<string, unknown>;
}

export interface Usage {
  inputTokens: number;
  outputTokens: number;
  cacheReadTokens: number;
  cacheWriteTokens: number;
}

export interface GenerateResult {
  text: string;
  refused: boolean;
  refusalCategory: string | null;
  truncated: boolean;
  model: string;
  usage: Usage;
}

function client(env: Env): Anthropic {
  return new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });
}

/**
 * One call to the Messages API.
 *
 * Three things here are load-bearing and easy to get wrong:
 *  - `stop_reason` is checked before `content` is read. Safety classifiers return
 *    HTTP 200 with an empty or partial content array, so indexing content[0]
 *    unconditionally throws on a refusal.
 *  - Server-side fallbacks are opted into, so a declined request is re-run on
 *    Anthropic's recommended fallback inside the same call rather than surfacing
 *    as a dead job.
 *  - No `temperature` / `top_p` / `top_k`, and no `thinking` budget: those are
 *    rejected on current models. Depth is controlled with `output_config.effort`.
 */
export async function generate(env: Env, req: GenerateRequest): Promise<GenerateResult> {
  const model = req.model ?? env.DRAFT_MODEL ?? 'claude-opus-5';
  const maxTokens = req.maxTokens ?? 16_000;

  const system: Anthropic.TextBlockParam[] = [
    { type: 'text', text: req.stableSystem },
    // Cache through the creator's strategy: it is identical across every draft
    // for this account, and it is the largest stable span we have.
    { type: 'text', text: req.creatorSystem, cache_control: { type: 'ephemeral' } },
  ];
  if (req.volatileSystem) system.push({ type: 'text', text: req.volatileSystem });

  const body: Record<string, unknown> = {
    model,
    max_tokens: maxTokens,
    system,
    messages: [{ role: 'user', content: req.userPrompt }],
    output_config: {
      effort: req.effort ?? 'medium',
      ...(req.schema
        ? { format: { type: 'json_schema', schema: req.schema } }
        : {}),
    },
    // Opt into server-side fallback routing by refusal category. `"default"` lets
    // Anthropic pick the substitute, so there is no pinned model to migrate later.
    fallbacks: 'default',
    betas: ['server-side-fallback-2026-07-01'],
  };

  let response: Anthropic.Beta.Messages.BetaMessage;
  try {
    // The `"default"` scalar form of `fallbacks` is newer than the SDK's typings;
    // the request shape is validated server-side.
    response = (await client(env).beta.messages.create(
      body as never,
    )) as Anthropic.Beta.Messages.BetaMessage;
  } catch (err) {
    throw classifyApiError(err);
  }

  const usage: Usage = {
    inputTokens: response.usage?.input_tokens ?? 0,
    outputTokens: response.usage?.output_tokens ?? 0,
    cacheReadTokens: response.usage?.cache_read_input_tokens ?? 0,
    cacheWriteTokens: response.usage?.cache_creation_input_tokens ?? 0,
  };

  if (response.stop_reason === 'refusal') {
    // `stop_details` is returned by the API but not yet in this SDK version's
    // typings, so it is read off the response rather than the typed surface.
    const details = (response as { stop_details?: { category?: string } | null }).stop_details;
    return {
      text: '',
      refused: true,
      refusalCategory: details?.category ?? null,
      truncated: false,
      model: response.model,
      usage,
    };
  }

  const text = response.content
    .filter((b): b is Anthropic.Beta.Messages.BetaTextBlock => b.type === 'text')
    .map((b) => b.text)
    .join('')
    .trim();

  return {
    text,
    refused: false,
    refusalCategory: null,
    truncated: response.stop_reason === 'max_tokens',
    model: response.model,
    usage,
  };
}

/**
 * Generate and parse a JSON payload. `output_config.format` guarantees the shape,
 * so a parse failure means the response was truncated rather than malformed.
 */
export async function generateJson<T>(
  env: Env,
  req: GenerateRequest & { schema: Record<string, unknown> },
): Promise<{ data: T | null; result: GenerateResult }> {
  const result = await generate(env, req);
  if (result.refused || !result.text) return { data: null, result };
  if (result.truncated) {
    throw new RetryableError('Model output hit max_tokens before completing the JSON payload', 30);
  }
  try {
    return { data: JSON.parse(result.text) as T, result };
  } catch {
    throw new RetryableError('Model returned unparseable JSON despite a schema constraint', 30);
  }
}

/** Records token spend so plan limits and margin can be measured per account. */
export async function recordUsage(env: Env, accountId: string, usage: Usage): Promise<void> {
  await meter(env, accountId, 'ai_input_tokens', usage.inputTokens + usage.cacheReadTokens);
  await meter(env, accountId, 'ai_output_tokens', usage.outputTokens);
}

/**
 * Splits transient API failures from permanent ones. Retrying a 400 just
 * re-sends the same broken request five times before failing anyway, so only
 * rate limits, connection failures, and 5xx become retryable.
 */
function classifyApiError(err: unknown): Error {
  if (err instanceof Anthropic.RateLimitError) {
    const retryAfter = Number.parseInt(err.headers.get('retry-after') ?? '', 10);
    return new RetryableError('Anthropic rate limit', Number.isFinite(retryAfter) ? retryAfter : 60);
  }
  if (err instanceof Anthropic.APIConnectionError) {
    return new RetryableError('Could not reach the Anthropic API', 30);
  }
  if (err instanceof Anthropic.APIError && typeof err.status === 'number' && err.status >= 500) {
    return new RetryableError(`Anthropic server error (${err.status})`, 30);
  }
  return err instanceof Error ? err : new Error(String(err));
}
