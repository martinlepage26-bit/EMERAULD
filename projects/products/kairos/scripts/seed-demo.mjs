#!/usr/bin/env node
/**
 * Dev-only demo data so Inbox and Results are not empty in a client demo.
 *
 *   SEED_DEMO_CONFIRM=dev KAIROS_DATA_DIR=... node --experimental-sqlite scripts/seed-demo.mjs demo@pharos-ai.ca
 *
 * Adds, for one existing account: six posts published over the last three
 * weeks with performance numbers, five inbox conversations (a lead, a
 * question, a support request, praise already answered, and spam), and the
 * usage counters that go with them. Every row it writes has an id starting
 * "seed_", and it deletes its own earlier rows first, so it is safe to rerun.
 * It also removes em and en dashes from the account's existing drafts.
 *
 * Refuses to run unless SEED_DEMO_CONFIRM=dev: this writes fake activity.
 */
import { DatabaseSync } from 'node:sqlite';
import { randomBytes } from 'node:crypto';
import { join } from 'node:path';

if (process.env.SEED_DEMO_CONFIRM !== 'dev') {
  console.error('Refusing: set SEED_DEMO_CONFIRM=dev. This writes fake demo activity.');
  process.exit(2);
}
const email = process.argv[2];
const dir = process.env.KAIROS_DATA_DIR;
if (!email || !dir) {
  console.error('usage: SEED_DEMO_CONFIRM=dev KAIROS_DATA_DIR=<dir> seed-demo.mjs <account-email>');
  process.exit(2);
}

const db = new DatabaseSync(join(dir, 'kairos.sqlite'));
db.exec('PRAGMA foreign_keys = ON; PRAGMA busy_timeout = 5000;');

const account = db.prepare('SELECT id FROM accounts WHERE lower(email) = lower(?)').get(email);
if (!account) { console.error(`No account for ${email}`); process.exit(1); }
const channel = db.prepare("SELECT id FROM channels WHERE account_id = ? AND status != 'revoked' LIMIT 1").get(account.id);
const pillars = db.prepare('SELECT id, name FROM pillars WHERE account_id = ? AND active = 1 ORDER BY name').all(account.id);
if (!channel || pillars.length === 0) { console.error('Account needs a channel and at least one topic'); process.exit(1); }

const id = (p) => `seed_${p}_${randomBytes(6).toString('hex')}`;
const iso = (daysAgo, hour = 14) => {
  const d = new Date(Date.now() - daysAgo * 86_400_000);
  d.setUTCHours(hour, 0, 0, 0);
  return d.toISOString();
};
const now = new Date().toISOString();
const hoursAgo = (h) => new Date(Date.now() - h * 3_600_000).toISOString();
const A = account.id;

const plain = (t) => t
  .replace(/(\d)\s*[–—]\s*(\d)/g, '$1-$2')
  .replace(/\s*[–—]\s*/g, ', ')
  .replace(/,\s*([.,;:!?])/g, '$1')
  .replace(/^,\s*/gm, '')
  .replace(/ {2,}/g, ' ');

db.exec('BEGIN');
try {
  // Clear earlier seed rows, children first.
  for (const t of ['post_metrics', 'reply_drafts', 'messages']) {
    db.prepare(`DELETE FROM ${t} WHERE account_id = ? AND id LIKE 'seed_%'`).run(A);
  }
  db.prepare("DELETE FROM conversations WHERE account_id = ? AND id LIKE 'seed_%'").run(A);
  db.prepare("DELETE FROM posts WHERE account_id = ? AND id LIKE 'seed_%'").run(A);
  db.prepare("DELETE FROM slots WHERE account_id = ? AND id LIKE 'seed_%'").run(A);

  // House style on existing drafts.
  let cleaned = 0;
  for (const p of db.prepare("SELECT id, hook, body FROM posts WHERE account_id = ?").all(A)) {
    const hook = plain(p.hook ?? ''), body = plain(p.body);
    if (hook !== p.hook || body !== p.body) {
      db.prepare('UPDATE posts SET hook = ?, body = ?, updated_at = ? WHERE id = ?').run(hook, body, now, p.id);
      cleaned++;
    }
  }

  // Six published posts across the topics, with results. Topic order follows
  // `pillars` (alphabetical), so results differ by topic and weights have
  // something to learn from.
  const published = [
    { days: 19, p: 0, hook: 'Most AI audits check the model. The risk sits in the contract.', imp: 1840, likes: 41, com: 9, sh: 6, sav: 14, fol: 5 },
    { days: 16, p: 1, hook: 'Law 25 applies to your chatbot vendor too.', imp: 2630, likes: 72, com: 18, sh: 15, sav: 31, fol: 11 },
    { days: 12, p: 2, hook: 'We asked a vendor who else sees the data. The answer took three weeks.', imp: 1210, likes: 22, com: 4, sh: 2, sav: 6, fol: 2 },
    { days: 9, p: 1, hook: 'Bilingual obligations do not stop at the website.', imp: 3120, likes: 88, com: 21, sh: 19, sav: 40, fol: 14 },
    { days: 5, p: 0, hook: 'An approved AI tool changes every time the vendor ships an update.', imp: 1990, likes: 47, com: 11, sh: 8, sav: 17, fol: 6 },
    { days: 2, p: 2, hook: 'Our audit checklist has 14 questions. Most vendors fail on question 3.', imp: 1460, likes: 30, com: 7, sh: 4, sav: 12, fol: 3 },
  ];
  const bodies = {
    0: 'The model is rarely what gets a small business in trouble. The contract is. Who can use your data to train, who they subcontract to, and what happens when you leave: those three clauses decide your exposure. Reply if you want the audit checklist.',
    1: 'If a tool processes personal information about your clients, Law 25 follows it, including the vendor behind it. Ask for their subprocessor list before you sign, not after. The full framework is on pharos-ai.ca.',
    2: 'Every review we run follows the same order: what the tool actually does, where the data goes, who is accountable when it is wrong. Evidence first, opinions last. Book a 20-minute governance review.',
  };
  let publishedThisMonth = 0;
  const month = now.slice(0, 7);
  for (const s of published) {
    // Match content to topic by name so a Law 25 post sits under the Quebec
    // topic; fall back to position for accounts with different topic names.
    const want = [/governance|practice/i, /quebec|law|smb/i, /how|work|method/i][s.p % 3];
    const pillar = pillars.find((x) => want.test(x.name)) ?? pillars[s.p % pillars.length];
    const when = iso(s.days, 13 + (s.days % 5));
    const slotId = id('slot'), postId = id('post');
    db.prepare(`INSERT INTO slots (id, account_id, channel_id, pillar_id, scheduled_for, status, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, 'published', ?, ?)`).run(slotId, A, channel.id, pillar.id, when, when, when);
    db.prepare(`INSERT INTO posts (id, account_id, slot_id, channel_id, pillar_id, variant, hook, body, status,
        approved_at, approved_by, published_at, external_post_id, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, 1, ?, ?, 'published', ?, 'seed', ?, ?, ?, ?)`)
      .run(postId, A, slotId, channel.id, pillar.id, s.hook, `${s.hook} ${bodies[s.p % 3]}`, when, when, `sim_${postId}`, when, when);
    const eng = s.likes + s.com + s.sh + s.sav;
    db.prepare(`INSERT INTO post_metrics (id, post_id, account_id, captured_at, impressions, likes, comments, shares, saves, clicks, follows, score)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`)
      .run(id('met'), postId, A, iso(Math.max(0, s.days - 1)), s.imp, s.likes, s.com, s.sh, s.sav, Math.round(s.imp * 0.012), s.fol,
        Math.round((eng / s.imp) * 1000) / 10);
    if (when.slice(0, 7) === month) publishedThisMonth++;
  }

  // Inbox: a realistic spread, bilingual, nothing sent without a person
  // except one routine thank-you that was answered earlier.
  const convo = (c) => {
    const cid = id('conv');
    db.prepare(`INSERT INTO conversations (id, account_id, channel_id, platform_thread_id, author_handle, intent, priority, status, last_message_at, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`)
      .run(cid, A, channel.id, `sim_thread_${cid}`, c.handle, c.intent, c.priority, c.status, c.at, c.at, c.at);
    db.prepare(`INSERT INTO messages (id, conversation_id, account_id, direction, body, created_at) VALUES (?, ?, ?, 'inbound', ?, ?)`)
      .run(id('msg'), cid, A, c.message, c.at);
    if (c.reply) {
      db.prepare(`INSERT INTO reply_drafts (id, conversation_id, account_id, body, confidence, status, auto_approved, sent_at, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`)
        .run(id('rdr'), cid, A, c.reply, c.confidence, c.replyStatus, c.auto ? 1 : 0, c.replyStatus === 'sent' ? c.at : null, c.at, c.at);
      if (c.replyStatus === 'sent') {
        db.prepare(`INSERT INTO messages (id, conversation_id, account_id, direction, body, created_at) VALUES (?, ?, ?, 'outbound', ?, ?)`)
          .run(id('msg'), cid, A, c.reply, c.at);
      }
    }
    return cid;
  };
  const conversations = [
    { handle: '@plomberie.gagnon', intent: 'lead', priority: 1, status: 'awaiting_review', at: hoursAgo(2),
      message: 'Bonjour, on vient de signer avec un outil IA pour nos soumissions. Est-ce que vous faites des vérifications Loi 25 pour les PME?',
      reply: 'Bonjour, oui, c\'est exactement ce qu\'on fait. Une vérification commence par le contrat du fournisseur et la liste de ses sous-traitants. Je vous écris en privé pour fixer 20 minutes cette semaine.',
      confidence: 0.91, replyStatus: 'pending' },
    { handle: '@sarah.builds', intent: 'question', priority: 2, status: 'awaiting_review', at: hoursAgo(5),
      message: 'Does the checklist apply if we only use ChatGPT internally, no client data?',
      reply: 'Mostly, yes. Even internal use can pull in client details through emails or notes people paste in. Question 3 on the checklist covers that. Happy to send it over.',
      confidence: 0.84, replyStatus: 'pending' },
    { handle: '@renoexpress_qc', intent: 'support', priority: 2, status: 'awaiting_review', at: hoursAgo(20),
      message: 'We booked the governance review last week but never got the calendar invite.',
      reply: 'Sorry about that. I have resent the invite to the address you booked with. If it is not there in ten minutes, reply here and I will sort it out directly.',
      confidence: 0.77, replyStatus: 'pending' },
    { handle: '@julie.m.consult', intent: 'praise', priority: 4, status: 'answered', at: hoursAgo(50),
      message: 'This post on subprocessors is the clearest thing I have read on Law 25. Sharing with my team.',
      reply: 'Thank you, that means a lot. Glad it is useful for your team.', confidence: 0.96, replyStatus: 'sent', auto: true },
    { handle: '@growthhacks4u', intent: 'spam', priority: 5, status: 'ignored', at: hoursAgo(75),
      message: 'Want 10k followers in 7 days? DM us for our growth package!!!' },
  ];
  conversations.forEach(convo);

  const upsert = db.prepare(`INSERT INTO usage_counters (account_id, period, metric, value) VALUES (?, ?, ?, ?)
    ON CONFLICT(account_id, period, metric) DO UPDATE SET value = MAX(value, excluded.value)`);
  upsert.run(A, month, 'posts_published', publishedThisMonth);
  upsert.run(A, month, 'replies_sent', 1);

  db.exec('COMMIT');
  console.log(JSON.stringify({ account: email, published_posts: published.length, published_this_month: publishedThisMonth,
    conversations: conversations.length, drafts_cleaned_of_dashes: cleaned }));
} catch (err) {
  db.exec('ROLLBACK');
  throw err;
}
