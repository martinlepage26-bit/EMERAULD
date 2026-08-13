import type { Env } from '../env';
import { db } from '../lib/db';
import type { AccountRecord, PillarRecord, StrategyRecord } from '../lib/types';
import { OPERATOR_SYSTEM } from '../ai/prompts';
import { notFound } from '../lib/errors';

export { generate, generateJson, recordUsage } from '../ai/claude';
export const OPERATOR_SYSTEM_REF = OPERATOR_SYSTEM;

export interface CreatorContext {
  account: AccountRecord;
  strategy: StrategyRecord;
  pillars: PillarRecord[];
}

/**
 * Loads the three records every generation call needs. Fetching them together
 * keeps the cached system prefix assembled the same way from every engine, which
 * is what makes the prefix cacheable across planning, drafting, and replies.
 */
export async function loadCreator(env: Env, accountId: string): Promise<CreatorContext> {
  const account = await db(env).first<AccountRecord>(
    `SELECT * FROM accounts WHERE id = ?`,
    accountId,
  );
  if (!account) throw notFound(`Account ${accountId}`);

  const strategy = await db(env).first<StrategyRecord>(
    `SELECT * FROM strategies WHERE account_id = ?`,
    accountId,
  );
  if (!strategy) throw notFound(`Strategy for account ${accountId}`);

  const pillars = await db(env).all<PillarRecord>(
    `SELECT * FROM pillars WHERE account_id = ? AND active = 1 ORDER BY name`,
    accountId,
  );

  return { account, strategy, pillars };
}
