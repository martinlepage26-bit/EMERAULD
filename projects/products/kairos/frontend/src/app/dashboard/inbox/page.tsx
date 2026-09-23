"use client";

import { useEffect, useState } from "react";
import { MessageSquare, Check, X } from "lucide-react";

export default function InboxPage() {
  const [data, setData] = useState<any>(null);
  
  useEffect(() => {
    const key = localStorage.getItem("kairos_api_key");
    if (key) {
      fetch("https://kairos.govern-ai.ca/v1/inbox", {
        headers: { Authorization: `Bearer ${key}` }
      })
      .then(r => r.json())
      .then(setData)
      .catch(console.error);
    }
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Inbox Triage</h1>
      <p className="text-gray-500 mb-8">Inbound messages are triaged by intent, with replies auto-drafted by the system.</p>

      <div className="bg-white border rounded-2xl shadow-sm divide-y">
        {data?.messages?.length > 0 ? (
          data.messages.map((msg: any) => (
            <div key={msg.id} className="p-6">Message rendering...</div>
          ))
        ) : (
          <div className="p-12 text-center text-gray-500 flex flex-col items-center">
            <MessageSquare className="w-8 h-8 mb-4 text-gray-300" />
            <p>Inbox zero. All messages triaged and answered.</p>
          </div>
        )}
      </div>
    </div>
  );
}
