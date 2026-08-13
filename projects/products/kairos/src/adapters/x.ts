import { httpJson } from './http';
import {
  EMPTY_METRICS,
  type InboundMessage,
  type MetricsSnapshot,
  type PlatformAdapter,
  type PublishInput,
  type PublishResult,
  type ReplyInput,
} from './types';

const API = 'https://api.x.com/2';

interface CreateTweetResponse {
  data: { id: string; text: string };
}

interface TweetMetricsResponse {
  data?: Array<{
    id: string;
    public_metrics?: {
      impression_count?: number;
      like_count?: number;
      reply_count?: number;
      retweet_count?: number;
      bookmark_count?: number;
    };
    non_public_metrics?: { url_link_clicks?: number; user_profile_clicks?: number };
  }>;
}

interface MentionsResponse {
  data?: Array<{
    id: string;
    text: string;
    author_id: string;
    conversation_id: string;
    created_at: string;
  }>;
  includes?: { users?: Array<{ id: string; username: string }> };
}

export class XAdapter implements PlatformAdapter {
  readonly platform = 'x';

  async publish(input: PublishInput): Promise<PublishResult> {
    const res = await httpJson<CreateTweetResponse>(`${API}/tweets`, {
      method: 'POST',
      token: input.accessToken,
      body: { text: input.body },
    });
    return {
      externalPostId: res.data.id,
      url: `https://x.com/i/status/${res.data.id}`,
    };
  }

  async fetchInbound(accessToken: string, since: string): Promise<InboundMessage[]> {
    const params = new URLSearchParams({
      'tweet.fields': 'created_at,conversation_id,author_id',
      expansions: 'author_id',
      start_time: since,
      max_results: '100',
    });
    const res = await httpJson<MentionsResponse>(
      `${API}/users/me/mentions?${params.toString()}`,
      { token: accessToken },
    );

    const handles = new Map(
      (res.includes?.users ?? []).map((u) => [u.id, u.username] as const),
    );

    return (res.data ?? []).map((t) => ({
      threadId: t.conversation_id,
      externalId: t.id,
      authorHandle: handles.get(t.author_id) ?? t.author_id,
      body: t.text,
      createdAt: t.created_at,
    }));
  }

  async fetchMetrics(accessToken: string, externalPostId: string): Promise<MetricsSnapshot> {
    const params = new URLSearchParams({
      ids: externalPostId,
      'tweet.fields': 'public_metrics,non_public_metrics',
    });
    const res = await httpJson<TweetMetricsResponse>(`${API}/tweets?${params.toString()}`, {
      token: accessToken,
    });

    const tweet = res.data?.[0];
    if (!tweet) return EMPTY_METRICS;

    const pub = tweet.public_metrics ?? {};
    return {
      impressions: pub.impression_count ?? 0,
      likes: pub.like_count ?? 0,
      comments: pub.reply_count ?? 0,
      shares: pub.retweet_count ?? 0,
      saves: pub.bookmark_count ?? 0,
      clicks: tweet.non_public_metrics?.url_link_clicks ?? 0,
      // X does not expose per-post follower attribution, so this stays zero
      // rather than being estimated. The growth engine weights it at zero too.
      follows: 0,
    };
  }

  async sendReply(input: ReplyInput): Promise<{ externalId: string }> {
    const res = await httpJson<CreateTweetResponse>(`${API}/tweets`, {
      method: 'POST',
      token: input.accessToken,
      body: { text: input.body, reply: { in_reply_to_tweet_id: input.threadId } },
    });
    return { externalId: res.data.id };
  }
}
