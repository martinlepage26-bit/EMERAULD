-- Agent mode: model requests handed to an out-of-band worker (a headless
-- Claude Code session) instead of the Messages API. The row is keyed by a hash
-- of the request, so a retried job finds the answer to the call it made.
CREATE TABLE agent_work (
  id           TEXT PRIMARY KEY,
  request_key  TEXT NOT NULL UNIQUE,
  account_id   TEXT,
  model        TEXT NOT NULL,
  request      TEXT NOT NULL,          -- JSON: system blocks, user prompt, schema
  status       TEXT NOT NULL DEFAULT 'pending',   -- pending | done
  result       TEXT,
  worker_meta  TEXT NOT NULL DEFAULT '{}',        -- JSON: session id, duration
  created_at   TEXT NOT NULL,
  completed_at TEXT
);
CREATE INDEX idx_agent_work_status ON agent_work(status, created_at);
