import { createMcpHandler } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

interface Env {
  FIGMA_API_BASE_URL?: string;
  FIGMA_PERSONAL_ACCESS_TOKEN?: string;
  FIGMA_TOKEN?: string;
  FIGMA_ACCESS_TOKEN?: string;
  FIGMA_BEARER_TOKEN?: string;
  FIGMA_AUTH_MODE?: string;
  MAX_FIGMA_RESPONSE_BYTES?: string;
}

type FigmaNode = {
  id?: string;
  name?: string;
  type?: string;
  visible?: boolean;
  children?: FigmaNode[];
  absoluteBoundingBox?: {
    x?: number;
    y?: number;
    width?: number;
    height?: number;
  };
  layoutMode?: string;
  primaryAxisSizingMode?: string;
  counterAxisSizingMode?: string;
  fills?: Array<{
    type?: string;
    visible?: boolean;
    color?: { r?: number; g?: number; b?: number; a?: number };
  }>;
};

type FigmaFileResponse = {
  name?: string;
  role?: string;
  lastModified?: string;
  editorType?: string;
  thumbnailUrl?: string;
  version?: string;
  document?: FigmaNode;
};

type ParsedFigmaUrl = {
  fileKey?: string;
  nodeId?: string;
  mode?: string;
  fileName?: string;
  originalUrl: string;
};

const fileLocatorSchema = {
  key: z.string().optional().describe("Figma file key. Optional if url is provided."),
  url: z.string().optional().describe("Full Figma file or node URL. Optional if key is provided.")
};

const maxBytesSchema = z
  .number()
  .int()
  .min(1000)
  .max(500000)
  .optional()
  .describe("Maximum characters returned in the MCP text response. Defaults to 80000.");

function textResult(text: string) {
  return { content: [{ type: "text" as const, text }] };
}

function jsonResult(data: unknown, maxChars = 80000) {
  const text = JSON.stringify(data, null, 2);
  if (text.length <= maxChars) {
    return textResult(text);
  }

  return textResult(
    JSON.stringify(
      {
        truncated: true,
        maxChars,
        note: "The Figma response was larger than the requested limit. Re-run with narrower ids/depth or a larger maxBytes value.",
        preview: text.slice(0, maxChars)
      },
      null,
      2
    )
  );
}

function getMaxChars(env: Env, override?: number): number {
  if (override) return override;
  const parsed = Number.parseInt(env.MAX_FIGMA_RESPONSE_BYTES ?? "", 10);
  return Number.isFinite(parsed) && parsed > 0 ? parsed : 80000;
}

function normalizeNodeId(id: string): string {
  return decodeURIComponent(id).trim().replace(/-/g, ":");
}

function parseFigmaUrl(url: string): ParsedFigmaUrl {
  const parsed = new URL(url);
  const match = parsed.pathname.match(
    /^\/(file|design|proto|figjam|slides)\/([^/?#]+)(?:\/([^?#]+))?/i
  );
  const rawNodeId = parsed.searchParams.get("node-id") ?? parsed.searchParams.get("node_id");

  return {
    fileKey: match?.[2],
    mode: match?.[1],
    fileName: match?.[3] ? decodeURIComponent(match[3]) : undefined,
    nodeId: rawNodeId ? normalizeNodeId(rawNodeId) : undefined,
    originalUrl: url
  };
}

function resolveFileKey(input: { key?: string; url?: string }): string {
  if (input.key?.trim()) return input.key.trim();
  if (input.url?.trim()) {
    const parsed = parseFigmaUrl(input.url.trim());
    if (parsed.fileKey) return parsed.fileKey;
  }
  throw new Error("Provide either a Figma file key or a Figma URL.");
}

function resolveNodeIds(input: { ids?: string[]; nodeUrl?: string }): string[] {
  const ids = (input.ids ?? []).map(normalizeNodeId).filter(Boolean);
  if (input.nodeUrl?.trim()) {
    const parsed = parseFigmaUrl(input.nodeUrl.trim());
    if (parsed.nodeId) ids.push(parsed.nodeId);
  }
  return [...new Set(ids)];
}

function figmaBaseUrl(env: Env): string {
  return (env.FIGMA_API_BASE_URL ?? "https://api.figma.com").replace(/\/+$/, "");
}

function figmaAuthHeaders(env: Env): HeadersInit {
  const personalToken =
    env.FIGMA_PERSONAL_ACCESS_TOKEN ?? env.FIGMA_TOKEN ?? env.FIGMA_ACCESS_TOKEN;
  const bearerToken = env.FIGMA_BEARER_TOKEN ?? env.FIGMA_ACCESS_TOKEN;
  const useBearer = env.FIGMA_AUTH_MODE?.toLowerCase() === "bearer" || !!env.FIGMA_BEARER_TOKEN;

  if (useBearer && bearerToken) {
    return { Authorization: `Bearer ${bearerToken}` };
  }

  if (personalToken) {
    return { "X-Figma-Token": personalToken };
  }

  throw new Error(
    "Figma token is not configured. Set FIGMA_PERSONAL_ACCESS_TOKEN as a Worker secret or in local .dev.vars."
  );
}

function appendQuery(url: URL, params: Record<string, string | number | boolean | undefined>) {
  for (const [key, value] of Object.entries(params)) {
    if (value === undefined || value === "") continue;
    url.searchParams.set(key, String(value));
  }
}

async function figmaGet<T>(
  env: Env,
  path: string,
  params: Record<string, string | number | boolean | undefined> = {}
): Promise<T> {
  const url = new URL(`${figmaBaseUrl(env)}${path}`);
  appendQuery(url, params);

  const response = await fetch(url, {
    headers: {
      Accept: "application/json",
      ...figmaAuthHeaders(env)
    }
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(
      `Figma API ${response.status} ${response.statusText}: ${body.slice(0, 1200)}`
    );
  }

  return (await response.json()) as T;
}

function compactColor(color?: { r?: number; g?: number; b?: number; a?: number }) {
  if (!color) return undefined;
  const toByte = (value?: number) => Math.round(Math.max(0, Math.min(1, value ?? 0)) * 255);
  return {
    hex: `#${[toByte(color.r), toByte(color.g), toByte(color.b)]
      .map((value) => value.toString(16).padStart(2, "0"))
      .join("")}`,
    alpha: Number((color.a ?? 1).toFixed(3))
  };
}

function summarizeNode(node: FigmaNode, childLimit: number, depth = 0): unknown {
  const children = Array.isArray(node.children) ? node.children : [];
  const visibleFills = Array.isArray(node.fills)
    ? node.fills
        .filter((fill) => fill.visible !== false)
        .slice(0, 4)
        .map((fill) => ({ type: fill.type, color: compactColor(fill.color) }))
    : undefined;

  return {
    id: node.id,
    name: node.name,
    type: node.type,
    visible: node.visible,
    bounds: node.absoluteBoundingBox
      ? {
          x: node.absoluteBoundingBox.x,
          y: node.absoluteBoundingBox.y,
          width: node.absoluteBoundingBox.width,
          height: node.absoluteBoundingBox.height
        }
      : undefined,
    layout:
      node.layoutMode || node.primaryAxisSizingMode || node.counterAxisSizingMode
        ? {
            mode: node.layoutMode,
            primarySizing: node.primaryAxisSizingMode,
            counterSizing: node.counterAxisSizingMode
          }
        : undefined,
    fills: visibleFills?.length ? visibleFills : undefined,
    children:
      depth >= 3
        ? undefined
        : children.slice(0, childLimit).map((child) => summarizeNode(child, childLimit, depth + 1)),
    omittedChildren: children.length > childLimit ? children.length - childLimit : undefined
  };
}

function createServer(env: Env) {
  const server = new McpServer({
    name: "figma-mcp-server",
    version: "0.1.0"
  });

  server.tool(
    "figma_extract_from_url",
    "Parse a Figma file/node URL into file key, node id, file type, and display slug.",
    { url: z.string().url() },
    async ({ url }) => jsonResult(parseFigmaUrl(url))
  );

  server.tool(
    "figma_get_file_metadata",
    "Fetch Figma file metadata. Requires file_metadata:read scope.",
    { ...fileLocatorSchema, maxBytes: maxBytesSchema },
    async ({ key, url, maxBytes }) => {
      const fileKey = resolveFileKey({ key, url });
      const data = await figmaGet(env, `/v1/files/${encodeURIComponent(fileKey)}/meta`);
      return jsonResult(data, getMaxChars(env, maxBytes));
    }
  );

  server.tool(
    "figma_get_file",
    "Fetch Figma file JSON. Use ids and depth to keep the result bounded. Requires file_content:read scope.",
    {
      ...fileLocatorSchema,
      ids: z.array(z.string()).optional().describe("Optional node ids to retrieve inside the file."),
      depth: z.number().int().min(1).max(10).optional(),
      version: z.string().optional(),
      geometry: z.enum(["paths"]).optional(),
      pluginData: z.string().optional().describe("Comma-separated plugin IDs or shared."),
      branchData: z.boolean().optional(),
      maxBytes: maxBytesSchema
    },
    async ({ key, url, ids, depth, version, geometry, pluginData, branchData, maxBytes }) => {
      const fileKey = resolveFileKey({ key, url });
      const data = await figmaGet(env, `/v1/files/${encodeURIComponent(fileKey)}`, {
        ids: ids?.map(normalizeNodeId).join(","),
        depth,
        version,
        geometry,
        plugin_data: pluginData,
        branch_data: branchData
      });
      return jsonResult(data, getMaxChars(env, maxBytes));
    }
  );

  server.tool(
    "figma_get_nodes",
    "Fetch specific Figma nodes from a file. Pass ids directly or provide nodeUrl. Requires file_content:read scope.",
    {
      ...fileLocatorSchema,
      ids: z.array(z.string()).optional(),
      nodeUrl: z.string().url().optional(),
      depth: z.number().int().min(1).max(10).optional(),
      version: z.string().optional(),
      geometry: z.enum(["paths"]).optional(),
      pluginData: z.string().optional().describe("Comma-separated plugin IDs or shared."),
      maxBytes: maxBytesSchema
    },
    async ({ key, url, ids, nodeUrl, depth, version, geometry, pluginData, maxBytes }) => {
      const fileKey = resolveFileKey({ key, url: url ?? nodeUrl });
      const nodeIds = resolveNodeIds({ ids, nodeUrl });
      if (!nodeIds.length) throw new Error("Provide at least one node id or a Figma node URL.");

      const data = await figmaGet(env, `/v1/files/${encodeURIComponent(fileKey)}/nodes`, {
        ids: nodeIds.join(","),
        depth,
        version,
        geometry,
        plugin_data: pluginData
      });
      return jsonResult(data, getMaxChars(env, maxBytes));
    }
  );

  server.tool(
    "figma_get_image",
    "Get expiring image export URLs for node ids. Use this for screenshots/design references. Requires file_content:read scope.",
    {
      ...fileLocatorSchema,
      ids: z.array(z.string()).optional(),
      nodeUrl: z.string().url().optional(),
      format: z.enum(["jpg", "png", "svg", "pdf"]).default("png"),
      scale: z.number().min(0.01).max(4).optional(),
      svgIncludeId: z.boolean().optional(),
      svgOutlineText: z.boolean().optional(),
      contentsOnly: z.boolean().optional(),
      useAbsoluteBounds: z.boolean().optional(),
      version: z.string().optional(),
      maxBytes: maxBytesSchema
    },
    async ({
      key,
      url,
      ids,
      nodeUrl,
      format,
      scale,
      svgIncludeId,
      svgOutlineText,
      contentsOnly,
      useAbsoluteBounds,
      version,
      maxBytes
    }) => {
      const fileKey = resolveFileKey({ key, url: url ?? nodeUrl });
      const nodeIds = resolveNodeIds({ ids, nodeUrl });
      if (!nodeIds.length) throw new Error("Provide at least one node id or a Figma node URL.");

      const data = await figmaGet(env, `/v1/images/${encodeURIComponent(fileKey)}`, {
        ids: nodeIds.join(","),
        format,
        scale,
        svg_include_id: svgIncludeId,
        svg_outline_text: svgOutlineText,
        contents_only: contentsOnly,
        use_absolute_bounds: useAbsoluteBounds,
        version
      });
      return jsonResult(data, getMaxChars(env, maxBytes));
    }
  );

  server.tool(
    "figma_get_image_fills",
    "Get expiring URLs for all image fills in a Figma file. Requires file_content:read scope.",
    { ...fileLocatorSchema, maxBytes: maxBytesSchema },
    async ({ key, url, maxBytes }) => {
      const fileKey = resolveFileKey({ key, url });
      const data = await figmaGet(env, `/v1/files/${encodeURIComponent(fileKey)}/images`);
      return jsonResult(data, getMaxChars(env, maxBytes));
    }
  );

  server.tool(
    "figma_summarize_file",
    "Fetch a bounded Figma file tree and return compact design context: metadata, pages, frames, bounds, layouts, and visible fills.",
    {
      ...fileLocatorSchema,
      depth: z.number().int().min(1).max(5).default(3),
      childLimit: z.number().int().min(1).max(50).default(12),
      maxBytes: maxBytesSchema
    },
    async ({ key, url, depth, childLimit, maxBytes }) => {
      const fileKey = resolveFileKey({ key, url });
      const data = await figmaGet<FigmaFileResponse>(env, `/v1/files/${encodeURIComponent(fileKey)}`, {
        depth
      });

      const pages = Array.isArray(data.document?.children) ? data.document.children : [];
      return jsonResult(
        {
          fileKey,
          name: data.name,
          role: data.role,
          lastModified: data.lastModified,
          editorType: data.editorType,
          version: data.version,
          thumbnailUrl: data.thumbnailUrl,
          pageCount: pages.length,
          pages: pages.map((page) => summarizeNode(page, childLimit))
        },
        getMaxChars(env, maxBytes)
      );
    }
  );

  return server;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/" || url.pathname === "/health") {
      return Response.json({
        ok: true,
        service: "figma-mcp-server",
        mcp: "/mcp",
        tools: [
          "figma_extract_from_url",
          "figma_get_file_metadata",
          "figma_get_file",
          "figma_get_nodes",
          "figma_get_image",
          "figma_get_image_fills",
          "figma_summarize_file"
        ]
      });
    }

    const server = createServer(env);
    return createMcpHandler(server, { route: "/mcp" })(request, env, ctx);
  }
} satisfies ExportedHandler<Env>;
