"use client";

import { useEffect, useState } from "react";
import { format, addDays } from "date-fns";

export default function CalendarPage() {
  const [data, setData] = useState<any>(null);
  
  useEffect(() => {
    const key = localStorage.getItem("kairos_api_key");
    if (key) {
      fetch("https://kairos.govern-ai.ca/v1/calendar", {
        headers: { Authorization: `Bearer ${key}` }
      })
      .then(r => r.json())
      .then(setData)
      .catch(console.error);
    }
  }, []);

  const today = new Date();
  const days = Array.from({ length: 14 }).map((_, i) => addDays(today, i));

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Content Calendar (14 Days)</h1>
      <p className="text-gray-500 mb-8">The system automatically plans your content across pillars based on measured performance.</p>

      <div className="grid grid-cols-7 gap-4">
        {days.map((day, i) => (
          <div key={i} className="bg-white border rounded-xl p-4 min-h-[120px]">
            <div className="text-sm font-medium text-gray-400 mb-2">{format(day, "MMM d")}</div>
            {/* We would render slots here based on data */}
            {i % 3 === 0 && <div className="mt-2 text-xs bg-blue-50 text-blue-700 border border-blue-200 px-2 py-1 rounded">Planned Post</div>}
          </div>
        ))}
      </div>
    </div>
  );
}
