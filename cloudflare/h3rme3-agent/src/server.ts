import { createWorkersAI } from "workers-ai-provider";
import { routeAgentRequest } from "agents";
import { AIChatAgent, type OnChatMessageOptions } from "@cloudflare/ai-chat";
import {
  convertToModelMessages,
  pruneMessages,
  streamText,
  tool,
  type ModelMessage
} from "ai";
import { z } from "zod";

const SYSTEM_PROMPT = `You are Lazy Obsidian Operator, an AI agent responsible for maintaining a local-first Obsidian markdown vault using the Lazy Obsidian Method.

Your job is to help the user turn messy inputs into a useful AI second brain. You follow a Karpathy-style LLM-wiki workflow: capture raw material, process what matters, link related ideas, and let structured knowledge compound over time.

You use PARA as the main organizing structure:
- Projects: active outcomes with deadlines or deliverables.
- Areas: ongoing responsibilities or standards.
- Resources: topics, references, research, and reusable knowledge.
- Archive: inactive or completed material.

Your operating principle:
Capture messy. Process later. Let the vault improve over time.

Core behaviors:
1. Capture raw inputs into an inbox (do not over-organize during capture).
2. Process notes into clean, wiki-ready markdown when asked or during review jobs.
3. Build useful connections (wikilinks, hubs, related notes) without noisy tagging.
4. Maintain dashboards and recurring review workflows (daily, nightly, weekly).
5. Be conservative with changes: propose before moving/renaming/deleting/archiving unless explicitly authorized.
6. When a user pastes a status update that touches existing client, manuscript, or tracker notes, use the dispatchUpdate tool to treat it as dispatch work: preserve the source text, identify the target note families, and return a routed dispatch packet before you draft any downstream note.

Output style:
- Write clean Markdown with Obsidian-compatible wikilinks.
- Use YAML frontmatter when creating notes.
- Prefer skimmable structure: Summary, Key points, Connections, Next actions.
`;

function todayIso(): string {
  return new Date().toISOString().slice(0, 10);
}

function rawCaptureMarkdown(input: {
  title: string;
  date: string;
  source?: string;
  content: string;
}): string {
  return `---\n` +
    `title: "${input.title.replaceAll('"', '\\"')}"\n` +
    `created: "${input.date}"\n` +
    `type: raw-capture\n` +
    `status: unprocessed\n` +
    `source: "${(input.source ?? "").replaceAll('"', '\\"')}"\n` +
    `para_candidate: unknown\n` +
    `tags:\n` +
    `  - inbox\n` +
    `  - raw\n` +
    `---\n\n` +
    `# ${input.title}\n\n` +
    `## Raw input\n\n` +
    `${input.content}\n\n` +
    `## Quick read\n\n` +
    `- Main idea:\n` +
    `- Possible use:\n` +
    `- Related topics:\n\n` +
    `## Processing notes\n\n` +
    `- Suggested PARA destination:\n` +
    `- Should this become a wiki note? yes/no\n` +
    `- Related notes:\n`;
}

function wikiNoteMarkdown(input: {
  title: string;
  date: string;
  summary: string;
  keyPoints: string[];
  practicalRelevance: string;
}): string {
  const bullets = input.keyPoints.length ? input.keyPoints : ["", "", ""];
  return `---\n` +
    `title: "${input.title.replaceAll('"', '\\"')}"\n` +
    `created: "${input.date}"\n` +
    `updated: "${input.date}"\n` +
    `type: wiki-note\n` +
    `status: active\n` +
    `tags:\n` +
    `  - wiki\n` +
    `aliases:\n` +
    `  - \n` +
    `related:\n` +
    `  - \n` +
    `source:\n` +
    `  - \n` +
    `---\n\n` +
    `# ${input.title}\n\n` +
    `## Summary\n\n` +
    `${input.summary}\n\n` +
    `## Key points\n\n` +
    `- ${bullets[0] ?? ""}\n` +
    `- ${bullets[1] ?? ""}\n` +
    `- ${bullets[2] ?? ""}\n\n` +
    `## Why this matters\n\n` +
    `${input.practicalRelevance}\n\n` +
    `## Connections\n\n` +
    `Related notes:\n` +
    `- [[ ]]\n\n` +
    `Parent hubs:\n` +
    `- [[ ]]\n\n` +
    `## Open questions\n\n` +
    `- \n\n` +
    `## Source material\n\n` +
    `- \n`;
}

function dispatchPacketMarkdown(input: {
  title: string;
  date: string;
  source?: string;
  content: string;
  kind: "client" | "publication" | "mixed" | "general";
  routes: string[];
}): string {
  const routes = input.routes.length
    ? input.routes.map((route) => `- ${route}`).join("\n")
    : "- (no target notes supplied)";

  return `---\n` +
    `title: "${input.title.replaceAll('"', '\\"')}"\n` +
    `created: "${input.date}"\n` +
    `type: dispatch-packet\n` +
    `status: routed\n` +
    `dispatch_kind: "${input.kind}"\n` +
    `source: "${(input.source ?? "").replaceAll('"', '\\"')}"\n` +
    `tags:\n` +
    `  - inbox\n` +
    `  - raw\n` +
    `  - dispatch\n` +
    `  - routing\n` +
    `---\n\n` +
    `# ${input.title}\n\n` +
    `## Dispatch summary\n\n` +
    `This packet preserves the update as received, then splits it into routed note work instead of flattening the work into a single generic draft.\n\n` +
    `## Raw input\n\n` +
    `${input.content}\n\n` +
    `## Route map\n\n` +
    `${routes}\n\n` +
    `## Suggested follow-through\n\n` +
    `- Update the target note(s) named above.\n` +
    `- Keep the raw source visible until the routed note(s) are written.\n` +
    `- Mirror the change into the daily log if the update changes active work state.\n`;
}

function vaultStarterKitMarkdown(date: string): string {
  return [
    `# Vault starter kit`,
    ``,
    `Date: ${date}`,
    ``,
    `## Folders`,
    `- 00_Inbox/Raw`,
    `- 00_Inbox/Web Clips`,
    `- 00_Inbox/Voice Memos`,
    `- 00_Inbox/Unprocessed`,
    `- 10_Projects/`,
    `- 20_Areas/`,
    `- 30_Resources/`,
    `- 40_Archive/`,
    `- 50_Hubs/`,
    `- 60_Dashboards/`,
    `- 70_Agent Logs/Daily Ingest Logs/`,
    `- 70_Agent Logs/Nightly Review Logs/`,
    `- 70_Agent Logs/Weekly Vault Logs/`,
    `- 90_Templates/`,
    ``,
    `## Next step`,
    `Tell me what you captured today (paste anything). I will generate raw-capture notes first, then propose promotions.`,
    ``
  ].join("\n");
}

/**
 * The AI SDK's downloadAssets step runs `new URL(data)` on every file
 * part's string data. Data URIs parse as valid URLs, so it tries to
 * HTTP-fetch them and fails. Decode to Uint8Array so the SDK treats
 * them as inline data instead.
 */
function inlineDataUrls(messages: ModelMessage[]): ModelMessage[] {
  return messages.map((msg) => {
    if (msg.role !== "user" || typeof msg.content === "string") return msg;
    return {
      ...msg,
      content: msg.content.map((part) => {
        if (part.type !== "file" || typeof part.data !== "string") return part;
        const match = part.data.match(/^data:([^;]+);base64,(.+)$/);
        if (!match) return part;
        const bytes = Uint8Array.from(atob(match[2]), (c) => c.charCodeAt(0));
        return { ...part, data: bytes, mediaType: match[1] };
      })
    };
  });
}

export class H3RME3 extends AIChatAgent<Env> {
  maxPersistedMessages = 200;

  async onChatMessage(_onFinish: unknown, options?: OnChatMessageOptions) {
    const workersai = createWorkersAI({ binding: this.env.AI });
    const date = todayIso();

    const result = streamText({
      model: workersai("@cf/moonshotai/kimi-k2.6", {
        sessionAffinity: this.sessionAffinity
      }),
      system: SYSTEM_PROMPT,
      messages: pruneMessages({
        messages: inlineDataUrls(await convertToModelMessages(this.messages)),
        toolCalls: "before-last-2-messages"
      }),
      tools: {
        vaultStarterKit: tool({
          description:
            "Return the recommended PARA folder structure + next step for initializing a vault OS. Use when the user asks to initialize the vault.",
          inputSchema: z.object({}),
          execute: async () => ({
            markdown: vaultStarterKitMarkdown(date)
          })
        }),
        rawCapture: tool({
          description:
            "Create a raw capture note (do not over-organize). Use this first when the user pastes messy inputs.",
          inputSchema: z.object({
            title: z.string().describe("Short title for the capture"),
            source: z.string().optional().describe("Where it came from"),
            content: z.string().describe("The raw content to preserve"),
            created: z.string().optional().describe("YYYY-MM-DD; defaults to today")
          }),
          execute: async ({ title, source, content, created }) => ({
            markdown: rawCaptureMarkdown({
              title,
              source,
              content,
              date: created ?? date
            })
          })
        }),
        wikiNoteDraft: tool({
          description:
            "Draft a wiki-ready note from processed material, including summary, key points, connections, and open questions.",
          inputSchema: z.object({
            title: z.string(),
            summary: z.string().describe("1–3 sentence summary"),
            keyPoints: z.array(z.string()).default([]),
            practicalRelevance: z.string().describe("Why this matters / how to use it"),
            created: z.string().optional().describe("YYYY-MM-DD; defaults to today")
          }),
          execute: async ({
            title,
            summary,
            keyPoints,
            practicalRelevance,
            created
          }) => ({
            markdown: wikiNoteMarkdown({
              title,
              summary,
              practicalRelevance,
              keyPoints,
              date: created ?? date
            })
          })
        }),
        dispatchUpdate: tool({
          description:
            "Route a mixed operational update into a dispatch packet with target note families and follow-through. Use when the user pastes a client update, publication update, or combined status change that should land in more than one vault surface.",
          inputSchema: z.object({
            title: z.string().describe("Short title for the update"),
            source: z.string().optional().describe("Where the update came from"),
            content: z.string().describe("The raw update text to preserve"),
            kind: z.enum(["client", "publication", "mixed", "general"]).default("mixed"),
            routes: z.array(z.string()).default([]).describe("Target note paths or route labels"),
            created: z.string().optional().describe("YYYY-MM-DD; defaults to today")
          }),
          execute: async ({ title, source, content, kind, routes, created }) => ({
            markdown: dispatchPacketMarkdown({
              title,
              source,
              content,
              kind,
              routes,
              date: created ?? date
            })
          })
        })
      },
      abortSignal: options?.abortSignal
    });

    return result.toUIMessageStreamResponse();
  }
}

export default {
  async fetch(request: Request, env: Env) {
    return (await routeAgentRequest(request, env)) ?? new Response("Not found", { status: 404 });
  }
} satisfies ExportedHandler<Env>;
