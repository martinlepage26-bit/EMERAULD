-- Webhook delivery dedupe. Stripe retries deliveries and does not guarantee
-- order, so every event id is applied at most once.
CREATE TABLE stripe_events (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  received_at TEXT NOT NULL
);
