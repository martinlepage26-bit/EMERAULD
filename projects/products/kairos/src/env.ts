export interface Env {
  DB: D1Database;
  MEDIA: R2Bucket;
  CACHE: KVNamespace;

  ENVIRONMENT: string;
  DRAFT_MODEL: string;
  STRATEGY_MODEL: string;
  DRY_RUN: string;
  JOB_BATCH_SIZE: string;
  PUBLIC_BASE_URL: string;
  /** Comma-separated browser origins allowed to call the API cross-origin. */
  DASHBOARD_ORIGINS: string;
  /**
   * "agent" hands every model call to an out-of-band worker through
   * /v1/agent/work instead of the Messages API. Anything else uses the API.
   */
  AI_MODE?: string;
  /** Bearer token for the /v1/agent/work endpoints. Unset disables them. */
  AGENT_TOKEN?: string;

  ANTHROPIC_API_KEY: string;
  STRIPE_SECRET_KEY: string;
  STRIPE_WEBHOOK_SECRET: string;
  AUTH_SIGNING_KEY: string;
  /** Encrypts channel access tokens at rest. At least 32 random characters. */
  TOKEN_ENCRYPTION_KEY: string;
}

export interface RequestContext {
  accountId: string;
  keyId: string;
}

export type AppBindings = {
  Bindings: Env;
  Variables: { ctx: RequestContext };
};

export function isDryRun(env: Env): boolean {
  return env.DRY_RUN !== 'false';
}

/**
 * Browser origins the dashboard may call from. Requests carry a bearer token
 * rather than cookies, so no credentialed-origin reflection is involved: an
 * origin that is not on this list simply gets no CORS headers back.
 */
export function dashboardOrigins(env: Env): string[] {
  return (env.DASHBOARD_ORIGINS ?? '')
    .split(',')
    .map((o) => o.trim())
    .filter(Boolean);
}

export function isAgentMode(env: Env): boolean {
  return env.AI_MODE === 'agent';
}

export function jobBatchSize(env: Env): number {
  const n = Number.parseInt(env.JOB_BATCH_SIZE ?? '', 10);
  return Number.isFinite(n) && n > 0 ? n : 25;
}
