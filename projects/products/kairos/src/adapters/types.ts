export interface PublishInput {
  body: string;
  mediaUrls: string[];
  accessToken: string;
  externalAccountId: string | null;
}

export interface PublishResult {
  externalPostId: string;
  url: string;
}

export interface InboundMessage {
  threadId: string;
  externalId: string;
  authorHandle: string;
  body: string;
  createdAt: string;
}

export interface MetricsSnapshot {
  impressions: number;
  likes: number;
  comments: number;
  shares: number;
  saves: number;
  clicks: number;
  follows: number;
}

export interface ReplyInput {
  threadId: string;
  body: string;
  accessToken: string;
}

export interface PlatformAdapter {
  readonly platform: string;
  publish(input: PublishInput): Promise<PublishResult>;
  fetchInbound(accessToken: string, since: string): Promise<InboundMessage[]>;
  fetchMetrics(accessToken: string, externalPostId: string): Promise<MetricsSnapshot>;
  sendReply(input: ReplyInput): Promise<{ externalId: string }>;
}

export const EMPTY_METRICS: MetricsSnapshot = {
  impressions: 0,
  likes: 0,
  comments: 0,
  shares: 0,
  saves: 0,
  clicks: 0,
  follows: 0,
};
