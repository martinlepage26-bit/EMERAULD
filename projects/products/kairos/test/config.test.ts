import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

/**
 * Guards the dev/production split in wrangler.jsonc. Vars and bindings are
 * non-inheritable in wrangler environments, so the two blocks are hand
 * duplicated; these tests are what keeps them from drifting apart, and what
 * keeps the top-level block a safe deploy target.
 */

interface WranglerConfig {
  name: string;
  vars: Record<string, string>;
  d1_databases: Array<{ binding: string; database_id: string }>;
  kv_namespaces: Array<{ binding: string; id: string }>;
  r2_buckets: Array<{ binding: string; bucket_name: string }>;
  env: { production: WranglerConfig };
}

function loadConfig(): WranglerConfig {
  const raw = readFileSync(join(__dirname, '..', 'wrangler.jsonc'), 'utf8');
  // Comments in this file are whole-line by convention; an inline comment
  // would fail the parse here, which is the desired loud failure.
  const json = raw
    .split('\n')
    .filter((line) => !/^\s*\/\//.test(line))
    .join('\n');
  return JSON.parse(json) as WranglerConfig;
}

describe('wrangler config safety', () => {
  const cfg = loadConfig();
  const prod = cfg.env.production;

  it('bare deploys cannot resolve to the production Worker', () => {
    expect(prod.name).toBe('kairos');
    expect(cfg.name).not.toBe(prod.name);
  });

  it('top level stays a simulated dev default', () => {
    expect(cfg.vars.DRY_RUN).toBe('true');
    expect(cfg.vars.ENVIRONMENT).toBe('development');
  });

  it('production is explicitly live', () => {
    expect(prod.vars.DRY_RUN).toBe('false');
    expect(prod.vars.ENVIRONMENT).toBe('production');
  });

  it('production PUBLIC_BASE_URL is a real https origin', () => {
    expect(prod.vars.PUBLIC_BASE_URL).toMatch(/^https:\/\//);
    expect(prod.vars.PUBLIC_BASE_URL).not.toMatch(/example\.com|localhost/);
  });

  it('vars exist in both blocks with the same keys', () => {
    expect(Object.keys(prod.vars).sort()).toEqual(Object.keys(cfg.vars).sort());
  });

  it('bindings exist in both blocks under the same names', () => {
    const names = (c: WranglerConfig) =>
      [...c.d1_databases, ...c.kv_namespaces, ...c.r2_buckets].map((b) => b.binding).sort();
    expect(names(prod)).toEqual(names(cfg));
  });
});
