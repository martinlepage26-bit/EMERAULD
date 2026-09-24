"use client";

import { useEffect, useState } from "react";
import { Play, Pause } from "lucide-react";
import { authedFetch } from "@/lib/api";
import { LoadError, Loading } from "@/components/LoadState";

interface Me {
  account: {
    id: string;
    email: string;
    display_name: string;
    plan: string;
    status: string;
    trial_ends_at: string | null;
  };
  plan: { name: string; channels: number; postsPerMonth: number; repliesPerMonth: number };
  controls: {
    autopilot_publishing: number;
    autopilot_replies: number;
    paused_until: string | null;
    daily_publish_cap: number;
    daily_reply_cap: number;
  };
  channels: Array<{ id: string; platform: string; handle: string; status: string }>;
}

const LOOPS = [
  ["Planning", "Checking daily at 05:10 UTC"],
  ["Drafting", "Processing job queue continuously"],
  ["Publishing", "Sweeping every 15 minutes"],
  ["Inbox", "Sweeping every 15 minutes"],
  ["Learning what works", "Metrics collection at xx:17"],
];

export default function DashboardOverview() {
  const [data, setData] = useState<Me | null>(null);
  const [error, setError] = useState<Error | null>(null);

  // The layout gates on a verified key before this mounts.
  useEffect(() => {
    authedFetch<Me>("/v1/me").then(setData).catch(setError);
  }, []);

  if (error) {
    return (
      <div>
        <h1 className="text-3xl font-bold mb-8">Overview</h1>
        <LoadError error={error} />
      </div>
    );
  }

  if (!data) {
    return (
      <div>
        <h1 className="text-3xl font-bold mb-8">Overview</h1>
        <Loading />
      </div>
    );
  }

  const paused = data.controls.paused_until
    ? new Date(data.controls.paused_until) > new Date()
    : false;
  // Autopilot is per-loop in the data model; the badge reports the union, so
  // "Active" never overstates a creator who enabled only one of the two.
  const publishing = data.controls.autopilot_publishing === 1;
  const replies = data.controls.autopilot_replies === 1;
  const anyOn = publishing || replies;

  return (
    <div>
      <div className="flex flex-wrap gap-3 justify-between items-center mb-8">
        <h1 className="text-2xl sm:text-3xl font-bold">Overview</h1>
        {anyOn && !paused ? (
          <span className="flex items-center gap-2 text-green-600 bg-green-50 px-3 py-1 rounded-full text-sm font-medium border border-green-200">
            <Play className="w-4 h-4" />
            Autopilot: {publishing && replies ? "publishing + replies" : publishing ? "publishing" : "replies"}
          </span>
        ) : (
          <span className="flex items-center gap-2 text-amber-600 bg-amber-50 px-3 py-1 rounded-full text-sm font-medium border border-amber-200">
            <Pause className="w-4 h-4" /> {paused ? "Paused" : "Autopilot off"}
          </span>
        )}
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6 mb-8">
        <StatCard
          title="Connected Channels"
          value={`${data.channels.length} / ${data.plan.channels}`}
        />
        <StatCard title="Plan" value={data.plan.name} />
        <StatCard title="Account Status" value={data.account.status} />
      </div>

      {data.account.plan === "trial" && data.account.trial_ends_at && (
        <div className="bg-blue-50 border border-blue-200 text-blue-900 rounded-2xl p-4 mb-8 text-sm">
          Trial runs to {new Date(data.account.trial_ends_at).toLocaleDateString()}.
        </div>
      )}

      <div className="bg-white p-6 rounded-2xl border shadow-sm mb-8">
        <h2 className="text-xl font-bold mb-4">What Kairos is doing</h2>
        <p className="text-gray-600 mb-4">
          Kairos runs five background loops on your behalf. Each one checks your stop condition,
          daily caps ({data.controls.daily_publish_cap} posts, {data.controls.daily_reply_cap}{" "}
          replies), and pause window before it acts.
        </p>
        <ul className="space-y-3 text-sm">
          {LOOPS.map(([name, cadence]) => (
            <li key={name} className="flex justify-between p-3 bg-gray-50 rounded-lg">
              <span className="font-medium">{name}</span>
              <span className="text-gray-500">{cadence}</span>
            </li>
          ))}
        </ul>
      </div>

      {data.channels.length > 0 && (
        <div className="bg-white p-6 rounded-2xl border shadow-sm">
          <h2 className="text-xl font-bold mb-4">Channels</h2>
          <ul className="divide-y">
            {data.channels.map((ch) => (
              <li key={ch.id} className="flex justify-between py-3 text-sm">
                <span className="font-medium">
                  {ch.handle} <span className="text-gray-400">· {ch.platform}</span>
                </span>
                <span className="text-gray-500 capitalize">{ch.status}</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

function StatCard({ title, value }: { title: string; value: string | number }) {
  return (
    <div className="bg-white p-6 rounded-2xl border shadow-sm">
      <h3 className="text-sm font-medium text-gray-500 mb-1">{title}</h3>
      <div className="text-2xl font-bold capitalize">{value}</div>
    </div>
  );
}
