import type { StrategyRecord, PillarRecord } from '../lib/types';

/**
 * The invariant half of every system prompt. This text is byte-identical across
 * all accounts and all calls, so it sits first in the prefix where the cache can
 * reach it. Changing a single character here invalidates every cached prefix in
 * the fleet, so treat edits as a deploy-level decision.
 */
export const OPERATOR_SYSTEM = `You write social content on behalf of a specific creator, inside an automated publishing system.

The creator is not reviewing most of what you produce before it goes out. Write accordingly: everything you return should be publishable as-is by someone who cares about their reputation.

What good output looks like here:
- It sounds like the creator described below, not like a brand account. Match their register, their sentence rhythm, and their level of directness.
- It says one thing. A post that makes three points makes none of them.
- The opening line earns the second line. Readers decide in about a second.
- Claims stay inside what the creator can actually support. When you are not certain of a fact, write around it rather than asserting it.
- No engagement bait, no manufactured outrage, no fake personal anecdotes, no invented statistics, and no claims about results the creator has not stated.

Formatting: plain text suited to the target platform. No markdown headers, no bold, no bullet characters unless the platform section says otherwise.`;

/** The creator-specific half of the cached prefix: stable per account. */
export function strategySystem(strategy: StrategyRecord, pillars: PillarRecord[]): string {
  const banned = safeArray(strategy.banned_phrases);
  const proof = safeArray(strategy.proof_points);
  const ctas = safeArray(strategy.cta_library);

  return [
    `# The creator`,
    ``,
    `Positioning: ${strategy.positioning}`,
    `Audience: ${strategy.audience}`,
    `Voice: ${strategy.tone}`,
    ``,
    proof.length ? `Things they can credibly claim:\n${proof.map((p) => `- ${p}`).join('\n')}` : '',
    ``,
    `# Content pillars`,
    pillars.map((p) => `- ${p.name}: ${p.description || 'no further detail given'}`).join('\n'),
    ``,
    ctas.length ? `# Calls to action they use\n${ctas.map((c) => `- ${c}`).join('\n')}` : '',
    ``,
    banned.length
      ? `# Never use these words or phrases\n${banned.map((b) => `- ${b}`).join('\n')}`
      : '',
  ]
    .filter(Boolean)
    .join('\n');
}

const PLATFORM_NOTES: Record<string, string> = {
  x: 'Under 280 characters. One idea. No hashtags. Line breaks are allowed and usually help.',
  linkedin:
    'Between 60 and 200 words. The first two lines appear before the "see more" fold, so the hook has to survive being cut there. At most one hashtag, and only if it is genuinely a topic tag. No "Agree?" closers.',
  instagram:
    'Caption between 40 and 150 words. Written to sit under an image. Up to five relevant hashtags on a final line.',
  threads: 'Under 500 characters. Conversational. No hashtags.',
};

export function platformNote(platform: string): string {
  return PLATFORM_NOTES[platform] ?? 'Keep it under 200 words and plain-text.';
}

// ---------------------------------------------------------------------------
// Calendar planning
// ---------------------------------------------------------------------------

export const CALENDAR_SCHEMA = {
  type: 'object',
  properties: {
    slots: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          pillar_name: { type: 'string' },
          day_offset: { type: 'integer' },
          hour_utc: { type: 'integer' },
          angle: { type: 'string', description: 'The specific take this slot should argue.' },
        },
        required: ['pillar_name', 'day_offset', 'hour_utc', 'angle'],
        additionalProperties: false,
      },
    },
  },
  required: ['slots'],
  additionalProperties: false,
} as const;

export function calendarPrompt(input: {
  platform: string;
  postsNeeded: number;
  horizonDays: number;
  pillars: PillarRecord[];
  recentAngles: string[];
}): string {
  return [
    `Plan ${input.postsNeeded} posts for ${input.platform} across the next ${input.horizonDays} days.`,
    ``,
    `Allocate across pillars roughly in proportion to these weights, which reflect what has actually performed for this creator:`,
    input.pillars.map((p) => `- ${p.name}: weight ${p.weight.toFixed(2)}`).join('\n'),
    ``,
    `For each slot give a specific angle, not a topic. "Why retainer pricing punishes your best clients" is an angle. "Pricing" is a topic.`,
    ``,
    input.recentAngles.length
      ? `These angles ran recently. Do not repeat them or restate them in different words:\n${input.recentAngles.map((a) => `- ${a}`).join('\n')}`
      : `This is the creator's first planned cycle, so establish range across the pillars.`,
    ``,
    `day_offset is days from today (0 = today). hour_utc is the publish hour in UTC, 0 to 23. Spread posts so no two land within four hours of each other.`,
  ].join('\n');
}

// ---------------------------------------------------------------------------
// Post drafting
// ---------------------------------------------------------------------------

export const DRAFT_SCHEMA = {
  type: 'object',
  properties: {
    variants: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          hook: { type: 'string', description: 'The opening line, repeated from the body.' },
          body: { type: 'string', description: 'The full post text, ready to publish.' },
        },
        required: ['hook', 'body'],
        additionalProperties: false,
      },
    },
  },
  required: ['variants'],
  additionalProperties: false,
} as const;

export function draftPrompt(input: {
  platform: string;
  pillarName: string;
  angle: string;
  variants: number;
  winningExamples: string[];
}): string {
  return [
    `Write ${input.variants} variants of one post for ${input.platform}.`,
    ``,
    `Pillar: ${input.pillarName}`,
    `Angle: ${input.angle}`,
    ``,
    `Platform constraints: ${platformNote(input.platform)}`,
    ``,
    input.winningExamples.length
      ? [
          `These posts performed well for this creator. Use them to calibrate voice and structure, not subject matter:`,
          input.winningExamples.map((e) => `---\n${e}`).join('\n'),
        ].join('\n')
      : '',
    ``,
    `The variants should differ in approach, not in wording. One might open on a claim, another on a concrete situation, another on a number. Returning three rephrasings of the same sentence is a failed response.`,
  ]
    .filter(Boolean)
    .join('\n');
}

// ---------------------------------------------------------------------------
// Inbound triage and replies
// ---------------------------------------------------------------------------

export const TRIAGE_SCHEMA = {
  type: 'object',
  properties: {
    intent: {
      type: 'string',
      enum: ['question', 'praise', 'lead', 'support', 'collab', 'spam', 'hostile'],
    },
    priority: { type: 'integer', enum: [1, 2, 3, 4, 5] },
    reasoning: { type: 'string' },
  },
  required: ['intent', 'priority', 'reasoning'],
  additionalProperties: false,
} as const;

export function triagePrompt(input: { author: string; messages: string[] }): string {
  return [
    `Classify this inbound conversation.`,
    ``,
    `From: ${input.author}`,
    input.messages.map((m) => `> ${m}`).join('\n'),
    ``,
    `intent options:`,
    `- lead: they are describing a problem the creator is paid to solve, or asking about working together`,
    `- question: a genuine question about the creator's subject matter`,
    `- support: something is broken, or they bought something and need help`,
    `- collab: podcast, newsletter swap, speaking, partnership`,
    `- praise: appreciation with no question in it`,
    `- spam: automated, promotional, or unrelated`,
    `- hostile: abusive, or arguing in bad faith`,
    ``,
    `priority 1 means the creator loses money or trust by not answering today. priority 5 means it never needs an answer.`,
  ].join('\n');
}

export const REPLY_SCHEMA = {
  type: 'object',
  properties: {
    reply: { type: 'string' },
    confidence: {
      type: 'number',
      description: '0 to 1. How safe this is to send without the creator reading it first.',
    },
    escalate: { type: 'boolean' },
    escalation_reason: { type: 'string' },
  },
  required: ['reply', 'confidence', 'escalate', 'escalation_reason'],
  additionalProperties: false,
} as const;

export function replyPrompt(input: {
  intent: string;
  author: string;
  messages: string[];
  platform: string;
}): string {
  return [
    `Draft the creator's reply to this ${input.intent} conversation on ${input.platform}.`,
    ``,
    `From: ${input.author}`,
    input.messages.map((m) => `> ${m}`).join('\n'),
    ``,
    `Keep it short. Most good replies on social are one or two sentences.`,
    ``,
    `Set confidence honestly, because it decides whether this sends without a human reading it. Lower it whenever the reply would commit the creator to something: a price, a deadline, a meeting, a factual claim about their work, or an opinion on a named person or company. Set escalate to true when the right reply depends on something only the creator knows.`,
  ].join('\n');
}

function safeArray(raw: string): string[] {
  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed.map(String) : [];
  } catch {
    return [];
  }
}
