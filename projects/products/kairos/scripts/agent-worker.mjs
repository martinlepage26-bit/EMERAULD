#!/usr/bin/env node
/**
 * Answers Kairos agent-mode work with headless Claude Code.
 *
 * Polls /v1/agent/work, runs `claude -p` once per item with no tools, no MCP
 * servers and no project instructions (prompt in, text out), and posts the
 * answer back. The parked job picks it up on its next retry, and every Kairos
 * check (schema, banned phrases, gates) still runs on what comes back.
 *
 * Env: KAIROS_URL (default http://127.0.0.1:3480), AGENT_TOKEN, CLAUDE_BIN,
 *      AGENT_MODEL (optional), POLL_SECONDS (default 15), ONCE=1 to run one pass.
 */
import { spawn } from 'node:child_process';

const BASE = (process.env.KAIROS_URL ?? 'http://127.0.0.1:3480').replace(/\/$/, '');
const TOKEN = process.env.AGENT_TOKEN;
const CLAUDE = process.env.CLAUDE_BIN ?? 'claude';
const POLL = Number(process.env.POLL_SECONDS ?? 15) * 1000;
const TIMEOUT = Number(process.env.ITEM_TIMEOUT_SECONDS ?? 600) * 1000;
if (!TOKEN) { console.error('AGENT_TOKEN is required'); process.exit(2); }

const auth = { authorization: `Bearer ${TOKEN}`, 'content-type': 'application/json' };

function runClaude(system, prompt) {
  return new Promise((resolve, reject) => {
    // Prompt goes first as an argument, not on stdin: the CT920 `claude` wrapper
    // does not forward stdin, and `--tools` is variadic so anything after it
    // would be read as a tool name.
    const args = ['-p', prompt, '--output-format', 'json', '--tools', '', '--safe-mode',
      '--strict-mcp-config', '--no-session-persistence', '--system-prompt', system];
    if (process.env.AGENT_MODEL) args.push('--model', process.env.AGENT_MODEL);
    const child = spawn(CLAUDE, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let out = ''; let err = '';
    const timer = setTimeout(() => { child.kill('SIGTERM'); reject(new Error('claude timed out')); }, TIMEOUT);
    child.stdout.on('data', (d) => { out += d; });
    child.stderr.on('data', (d) => { err += d; });
    child.on('error', (e) => { clearTimeout(timer); reject(e); });
    child.on('close', (code) => {
      clearTimeout(timer);
      if (code !== 0) return reject(new Error(`claude exited ${code}: ${(err || out).slice(0, 500)}`));
      try { resolve(JSON.parse(out)); } catch { reject(new Error(`unparseable claude output: ${out.slice(0, 300)}`)); }
    });
  });
}

/** Pulls the JSON object out of a reply that may wrap it in prose or a fence. */
function extractJson(text) {
  const t = text.trim();
  try { JSON.parse(t); return t; } catch { /* fall through */ }
  const fenced = t.match(/```(?:json)?\s*([\s\S]*?)```/);
  if (fenced) { try { JSON.parse(fenced[1]); return fenced[1].trim(); } catch { /* fall through */ } }
  const start = t.indexOf('{'); const end = t.lastIndexOf('}');
  if (start >= 0 && end > start) { const s = t.slice(start, end + 1); JSON.parse(s); return s; }
  throw new Error('reply contained no JSON object');
}

async function answer(item) {
  const system = item.system.join('\n\n');
  let prompt = item.user;
  if (item.schema) {
    prompt += '\n\nRespond with a single JSON object that validates against this JSON Schema, '
      + 'and nothing else: no prose, no code fence.\n' + JSON.stringify(item.schema);
  }
  const started = Date.now();
  const res = await runClaude(system, prompt);
  if (res.is_error) throw new Error(`claude reported an error: ${String(res.result).slice(0, 300)}`);
  let text = String(res.result ?? '');
  if (item.schema) text = extractJson(text);
  const r = await fetch(`${BASE}/v1/agent/work/${item.id}`, {
    method: 'POST', headers: auth,
    body: JSON.stringify({ text, meta: { session_id: res.session_id, duration_ms: Date.now() - started, cost_usd: res.total_cost_usd } }),
  });
  if (!r.ok) throw new Error(`submit failed ${r.status}: ${await r.text()}`);
  console.log(`answered ${item.id} in ${Math.round((Date.now() - started) / 1000)}s`);
}

async function pass() {
  const r = await fetch(`${BASE}/v1/agent/work?limit=5`, { headers: auth });
  if (!r.ok) throw new Error(`list failed ${r.status}`);
  const { work } = await r.json();
  for (const item of work) {
    try { await answer(item); } catch (e) { console.error(`item ${item.id}: ${e.message}`); }
  }
  return work.length;
}

do {
  try { await pass(); } catch (e) { console.error(`poll: ${e.message}`); }
  if (process.env.ONCE) break;
  await new Promise((r) => setTimeout(r, POLL));
} while (true);
