import { Hono } from 'hono';
import { z } from 'zod';
import type { AppBindings } from '../env';
import { db } from '../lib/db';
import { badRequest, notFound, unauthorized } from '../lib/errors';
import { nowIso, sha256Hex } from '../lib/ids';

/**
 * The out-of-band side of agent mode. A worker lists pending model requests
 * and submits answers; the parked job picks the answer up on its next retry.
 * Guarded by a dedicated token, not a creator API key, because it reads every
 * account's prompts.
 */
export const agent = new Hono<AppBindings>();

agent.use('/v1/agent/*', async (c, next) => {
  const expected = c.env.AGENT_TOKEN;
  if (!expected) throw notFound('Endpoint');
  const header = c.req.header('authorization') ?? '';
  const presented = header.startsWith('Bearer ') ? header.slice(7).trim() : '';
  // Compare digests so the check does not leak the token through timing.
  if (!presented || (await sha256Hex(presented)) !== (await sha256Hex(expected))) {
    throw unauthorized('Agent token required');
  }
  await next();
});

agent.get('/v1/agent/work', async (c) => {
  const limit = Math.min(20, Math.max(1, Number(c.req.query('limit') ?? 5)));
  const rows = await db(c.env).all<{ id: string; model: string; request: string; created_at: string }>(
    `SELECT id, model, request, created_at FROM agent_work
      WHERE status = 'pending' ORDER BY created_at ASC LIMIT ?`,
    limit,
  );
  return c.json({
    work: rows.map((r) => ({ id: r.id, model: r.model, createdAt: r.created_at, ...JSON.parse(r.request) })),
  });
});

const answerSchema = z.object({
  text: z.string().max(200_000),
  meta: z.record(z.string(), z.unknown()).optional(),
});

agent.post('/v1/agent/work/:id', async (c) => {
  const parsed = answerSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid answer payload', parsed.error.issues);

  const res = await db(c.env).run(
    `UPDATE agent_work SET status = 'done', result = ?, worker_meta = ?, completed_at = ?
      WHERE id = ? AND status = 'pending'`,
    parsed.data.text,
    JSON.stringify(parsed.data.meta ?? {}),
    nowIso(),
    c.req.param('id'),
  );
  if (res.meta.changes !== 1) throw notFound('Pending work item');
  return c.json({ ok: true });
});
