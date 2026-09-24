"use client";

import { useEffect, useState } from "react";
import { MessageSquare } from "lucide-react";
import { formatDistanceToNow, parseISO } from "date-fns";
import { authedFetch } from "@/lib/api";
import { EmptyState, LoadError, Loading } from "@/components/LoadState";

interface Conversation {
  id: string;
  author_handle: string;
  intent: string | null;
  priority: number;
  status: string;
  last_message_at: string;
  platform: string;
  latest_message: string | null;
  pending_draft_id: string | null;
}

const PRIORITY_LABEL: Record<number, { label: string; className: string }> = {
  1: { label: "High", className: "bg-red-50 text-red-700 border-red-200" },
  2: { label: "Normal", className: "bg-amber-50 text-amber-700 border-amber-200" },
  3: { label: "Low", className: "bg-gray-50 text-gray-600 border-gray-200" },
};

export default function InboxPage() {
  const [conversations, setConversations] = useState<Conversation[] | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [acting, setActing] = useState<string | null>(null);

  useEffect(() => {
    authedFetch<{ conversations: Conversation[] }>("/v1/inbox")
      .then((r) => setConversations(r.conversations ?? []))
      .catch(setError);
  }, []);

  const act = async (conversationId: string, draftId: string, action: "approve" | "reject") => {
    setActing(draftId);
    try {
      await authedFetch(`/v1/replies/${draftId}/${action}`, { method: "POST" });
      setConversations((current) =>
        (current ?? []).map((c) =>
          c.id === conversationId ? { ...c, pending_draft_id: null, status: "answered" } : c,
        ),
      );
    } catch (err) {
      setError(err as Error);
    }
    setActing(null);
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Inbox</h1>
      <p className="text-gray-500 mb-8">
        Replies to your posts and messages, sorted by what the person wants, with a reply drafted for
        you. Routine answers can go out on their own if you allow it; leads and complaints always wait for you.
      </p>

      {error ? (
        <LoadError error={error} />
      ) : conversations === null ? (
        <Loading />
      ) : conversations.length === 0 ? (
        <EmptyState icon={<MessageSquare className="w-8 h-8" />}>
          You&apos;re all caught up. New messages are checked every 15 minutes.
        </EmptyState>
      ) : (
        <div className="bg-white border rounded-2xl shadow-sm divide-y">
          {conversations.map((conv) => {
            const priority = PRIORITY_LABEL[conv.priority] ?? PRIORITY_LABEL[3];
            return (
              <div key={conv.id} className="p-6">
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-3">
                    <span className="font-medium">{conv.author_handle}</span>
                    <span className="text-xs text-gray-400">{conv.platform}</span>
                    {conv.intent && (
                      <span className="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded capitalize">
                        {conv.intent}
                      </span>
                    )}
                  </div>
                  <div className="flex items-center gap-3">
                    <span className={`text-xs border px-2 py-0.5 rounded ${priority?.className}`}>
                      {priority?.label}
                    </span>
                    <span className="text-xs text-gray-400">
                      {formatDistanceToNow(parseISO(conv.last_message_at), { addSuffix: true })}
                    </span>
                  </div>
                </div>

                {conv.latest_message && (
                  <p className="text-gray-700 mb-4 whitespace-pre-wrap">{conv.latest_message}</p>
                )}

                {conv.pending_draft_id ? (
                  <div className="flex gap-3">
                    <button
                      disabled={acting === conv.pending_draft_id}
                      onClick={() => act(conv.id, conv.pending_draft_id as string, "approve")}
                      className="bg-black text-white px-4 py-2 rounded-lg text-sm font-medium disabled:opacity-40"
                    >
                      Send reply
                    </button>
                    <button
                      disabled={acting === conv.pending_draft_id}
                      onClick={() => act(conv.id, conv.pending_draft_id as string, "reject")}
                      className="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium disabled:opacity-40"
                    >
                      Discard draft
                    </button>
                  </div>
                ) : (
                  <p className="text-xs text-gray-400 capitalize">{conv.status}</p>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
