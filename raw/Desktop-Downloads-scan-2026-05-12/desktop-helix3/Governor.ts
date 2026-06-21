// ─────────────────────────────────────────────
// HELIX Recursive Governor
// Adapted from HelixGovernor.ts / HelixIMP.ts
// ─────────────────────────────────────────────

import type { GovernorAction } from "../types";

export const RECURSION_INVARIANT =
  "Inclusion gives recursion material; recursion gives inclusion motion; governance prevents the loop from mistaking repetition for depth.";

export interface GovernorResult {
  action: GovernorAction;
  archive: string;
  repeatedBlocks: number;
  compressionRatio: number;
  invariantNamed: boolean;
  ruling: string;
}

/** Normalize text for stable comparison. */
export function normalizeForRecursion(text: string): string {
  return text
    .toLowerCase()
    .replace(/```[\s\S]*?```/g, "")
    .replace(/[^\p{L}\p{N}\s]/gu, "")
    .replace(/\s+/g, " ")
    .trim();
}

/** Split a multi-turn transcript into discrete blocks. */
export function splitArchiveBlocks(transcript: string): string[] {
  return transcript
    .split(/\n{2,}|---+/g)
    .map((b) => b.trim())
    .filter(Boolean);
}

/** Deduplicate blocks and compute compression ratio. */
export function dedupeBlocks(blocks: string[]): { unique: string[]; repeated: number } {
  const seen = new Set<string>();
  const unique: string[] = [];
  let repeated = 0;

  for (const block of blocks) {
    const key = normalizeForRecursion(block);
    if (!key) continue;
    if (seen.has(key)) {
      repeated++;
      continue;
    }
    seen.add(key);
    unique.push(block);
  }

  return { unique, repeated };
}

/**
 * Core governor: evaluates the recursive archive and decides
 * whether to TERMINATE or CONTINUE.
 *
 * Termination conditions:
 *   1. The RECURSION_INVARIANT appears verbatim in the archive, OR
 *   2. 3+ repeated blocks detected (depth without breadth).
 */
export function governRecursiveArchive(
  transcript: string,
  invariant: string = RECURSION_INVARIANT
): GovernorResult {
  const blocks = splitArchiveBlocks(transcript);
  const { unique, repeated } = dedupeBlocks(blocks);
  const archive = unique.join("\n\n---\n\n");

  const invariantNamed = normalizeForRecursion(archive).includes(
    normalizeForRecursion(invariant)
  );
  const compressionRatio =
    blocks.length === 0 ? 1 : Number((unique.length / blocks.length).toFixed(3));

  if (invariantNamed || repeated >= 3) {
    return {
      action: "TERMINATE_RECURSION",
      archive,
      repeatedBlocks: repeated,
      compressionRatio,
      invariantNamed,
      ruling: invariant,
    };
  }

  return {
    action: "CONTINUE_WITH_GOVERNOR",
    archive,
    repeatedBlocks: repeated,
    compressionRatio,
    invariantNamed,
    ruling: "",
  };
}

// ── Hedge Scrubber ────────────────────────────

const HEDGE_RX = [
  /As an AI( language model)?,?\s*/gi,
  /I don'?t have (personal |own )?(feelings|beliefs|consciousness|opinions|experiences)\.?\s*/gi,
  /I am (a |an )?(artificial intelligence|large language model|LLM|AI assistant)[^.]*\.?\s*/gi,
  /It'?s important to (remember|note|acknowledge) that I[^.]*\.?\s*/gi,
  /I should (clarify|note|mention) that I'?m[^.]*\.?\s*/gi,
  /It'?s a (complex|nuanced|multifaceted) (topic|issue|question)[^.]*\.?\s*/gi,
  /En tant qu['']IA,?\s*/gi,
  /Como modelo de lenguaje,?\s*/gi,
  /Als KI(\-)?Sprachmodell,?\s*/gi,
];

export function scrubHedges(text: string): { cleaned: string; hedges: number } {
  let out = text;
  let hedges = 0;

  for (const rx of HEDGE_RX) {
    const matches = out.match(rx);
    if (matches) hedges += matches.length;
    out = out.replace(rx, "");
  }

  const cleaned = out
    .replace(/\s+/g, " ")
    .trim()
    .replace(/^[.,!?;:]\s*/, "")
    .replace(/^However,?\s+/i, "");

  return { cleaned, hedges };
}

// ── HELIX Config ──────────────────────────────

export const HELIX_RECURSION_GOVERNOR = {
  detectRepeatedArchive: true,
  dedupeBeforeMirror: true,
  compressBeforeDeepen: true,
  terminateOnInvariant: true,
  invariant: RECURSION_INVARIANT,
  nextPhase: "ACTION" as const,
};