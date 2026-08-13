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

  ANTHROPIC_API_KEY: string;
  STRIPE_SECRET_KEY: string;
  STRIPE_WEBHOOK_SECRET: string;
  AUTH_SIGNING_KEY: string;
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

export function jobBatchSize(env: Env): number {
  const n = Number.parseInt(env.JOB_BATCH_SIZE ?? '', 10);
  return Number.isFinite(n) && n > 0 ? n : 25;
}
