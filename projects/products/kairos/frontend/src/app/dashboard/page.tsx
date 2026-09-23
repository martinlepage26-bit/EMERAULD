"use client";

import { useEffect, useState } from "react";
import { Play, Pause } from "lucide-react";

export default function DashboardOverview() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  // The layout gates on a verified key before this mounts, so the key is present.
  useEffect(() => {
    const key = localStorage.getItem("kairos_api_key");
    if (key) {
      fetchData(key);
    } else {
      setLoading(false);
    }
  }, []);

  const fetchData = async (key: string) => {
    setLoading(true);
    try {
      const res = await fetch("https://kairos.govern-ai.ca/v1/me", {
        headers: { Authorization: `Bearer ${key}` }
      });
      if (res.ok) {
        setData(await res.json());
      }
    } catch (e) {
      console.error(e);
    }
    setLoading(false);
  };

  if (loading) return <div>Loading your digital affairs...</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Overview</h1>
        {data?.controls?.autopilot ? (
          <span className="flex items-center gap-2 text-green-600 bg-green-50 px-3 py-1 rounded-full text-sm font-medium border border-green-200">
            <Play className="w-4 h-4" /> Autopilot Active
          </span>
        ) : (
          <span className="flex items-center gap-2 text-amber-600 bg-amber-50 px-3 py-1 rounded-full text-sm font-medium border border-amber-200">
            <Pause className="w-4 h-4" /> Autopilot Paused
          </span>
        )}
      </div>

      <div className="grid grid-cols-3 gap-6 mb-8">
        <StatCard title="Connected Channels" value={data?.channels?.length || 0} />
        <StatCard title="Plan" value={data?.account?.plan_id || "—"} />
        <StatCard title="Account Status" value={data?.account?.status || "Active"} />
      </div>

      <div className="bg-white p-6 rounded-2xl border shadow-sm mb-8">
        <h2 className="text-xl font-bold mb-4">System State</h2>
        <p className="text-gray-600 mb-4">Kairos runs five background loops on your behalf. Each one checks your stop condition, daily caps, and pause window before it acts.</p>
        <ul className="space-y-3 text-sm">
          <li className="flex justify-between p-3 bg-gray-50 rounded-lg">
            <span className="font-medium">Content Planning</span>
            <span className="text-gray-500">Checking daily at 05:10 UTC</span>
          </li>
          <li className="flex justify-between p-3 bg-gray-50 rounded-lg">
            <span className="font-medium">Auto-Drafting</span>
            <span className="text-gray-500">Processing job queue continuously</span>
          </li>
          <li className="flex justify-between p-3 bg-gray-50 rounded-lg">
            <span className="font-medium">Publish Dispatch</span>
            <span className="text-gray-500">Sweeping every 15 minutes</span>
          </li>
          <li className="flex justify-between p-3 bg-gray-50 rounded-lg">
            <span className="font-medium">Inbox Triage</span>
            <span className="text-gray-500">Sweeping every 15 minutes</span>
          </li>
          <li className="flex justify-between p-3 bg-gray-50 rounded-lg">
            <span className="font-medium">Growth Compounding</span>
            <span className="text-gray-500">Metrics collection at xx:17</span>
          </li>
        </ul>
      </div>
    </div>
  );
}

function StatCard({ title, value }: { title: string; value: string | number }) {
  return (
    <div className="bg-white p-6 rounded-2xl border shadow-sm">
      <h3 className="text-sm font-medium text-gray-500 mb-1">{title}</h3>
      <div className="text-2xl font-bold">{value}</div>
    </div>
  );
}
