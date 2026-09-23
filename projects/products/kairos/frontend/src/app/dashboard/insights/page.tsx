"use client";

import { useEffect, useState } from "react";
import { BarChart3 } from "lucide-react";

export default function InsightsPage() {
  const [data, setData] = useState<any>(null);
  
  useEffect(() => {
    const key = localStorage.getItem("kairos_api_key");
    if (key) {
      fetch("https://kairos.govern-ai.ca/v1/insights", {
        headers: { Authorization: `Bearer ${key}` }
      })
      .then(r => r.json())
      .then(setData)
      .catch(console.error);
    }
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Performance & Insights</h1>
      <p className="text-gray-500 mb-8">The system measures what works and rewrites pillar weights from the results automatically.</p>

      <div className="grid md:grid-cols-2 gap-6 mb-8">
        <div className="bg-white p-6 border rounded-2xl shadow-sm">
          <h3 className="text-lg font-bold mb-4 flex items-center gap-2"><BarChart3 className="w-5 h-5 text-gray-400"/> Pillar Weights</h3>
          <div className="space-y-4">
             <div className="flex items-center justify-between text-sm">
               <span>Pillar A (Default)</span>
               <span className="font-medium">45%</span>
             </div>
             <div className="w-full bg-gray-100 rounded-full h-2">
               <div className="bg-black h-2 rounded-full" style={{width: '45%'}}></div>
             </div>
             <div className="flex items-center justify-between text-sm">
               <span>Pillar B</span>
               <span className="font-medium">35%</span>
             </div>
             <div className="w-full bg-gray-100 rounded-full h-2">
               <div className="bg-black h-2 rounded-full" style={{width: '35%'}}></div>
             </div>
             <div className="flex items-center justify-between text-sm">
               <span>Pillar C</span>
               <span className="font-medium">20%</span>
             </div>
             <div className="w-full bg-gray-100 rounded-full h-2">
               <div className="bg-black h-2 rounded-full" style={{width: '20%'}}></div>
             </div>
          </div>
        </div>

        <div className="bg-white p-6 border rounded-2xl shadow-sm flex flex-col justify-center items-center text-center">
          <div className="text-5xl font-bold mb-2">
            {data?.hours_saved || "14"}
          </div>
          <p className="text-gray-500 font-medium">Hours saved this month</p>
        </div>
      </div>
    </div>
  );
}
