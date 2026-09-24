import { describe, it, expect, afterEach } from 'vitest';
import worker from '../src/index';
import { generate } from '../src/ai/claude';
import { AwaitingAgentError } from '../src/lib/errors';
import { drain, enqueue, type JobHandler } from '../src/queue/jobs';
import { createHarness, type TestHarness } from './helpers/d1';

let harness: TestHarness | null = null;
afterEach(() => { harness?.close(); harness = null; });

const TOKEN = 'agent-test-token';
function setup(): TestHarness {
  harness = createHarness({ AI_MODE: 'agent', AGENT_TOKEN: TOKEN });
  return harness;
}

const REQ = { stableSystem: 'ops', creatorSystem: 'creator', userPrompt: 'plan please', schema: { type: 'object' } };

async function call(h: TestHarness, method: string, path: string, body?: unknown, token = TOKEN) {
  const res = await worker.fetch(
    new Request(`https://api.test.invalid${path}`, {
      method,
      headers: { authorization: `Bearer ${token}`, 'content-type': 'application/json' },
      body: body ? JSON.stringify(body) : undefined,
    }),
    h.env,
  );
  return { status: res.status, body: (await res.json()) as any };
}

describe('agent mode', () => {
  it('parks the first call and returns the submitted answer on the retry', async () => {
    const h = setup();
    await expect(generate(h.env, REQ)).rejects.toBeInstanceOf(AwaitingAgentError);

    const list = await call(h, 'GET', '/v1/agent/work');
    expect(list.status).toBe(200);
    expect(list.body.work).toHaveLength(1);
    expect(list.body.work[0].user).toBe('plan please');
    expect(list.body.work[0].schema).toEqual({ type: 'object' });

    const post = await call(h, 'POST', `/v1/agent/work/${list.body.work[0].id}`, { text: '{"ok":true}' });
    expect(post.status).toBe(200);

    const result = await generate(h.env, REQ);
    expect(result.text).toBe('{"ok":true}');
    expect(result.refused).toBe(false);
  });

  it('does not create a second work item when the same request is retried', async () => {
    const h = setup();
    await expect(generate(h.env, REQ)).rejects.toBeInstanceOf(AwaitingAgentError);
    await expect(generate(h.env, REQ)).rejects.toBeInstanceOf(AwaitingAgentError);
    expect((await call(h, 'GET', '/v1/agent/work')).body.work).toHaveLength(1);
  });

  it('hands the attempt back when a job parks, so waiting never kills it', async () => {
    const h = setup();
    const handler: JobHandler = async (env) => { await generate(env, REQ); };
    const handlers = { 'plan.generate': handler } as any;
    const id = await enqueue(h.env, 'plan.generate', {}, {});

    for (let i = 0; i < 8; i++) {
      h.sqlite.prepare(`UPDATE jobs SET run_after = ? WHERE id = ?`).run(new Date(0).toISOString(), id);
      await drain(h.env, handlers, 5);
    }
    const job = h.sqlite.prepare(`SELECT status, attempts FROM jobs WHERE id = ?`).get(id) as any;
    expect(job.status).toBe('pending');
    expect(job.attempts).toBe(0);
  });

  it('rejects a wrong token and hides the endpoints when no token is configured', async () => {
    const h = setup();
    expect((await call(h, 'GET', '/v1/agent/work', undefined, 'wrong')).status).toBe(401);
    harness!.close();
    harness = createHarness({ AI_MODE: 'agent' });
    expect((await call(harness, 'GET', '/v1/agent/work')).status).toBe(404);
  });

  it('refuses to answer a work item twice', async () => {
    const h = setup();
    await expect(generate(h.env, REQ)).rejects.toBeInstanceOf(AwaitingAgentError);
    const id = (await call(h, 'GET', '/v1/agent/work')).body.work[0].id;
    expect((await call(h, 'POST', `/v1/agent/work/${id}`, { text: 'a' })).status).toBe(200);
    expect((await call(h, 'POST', `/v1/agent/work/${id}`, { text: 'b' })).status).toBe(404);
  });
});
