import { Hono } from 'hono';
import { z } from 'zod';
import type { AppBindings } from '../env';
import { audit, db } from '../lib/db';
import { newId, newReferralCode, nowIso } from '../lib/ids';
import { issueApiKey, requireAuth } from '../lib/auth';
import { badRequest, conflict, notFound } from '../lib/errors';
import { controlsFor } from '../lib/governance';
import { isSupportedPlatform, hasLiveAdapter } from '../adapters/registry';
import { PLANS, type AccountRecord } from '../lib/types';
import { enqueue } from '../queue/jobs';

export const accounts = new Hono<AppBindings>();

const signupSchema = z.object({
  email: z.string().email(),
  displayName: z.string().min(1).max(120),
  timezone: z.string().default('UTC'),
  referralCode: z.string().optional(),
});

/**
 * Public signup. Returns the API key exactly once, so the caller must store it.
 * A 14-day trial starts immediately with autopilot off: the creator opts into
 * unattended publishing after they have seen what the system drafts.
 */
accounts.post('/v1/accounts', async (c) => {
  const parsed = signupSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid signup payload', parsed.error.issues);
  const input = parsed.data;

  const existing = await db(c.env).first<{ id: string }>(
    `SELECT id FROM accounts WHERE lower(email) = lower(?)`,
    input.email,
  );
  if (existing) throw conflict('An account already exists for that email');

  const referrer = input.referralCode
    ? await db(c.env).first<{ id: string }>(
        `SELECT id FROM accounts WHERE referral_code = ?`,
        input.referralCode.toUpperCase(),
      )
    : null;

  const accountId = newId('acct');
  const now = nowIso();
  const trialEnds = new Date(Date.now() + 14 * 86_400_000).toISOString();

  await db(c.env).batch([
    {
      sql: `INSERT INTO accounts
              (id, email, display_name, timezone, plan, status, trial_ends_at,
               referral_code, referred_by, created_at, updated_at)
            VALUES (?, ?, ?, ?, 'trial', 'active', ?, ?, ?, ?, ?)`,
      binds: [
        accountId,
        input.email,
        input.displayName,
        input.timezone,
        trialEnds,
        newReferralCode(),
        referrer?.id ?? null,
        now,
        now,
      ],
    },
    {
      sql: `INSERT INTO automation_controls
              (account_id, autopilot_publishing, autopilot_replies, daily_publish_cap,
               daily_reply_cap, updated_at)
            VALUES (?, 0, 0, 10, 25, ?)`,
      binds: [accountId, now],
    },
  ]);

  if (referrer) {
    await db(c.env).run(
      `INSERT INTO referrals (id, referrer_account_id, referred_account_id, status, created_at)
       VALUES (?, ?, ?, 'pending', ?)`,
      newId('ref'),
      referrer.id,
      accountId,
      now,
    );
  }

  const key = await issueApiKey(c.env, accountId, 'default');
  await audit(c.env, {
    accountId,
    actor: 'public',
    action: 'account.created',
    entityType: 'account',
    entityId: accountId,
    detail: { referred: Boolean(referrer) },
  });

  return c.json(
    {
      accountId,
      apiKey: key.plaintext,
      trialEndsAt: trialEnds,
      note: 'Store this API key now. It cannot be retrieved again.',
    },
    201,
  );
});

accounts.use('/v1/me', requireAuth);
accounts.use('/v1/strategy', requireAuth);
accounts.use('/v1/pillars', requireAuth);
accounts.use('/v1/pillars/*', requireAuth);
accounts.use('/v1/channels', requireAuth);
accounts.use('/v1/controls', requireAuth);

accounts.get('/v1/me', async (c) => {
  const { accountId } = c.get('ctx');
  const account = await db(c.env).first<AccountRecord>(
    `SELECT id, email, display_name, timezone, plan, status, trial_ends_at, referral_code, created_at
       FROM accounts WHERE id = ?`,
    accountId,
  );
  if (!account) throw notFound('Account');

  const controls = await controlsFor(c.env, accountId);
  const channels = await db(c.env).all(
    `SELECT id, platform, handle, status, posts_per_week FROM channels WHERE account_id = ?`,
    accountId,
  );

  return c.json({ account, plan: PLANS[account.plan], controls, channels });
});

const strategySchema = z.object({
  positioning: z.string().min(10).max(2000),
  audience: z.string().min(10).max(2000),
  tone: z.string().min(5).max(2000),
  proofPoints: z.array(z.string().max(300)).max(20).default([]),
  bannedPhrases: z.array(z.string().max(120)).max(50).default([]),
  ctaLibrary: z.array(z.string().max(300)).max(20).default([]),
});

accounts.put('/v1/strategy', async (c) => {
  const { accountId } = c.get('ctx');
  const parsed = strategySchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid strategy payload', parsed.error.issues);
  const s = parsed.data;
  const now = nowIso();

  // Editing the strategy rewrites the cached system prefix for this account, so
  // the next generation call pays a cache write. That is the correct trade: a
  // stale voice is worse than one cold call.
  await db(c.env).run(
    `INSERT INTO strategies
       (id, account_id, positioning, audience, tone, proof_points, banned_phrases,
        cta_library, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
     ON CONFLICT(account_id) DO UPDATE SET
       positioning = excluded.positioning,
       audience = excluded.audience,
       tone = excluded.tone,
       proof_points = excluded.proof_points,
       banned_phrases = excluded.banned_phrases,
       cta_library = excluded.cta_library,
       updated_at = excluded.updated_at`,
    newId('strat'),
    accountId,
    s.positioning,
    s.audience,
    s.tone,
    JSON.stringify(s.proofPoints),
    JSON.stringify(s.bannedPhrases),
    JSON.stringify(s.ctaLibrary),
    now,
    now,
  );

  return c.json({ ok: true });
});

const pillarSchema = z.object({
  name: z.string().min(2).max(80),
  description: z.string().max(500).default(''),
  weight: z.number().min(0.1).max(3).default(1),
});

accounts.get('/v1/pillars', async (c) => {
  const { accountId } = c.get('ctx');
  return c.json({
    pillars: await db(c.env).all(
      `SELECT id, name, description, weight, active FROM pillars WHERE account_id = ? ORDER BY name`,
      accountId,
    ),
  });
});

accounts.post('/v1/pillars', async (c) => {
  const { accountId } = c.get('ctx');
  const parsed = pillarSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid pillar payload', parsed.error.issues);

  const id = newId('pil');
  const now = nowIso();
  await db(c.env).run(
    `INSERT INTO pillars (id, account_id, name, description, weight, active, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, 1, ?, ?)`,
    id,
    accountId,
    parsed.data.name,
    parsed.data.description,
    parsed.data.weight,
    now,
    now,
  );
  return c.json({ id }, 201);
});

const channelSchema = z.object({
  platform: z.string(),
  handle: z.string().min(1).max(120),
  accessToken: z.string().optional(),
  externalId: z.string().optional(),
  postsPerWeek: z.number().int().min(1).max(21).default(5),
});

accounts.post('/v1/channels', async (c) => {
  const { accountId } = c.get('ctx');
  const parsed = channelSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid channel payload', parsed.error.issues);
  const input = parsed.data;

  if (!isSupportedPlatform(input.platform)) {
    throw badRequest(`Unsupported platform "${input.platform}"`);
  }

  const account = await db(c.env).first<AccountRecord>(
    `SELECT * FROM accounts WHERE id = ?`,
    accountId,
  );
  if (!account) throw notFound('Account');

  const count = await db(c.env).first<{ n: number }>(
    `SELECT COUNT(*) AS n FROM channels WHERE account_id = ? AND status != 'revoked'`,
    accountId,
  );
  const limit = PLANS[account.plan].channels;
  if ((count?.n ?? 0) >= limit) {
    throw conflict(`The ${PLANS[account.plan].name} plan allows ${limit} channels`);
  }

  const id = newId('chan');
  const now = nowIso();
  await db(c.env).run(
    `INSERT INTO channels
       (id, account_id, platform, handle, external_id, access_token, status,
        posts_per_week, connected_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, 'connected', ?, ?, ?)`,
    id,
    accountId,
    input.platform,
    input.handle,
    input.externalId ?? null,
    input.accessToken ?? null,
    input.postsPerWeek,
    now,
    now,
  );

  // Plan the new channel now rather than waiting for tomorrow's cron, so the
  // creator sees a filled calendar during onboarding.
  await enqueue(c.env, 'plan.generate', {}, { accountId, idempotencyKey: `plan:${id}:initial` });

  return c.json(
    {
      id,
      simulated: !hasLiveAdapter(input.platform),
      note: hasLiveAdapter(input.platform)
        ? undefined
        : 'Publishing for this platform is simulated. Planning and drafting are live.',
    },
    201,
  );
});

const controlsSchema = z.object({
  autopilotPublishing: z.boolean().optional(),
  autopilotReplies: z.boolean().optional(),
  pausedUntil: z.string().datetime().nullable().optional(),
  dailyPublishCap: z.number().int().min(0).max(100).optional(),
  dailyReplyCap: z.number().int().min(0).max(500).optional(),
});

/**
 * The kill switch. Every change here is audited, because "who turned autopilot
 * on" is the first question asked when something unexpected gets published.
 */
accounts.put('/v1/controls', async (c) => {
  const { accountId, keyId } = c.get('ctx');
  const parsed = controlsSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid controls payload', parsed.error.issues);

  const current = await controlsFor(c.env, accountId);
  const next = {
    autopilot_publishing: parsed.data.autopilotPublishing ?? Boolean(current.autopilot_publishing),
    autopilot_replies: parsed.data.autopilotReplies ?? Boolean(current.autopilot_replies),
    paused_until:
      parsed.data.pausedUntil === undefined ? current.paused_until : parsed.data.pausedUntil,
    daily_publish_cap: parsed.data.dailyPublishCap ?? current.daily_publish_cap,
    daily_reply_cap: parsed.data.dailyReplyCap ?? current.daily_reply_cap,
  };

  await db(c.env).run(
    `INSERT INTO automation_controls
       (account_id, autopilot_publishing, autopilot_replies, paused_until,
        daily_publish_cap, daily_reply_cap, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, ?)
     ON CONFLICT(account_id) DO UPDATE SET
       autopilot_publishing = excluded.autopilot_publishing,
       autopilot_replies = excluded.autopilot_replies,
       paused_until = excluded.paused_until,
       daily_publish_cap = excluded.daily_publish_cap,
       daily_reply_cap = excluded.daily_reply_cap,
       updated_at = excluded.updated_at`,
    accountId,
    next.autopilot_publishing ? 1 : 0,
    next.autopilot_replies ? 1 : 0,
    next.paused_until,
    next.daily_publish_cap,
    next.daily_reply_cap,
    nowIso(),
  );

  await audit(c.env, {
    accountId,
    actor: `key:${keyId}`,
    action: 'controls.updated',
    entityType: 'account',
    entityId: accountId,
    detail: { from: current, to: next },
  });

  return c.json({ controls: next });
});
