-- KAIROS core schema.
-- Every table is tenanted by account_id. Cross-account reads are prevented at the
-- query layer (src/lib/db.ts) rather than by D1, which has no row-level security.

CREATE TABLE accounts (
  id                     TEXT PRIMARY KEY,
  email                  TEXT NOT NULL,
  display_name           TEXT NOT NULL,
  timezone               TEXT NOT NULL DEFAULT 'UTC',
  plan                   TEXT NOT NULL DEFAULT 'trial',   -- trial|solo|pro|studio|agency
  status                 TEXT NOT NULL DEFAULT 'active',  -- active|past_due|paused|canceled
  stripe_customer_id     TEXT,
  stripe_subscription_id TEXT,
  trial_ends_at          TEXT,
  referral_code          TEXT NOT NULL,
  referred_by            TEXT REFERENCES accounts(id),
  created_at             TEXT NOT NULL,
  updated_at             TEXT NOT NULL
);
CREATE UNIQUE INDEX idx_accounts_email ON accounts(lower(email));
CREATE UNIQUE INDEX idx_accounts_referral ON accounts(referral_code);
CREATE INDEX idx_accounts_stripe_sub ON accounts(stripe_subscription_id);

CREATE TABLE api_keys (
  id           TEXT PRIMARY KEY,
  account_id   TEXT NOT NULL REFERENCES accounts(id),
  name         TEXT NOT NULL,
  key_hash     TEXT NOT NULL,   -- SHA-256 of the presented key; the key itself is never stored
  prefix       TEXT NOT NULL,   -- first 8 chars, shown in the UI so keys are identifiable
  last_used_at TEXT,
  revoked_at   TEXT,
  created_at   TEXT NOT NULL
);
CREATE UNIQUE INDEX idx_api_keys_hash ON api_keys(key_hash);
CREATE INDEX idx_api_keys_account ON api_keys(account_id);

-- The creator's strategy: who they talk to, how they sound, what they will not say.
-- This is the cached prefix for every generation call, so it must be stable.
CREATE TABLE strategies (
  id             TEXT PRIMARY KEY,
  account_id     TEXT NOT NULL REFERENCES accounts(id),
  positioning    TEXT NOT NULL,
  audience       TEXT NOT NULL,
  tone           TEXT NOT NULL,
  proof_points   TEXT NOT NULL DEFAULT '[]',  -- JSON array of credibility anchors
  banned_phrases TEXT NOT NULL DEFAULT '[]',  -- JSON array; enforced post-generation
  cta_library    TEXT NOT NULL DEFAULT '[]',  -- JSON array of calls to action
  created_at     TEXT NOT NULL,
  updated_at     TEXT NOT NULL
);
CREATE UNIQUE INDEX idx_strategies_account ON strategies(account_id);

-- Content pillars. `weight` drives calendar allocation and is rewritten by the
-- growth engine from measured performance, which is what makes the system compound.
CREATE TABLE pillars (
  id          TEXT PRIMARY KEY,
  account_id  TEXT NOT NULL REFERENCES accounts(id),
  name        TEXT NOT NULL,
  description TEXT NOT NULL DEFAULT '',
  weight      REAL NOT NULL DEFAULT 1.0,
  active      INTEGER NOT NULL DEFAULT 1,
  created_at  TEXT NOT NULL,
  updated_at  TEXT NOT NULL
);
CREATE INDEX idx_pillars_account ON pillars(account_id, active);

CREATE TABLE channels (
  id                TEXT PRIMARY KEY,
  account_id        TEXT NOT NULL REFERENCES accounts(id),
  platform          TEXT NOT NULL,   -- x|linkedin|instagram|threads
  handle            TEXT NOT NULL,
  external_id       TEXT,
  access_token      TEXT,            -- encrypted at rest by the platform adapter layer
  refresh_token     TEXT,
  token_expires_at  TEXT,
  status            TEXT NOT NULL DEFAULT 'connected',  -- connected|expired|revoked|error
  posts_per_week    INTEGER NOT NULL DEFAULT 5,
  last_error        TEXT,
  connected_at      TEXT NOT NULL,
  updated_at        TEXT NOT NULL
);
CREATE INDEX idx_channels_account ON channels(account_id, status);
CREATE UNIQUE INDEX idx_channels_platform_handle ON channels(account_id, platform, handle);

-- A slot is an intent to publish: this channel, this pillar, this moment.
-- Slots are created by the strategy engine before any content exists.
CREATE TABLE slots (
  id            TEXT PRIMARY KEY,
  account_id    TEXT NOT NULL REFERENCES accounts(id),
  channel_id    TEXT NOT NULL REFERENCES channels(id),
  pillar_id     TEXT NOT NULL REFERENCES pillars(id),
  scheduled_for TEXT NOT NULL,
  status        TEXT NOT NULL DEFAULT 'planned',
                -- planned|drafting|ready|approved|publishing|published|failed|skipped
  created_at    TEXT NOT NULL,
  updated_at    TEXT NOT NULL
);
CREATE INDEX idx_slots_due ON slots(status, scheduled_for);
CREATE INDEX idx_slots_account ON slots(account_id, scheduled_for);
CREATE UNIQUE INDEX idx_slots_channel_time ON slots(channel_id, scheduled_for);

CREATE TABLE posts (
  id               TEXT PRIMARY KEY,
  account_id       TEXT NOT NULL REFERENCES accounts(id),
  slot_id          TEXT NOT NULL REFERENCES slots(id),
  channel_id       TEXT NOT NULL REFERENCES channels(id),
  pillar_id        TEXT NOT NULL REFERENCES pillars(id),
  variant          INTEGER NOT NULL DEFAULT 1,
  hook             TEXT NOT NULL DEFAULT '',
  body             TEXT NOT NULL,
  media_keys       TEXT NOT NULL DEFAULT '[]',  -- JSON array of R2 object keys
  status           TEXT NOT NULL DEFAULT 'draft',
                   -- draft|approved|publishing|published|failed|rejected
  approved_at      TEXT,
  approved_by      TEXT,   -- 'autopilot' or an account/user identifier
  published_at     TEXT,
  external_post_id TEXT,
  external_url     TEXT,
  recycled_from    TEXT REFERENCES posts(id),
  generation_meta  TEXT NOT NULL DEFAULT '{}',  -- JSON: model, tokens, cache hits
  last_error       TEXT,
  created_at       TEXT NOT NULL,
  updated_at       TEXT NOT NULL
);
CREATE INDEX idx_posts_slot ON posts(slot_id);
CREATE INDEX idx_posts_account_status ON posts(account_id, status);
CREATE INDEX idx_posts_published ON posts(account_id, published_at);

CREATE TABLE post_metrics (
  id          TEXT PRIMARY KEY,
  post_id     TEXT NOT NULL REFERENCES posts(id),
  account_id  TEXT NOT NULL REFERENCES accounts(id),
  captured_at TEXT NOT NULL,
  impressions INTEGER NOT NULL DEFAULT 0,
  likes       INTEGER NOT NULL DEFAULT 0,
  comments    INTEGER NOT NULL DEFAULT 0,
  shares      INTEGER NOT NULL DEFAULT 0,
  saves       INTEGER NOT NULL DEFAULT 0,
  clicks      INTEGER NOT NULL DEFAULT 0,
  follows     INTEGER NOT NULL DEFAULT 0,
  score       REAL NOT NULL DEFAULT 0  -- normalized engagement, see engines/growth.ts
);
CREATE INDEX idx_metrics_post ON post_metrics(post_id, captured_at);
CREATE INDEX idx_metrics_account ON post_metrics(account_id, captured_at);

-- Inbound conversations. This is the half of the job the creator most wants back:
-- reading and answering messages.
CREATE TABLE conversations (
  id                 TEXT PRIMARY KEY,
  account_id         TEXT NOT NULL REFERENCES accounts(id),
  channel_id         TEXT NOT NULL REFERENCES channels(id),
  platform_thread_id TEXT NOT NULL,
  author_handle      TEXT NOT NULL,
  intent             TEXT NOT NULL DEFAULT 'unclassified',
                     -- question|praise|lead|support|collab|spam|hostile|unclassified
  priority           INTEGER NOT NULL DEFAULT 3,  -- 1 highest .. 5 lowest
  status             TEXT NOT NULL DEFAULT 'open',  -- open|awaiting_review|answered|ignored
  last_message_at    TEXT NOT NULL,
  created_at         TEXT NOT NULL,
  updated_at         TEXT NOT NULL
);
CREATE UNIQUE INDEX idx_convos_thread ON conversations(channel_id, platform_thread_id);
CREATE INDEX idx_convos_triage ON conversations(account_id, status, priority);

CREATE TABLE messages (
  id              TEXT PRIMARY KEY,
  conversation_id TEXT NOT NULL REFERENCES conversations(id),
  account_id      TEXT NOT NULL REFERENCES accounts(id),
  direction       TEXT NOT NULL,  -- inbound|outbound
  body            TEXT NOT NULL,
  external_id     TEXT,
  created_at      TEXT NOT NULL
);
CREATE INDEX idx_messages_convo ON messages(conversation_id, created_at);
CREATE UNIQUE INDEX idx_messages_external ON messages(conversation_id, external_id);

CREATE TABLE reply_drafts (
  id              TEXT PRIMARY KEY,
  conversation_id TEXT NOT NULL REFERENCES conversations(id),
  account_id      TEXT NOT NULL REFERENCES accounts(id),
  body            TEXT NOT NULL,
  confidence      REAL NOT NULL DEFAULT 0,
  status          TEXT NOT NULL DEFAULT 'pending',  -- pending|approved|sent|rejected
  auto_approved   INTEGER NOT NULL DEFAULT 0,
  sent_at         TEXT,
  created_at      TEXT NOT NULL,
  updated_at      TEXT NOT NULL
);
CREATE INDEX idx_drafts_convo ON reply_drafts(conversation_id, status);
CREATE INDEX idx_drafts_pending ON reply_drafts(account_id, status);

-- Per-intent rules deciding what may be sent without a human reading it.
CREATE TABLE reply_rules (
  id             TEXT PRIMARY KEY,
  account_id     TEXT NOT NULL REFERENCES accounts(id),
  intent         TEXT NOT NULL,
  action         TEXT NOT NULL,  -- auto_send|queue_for_review|ignore
  min_confidence REAL NOT NULL DEFAULT 0.8,
  active         INTEGER NOT NULL DEFAULT 1,
  created_at     TEXT NOT NULL
);
CREATE UNIQUE INDEX idx_reply_rules ON reply_rules(account_id, intent);

-- Governance surface. Every autonomous loop reads this before acting, so the
-- operator always has a stop condition and a per-day ceiling.
CREATE TABLE automation_controls (
  account_id            TEXT PRIMARY KEY REFERENCES accounts(id),
  autopilot_publishing  INTEGER NOT NULL DEFAULT 0,
  autopilot_replies     INTEGER NOT NULL DEFAULT 0,
  paused_until          TEXT,
  daily_publish_cap     INTEGER NOT NULL DEFAULT 10,
  daily_reply_cap       INTEGER NOT NULL DEFAULT 25,
  updated_at            TEXT NOT NULL
);

-- Durable job queue. Cloudflare Queues would work, but a D1-backed queue keeps
-- the whole system testable locally and gives us an inspectable backlog.
CREATE TABLE jobs (
  id              TEXT PRIMARY KEY,
  account_id      TEXT REFERENCES accounts(id),
  kind            TEXT NOT NULL,
  payload         TEXT NOT NULL DEFAULT '{}',
  run_after       TEXT NOT NULL,
  status          TEXT NOT NULL DEFAULT 'pending',  -- pending|running|done|failed|dead
  attempts        INTEGER NOT NULL DEFAULT 0,
  max_attempts    INTEGER NOT NULL DEFAULT 5,
  locked_until    TEXT,
  idempotency_key TEXT,
  last_error      TEXT,
  created_at      TEXT NOT NULL,
  updated_at      TEXT NOT NULL
);
CREATE INDEX idx_jobs_claim ON jobs(status, run_after);
CREATE UNIQUE INDEX idx_jobs_idem ON jobs(idempotency_key);

-- Append-only audit trail. Required by the ethical-governance layer for any
-- automated pipeline: what acted, on what, when, and why.
CREATE TABLE audit_events (
  id          TEXT PRIMARY KEY,
  account_id  TEXT REFERENCES accounts(id),
  actor       TEXT NOT NULL,  -- 'system:<engine>' or an account/user identifier
  action      TEXT NOT NULL,
  entity_type TEXT NOT NULL,
  entity_id   TEXT,
  detail      TEXT NOT NULL DEFAULT '{}',
  created_at  TEXT NOT NULL
);
CREATE INDEX idx_audit_account ON audit_events(account_id, created_at);
CREATE INDEX idx_audit_entity ON audit_events(entity_type, entity_id);

-- Metered usage, per billing period. Drives plan limits and overage.
CREATE TABLE usage_counters (
  account_id TEXT NOT NULL REFERENCES accounts(id),
  period     TEXT NOT NULL,  -- YYYY-MM
  metric     TEXT NOT NULL,  -- posts_published|replies_sent|drafts_generated|ai_input_tokens|ai_output_tokens
  value      INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (account_id, period, metric)
);

CREATE TABLE referrals (
  id                  TEXT PRIMARY KEY,
  referrer_account_id TEXT NOT NULL REFERENCES accounts(id),
  referred_account_id TEXT NOT NULL REFERENCES accounts(id),
  status              TEXT NOT NULL DEFAULT 'pending',  -- pending|qualified|rewarded|void
  reward_applied_at   TEXT,
  created_at          TEXT NOT NULL
);
CREATE UNIQUE INDEX idx_referrals_referred ON referrals(referred_account_id);
CREATE INDEX idx_referrals_referrer ON referrals(referrer_account_id, status);
