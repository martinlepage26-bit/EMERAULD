"use client";

import { useEffect, useState } from "react";
import { BarChart3 } from "lucide-react";
import { authedFetch } from "@/lib/api";
import { LoadError, Loading } from "@/components/LoadState";

interface Pillar {
  name: string;
  weight: number;
  posts: number;
  avg_score: number | null;
}

interface Insights {
  window: string;
  totals: { posts: number; impressions: number; engagements: number; follows: number };
  pillars: Pillar[];
  usage: {
    postsPublished: number;
    repliesSent: number;
    planLimits: { name: string; postsPerMonth: number; repliesPerMonth: number };
  };
  hoursSaved: { hours: number; basis: Record<string, number> };
}

export default function InsightsPage() {
  const [data, setData] = useState<Insights | null>(null);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    authedFetch<Insights>("/v1/insights").then(setData).catch(setError);
  }, []);

  if (error) {
    return (
      <div>
        <h1 className="text-3xl font-bold mb-8">Performance &amp; Insights</h1>
        <LoadError error={error} />
      </div>
    );
  }

  if (!data) {
    return (
      <div>
        <h1 className="text-3xl font-bold mb-8">Performance &amp; Insights</h1>
        <Loading />
      </div>
    );
  }

  // Weights are stored unnormalized, so the bars are drawn relative to their sum.
  const weightTotal = data.pillars.reduce((sum, p) => sum + (p.weight || 0), 0);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-2">Performance &amp; Insights</h1>
      <p className="text-gray-500 mb-8">
        Measured over the last {data.window}. Kairos shifts effort toward topics that perform
        automatically.
      </p>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
        <Stat label="Posts published" value={data.totals.posts} />
        <Stat label="Impressions" value={data.totals.impressions.toLocaleString()} />
        <Stat label="Engagements" value={data.totals.engagements.toLocaleString()} />
        <Stat label="New follows" value={data.totals.follows.toLocaleString()} />
      </div>

      <div className="grid md:grid-cols-2 gap-6 mb-8">
        <div className="bg-white p-6 border rounded-2xl shadow-sm">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
            <BarChart3 className="w-5 h-5 text-gray-400" /> Topics
          </h3>

          {data.pillars.length === 0 ? (
            <p className="text-sm text-gray-500">No topics set up yet.</p>
          ) : (
            <div className="space-y-4">
              {data.pillars.map((pillar) => {
                const share = weightTotal > 0 ? Math.round((pillar.weight / weightTotal) * 100) : 0;
                return (
                  <div key={pillar.name}>
                    <div className="flex items-center justify-between text-sm mb-1">
                      <span>{pillar.name}</span>
                      <span className="font-medium">{share}%</span>
                    </div>
                    <div className="w-full bg-gray-100 rounded-full h-2">
                      <div className="bg-black h-2 rounded-full" style={{ width: `${share}%` }} />
                    </div>
                    <div className="text-xs text-gray-400 mt-1">
                      {pillar.posts} posts
                      {pillar.avg_score !== null && ` · avg score ${pillar.avg_score}`}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        <div className="bg-white p-6 border rounded-2xl shadow-sm flex flex-col justify-center items-center text-center">
          <div className="text-5xl font-bold mb-2">{data.hoursSaved.hours}</div>
          <p className="text-gray-500 font-medium mb-4">Hours saved this month</p>
          <dl className="text-xs text-gray-400 space-y-0.5">
            {Object.entries(data.hoursSaved.basis).map(([label, minutes]) => (
              <div key={label} className="flex gap-2 justify-center">
                <dt className="capitalize">{label.replace(/([A-Z])/g, " $1").toLowerCase()}:</dt>
                <dd>{minutes}</dd>
              </div>
            ))}
          </dl>
        </div>
      </div>

      <div className="bg-white p-6 border rounded-2xl shadow-sm">
        <h3 className="text-lg font-bold mb-4">Plan usage</h3>
        <div className="space-y-4">
          <Usage
            label="Posts published"
            used={data.usage.postsPublished}
            limit={data.usage.planLimits.postsPerMonth}
          />
          <Usage
            label="Replies sent"
            used={data.usage.repliesSent}
            limit={data.usage.planLimits.repliesPerMonth}
          />
        </div>
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string | number }) {
  return (
    <div className="bg-white p-6 rounded-2xl border shadow-sm">
      <h3 className="text-sm font-medium text-gray-500 mb-1">{label}</h3>
      <div className="text-2xl font-bold">{value}</div>
    </div>
  );
}

function Usage({ label, used, limit }: { label: string; used: number; limit: number }) {
  const pct = limit > 0 ? Math.min(100, Math.round((used / limit) * 100)) : 0;
  return (
    <div>
      <div className="flex items-center justify-between text-sm mb-1">
        <span>{label}</span>
        <span className="font-medium">
          {used} / {limit}
        </span>
      </div>
      <div className="w-full bg-gray-100 rounded-full h-2">
        <div
          className={`h-2 rounded-full ${pct >= 90 ? "bg-red-500" : "bg-black"}`}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}
