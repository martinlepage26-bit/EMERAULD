import type {
  InboundMessage,
  MetricsSnapshot,
  PlatformAdapter,
  PublishInput,
  PublishResult,
  ReplyInput,
} from './types';

/**
 * Stands in for a live platform when DRY_RUN is on.
 *
 * This exists so the full pipeline (plan, draft, publish, measure, rebalance)
 * can be exercised before a single creator has connected an account. Metrics are
 * drawn from a plausible distribution rather than returned as zeros, because a
 * growth engine fed constant zeros never demonstrates that it reweights.
 */
export class SimulatedAdapter implements PlatformAdapter {
  constructor(readonly platform: string) {}

  async publish(input: PublishInput): Promise<PublishResult> {
    const id = `sim_${this.platform}_${Date.now()}_${Math.floor(Math.random() * 1e6)}`;
    console.log(`[dry-run] ${this.platform} publish (${input.body.length} chars)`);
    return { externalPostId: id, url: `https://example.invalid/${this.platform}/${id}` };
  }

  async fetchInbound(_accessToken: string, _since: string): Promise<InboundMessage[]> {
    return [];
  }

  async fetchMetrics(_accessToken: string, externalPostId: string): Promise<MetricsSnapshot> {
    // Seeded from the post id so repeated collections for one post trend rather
    // than jump around, which is what the growth engine expects to see.
    const seed = [...externalPostId].reduce((a, c) => (a * 31 + c.charCodeAt(0)) >>> 0, 7);
    const rand = (n: number, spread: number) => Math.floor(n * (0.5 + ((seed % spread) / spread)));

    const impressions = rand(4000, 97);
    return {
      impressions,
      likes: Math.floor(impressions * 0.021),
      comments: Math.floor(impressions * 0.004),
      shares: Math.floor(impressions * 0.002),
      saves: Math.floor(impressions * 0.003),
      clicks: Math.floor(impressions * 0.011),
      follows: Math.floor(impressions * 0.0009),
    };
  }

  async sendReply(input: ReplyInput): Promise<{ externalId: string }> {
    console.log(`[dry-run] ${this.platform} reply to ${input.threadId}`);
    return { externalId: `sim_reply_${Date.now()}` };
  }
}
