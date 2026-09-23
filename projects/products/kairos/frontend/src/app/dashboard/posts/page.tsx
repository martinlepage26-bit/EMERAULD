"use client";

import { useEffect, useState } from "react";
import { FileText, CheckCircle2, Clock } from "lucide-react";

export default function PostsPage() {
  const [data, setData] = useState<any>(null);
  
  useEffect(() => {
    const key = localStorage.getItem("kairos_api_key");
    if (key) {
      fetch("https://kairos.govern-ai.ca/v1/posts", {
        headers: { Authorization: `Bearer ${key}` }
      })
      .then(r => r.json())
      .then(setData)
      .catch(console.error);
    }
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Posts & Drafts</h1>
      
      <div className="flex gap-4 border-b mb-8">
        <button className="pb-2 border-b-2 border-black font-medium">Pending Review</button>
        <button className="pb-2 text-gray-500 hover:text-black">Published History</button>
      </div>

      <div className="space-y-4">
        {data?.posts?.length > 0 ? (
          data.posts.map((post: any) => (
            <div key={post.id} className="bg-white p-6 border rounded-2xl shadow-sm">
              <div className="flex justify-between mb-4">
                <span className="text-sm font-medium text-blue-600 bg-blue-50 px-2 py-1 rounded">Draft</span>
              </div>
              <p className="text-gray-900 mb-6 font-serif">{post.content}</p>
              <div className="flex gap-3">
                <button className="bg-black text-white px-4 py-2 rounded-lg text-sm font-medium">Approve & Queue</button>
                <button className="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium">Reject</button>
              </div>
            </div>
          ))
        ) : (
          <div className="bg-white border border-dashed rounded-2xl p-12 text-center text-gray-500 flex flex-col items-center">
            <FileText className="w-8 h-8 mb-4 text-gray-300" />
            <p>No drafts pending review right now. The drafting loop will generate more soon.</p>
          </div>
        )}
      </div>
    </div>
  );
}
