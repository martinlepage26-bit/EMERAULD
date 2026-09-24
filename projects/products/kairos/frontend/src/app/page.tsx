"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { CheckCircle2, ArrowRight, BarChart3, Clock, MessageSquare, PenTool } from "lucide-react";
import { SignupDialog } from "@/components/SignupDialog";
import { getPublicConfig } from "@/lib/api";

export default function Home() {
  const [signupPlan, setSignupPlan] = useState<{ id: string; name: string } | null>(null);
  const [signupEnabled, setSignupEnabled] = useState(true);

  useEffect(() => {
    getPublicConfig().then((c) => setSignupEnabled(c.signupEnabled));
  }, []);

  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="flex items-center justify-between px-6 py-4 border-b bg-white">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 bg-black rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-xl leading-none">K</span>
          </div>
          <span className="text-xl font-semibold tracking-tight">Kairos</span>
        </div>
        <nav className="flex items-center gap-6 text-sm font-medium">
          <Link href="#features" className="text-gray-600 hover:text-black">Features</Link>
          <Link href="#pricing" className="text-gray-600 hover:text-black">Pricing</Link>
          <Link href="/dashboard" className="text-black bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-full transition-colors">
            Login
          </Link>
        </nav>
      </header>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="px-6 py-24 md:py-32 max-w-5xl mx-auto text-center">
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-gray-900 mb-8">
            The opportune moment.<br />
            <span className="text-gray-500">Every time.</span>
          </h1>
          <p className="text-xl text-gray-600 mb-10 max-w-2xl mx-auto leading-relaxed">
            A subscription platform that plans, publishes, and grows your audience without you scheduling posts or answering messages by hand.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <button
              onClick={() => setSignupPlan({ id: "solo", name: "Solo" })}
              className="bg-black text-white px-8 py-4 rounded-full font-medium hover:bg-gray-800 transition-colors flex items-center gap-2"
            >
              {signupEnabled ? "Start Free Trial" : "Request Access"} <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="bg-gray-50 py-24 px-6">
          <div className="max-w-6xl mx-auto">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold mb-4">What Kairos does for you</h2>
              <p className="text-gray-600 max-w-2xl mx-auto">
                Describe your business, your voice, and the topics you want to be known for. Kairos handles the rest, and nothing goes out until you approve it.
              </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
              <FeatureCard 
                icon={<Clock />}
                title="1. Plans"
                description="Keeps a 14-day posting calendar full, giving more room to the topics that actually get results."
              />
              <FeatureCard 
                icon={<PenTool />}
                title="2. Drafts"
                description="Writes three versions of every post in your voice, and never uses words you have ruled out."
              />
              <FeatureCard 
                icon={<CheckCircle2 />}
                title="3. Publishes"
                description="Posts at the right time on each platform, exactly once, even when a network hiccups."
              />
              <FeatureCard 
                icon={<MessageSquare />}
                title="4. Answers"
                description="Sorts incoming messages, drafts replies, and sends only the routine ones. Leads and complaints always come to you."
              />
              <FeatureCard 
                icon={<BarChart3 />}
                title="5. Compounds"
                description="Learns what your audience responds to, shifts effort toward it, and brings your best posts back for new followers."
              />
            </div>
          </div>
        </section>

        {/* Pricing Section */}
        <section id="pricing" className="py-24 px-6 max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold mb-4">Simple, Transparent Pricing</h2>
            <p className="text-gray-600">Choose the tier that fits your growth stage.</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <PricingCard title="Solo" price="$49" channels={2} posts={60} replies={200} onSelect={setSignupPlan} />
            <PricingCard title="Pro" price="$149" channels={5} posts={200} replies={800} popular onSelect={setSignupPlan} />
            <PricingCard title="Studio" price="$399" channels={15} posts={700} replies={2000} onSelect={setSignupPlan} />
            <PricingCard title="Agency" price="$999" channels={50} posts={2000} replies={5000} onSelect={setSignupPlan} />
          </div>
        </section>
      </main>

      {signupPlan && (
        <SignupDialog
          planId={signupPlan.id}
          planName={signupPlan.name}
          signupEnabled={signupEnabled}
          onClose={() => setSignupPlan(null)}
        />
      )}

      <footer className="border-t py-12 text-center text-gray-500 text-sm">
        <p>© {new Date().getFullYear()} Kairos. Built for the opportune moment.</p>
      </footer>
    </div>
  );
}

function FeatureCard({ icon, title, description }: { icon: React.ReactNode, title: string, description: string }) {
  return (
    <div className="bg-white p-8 rounded-2xl border shadow-sm">
      <div className="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center text-gray-900 mb-6">
        {icon}
      </div>
      <h3 className="text-xl font-bold mb-3">{title}</h3>
      <p className="text-gray-600 leading-relaxed">{description}</p>
    </div>
  );
}

function PricingCard({
  title,
  price,
  channels,
  posts,
  replies,
  popular,
  onSelect,
}: {
  title: string;
  price: string;
  channels: number;
  posts: number;
  replies: number;
  popular?: boolean;
  onSelect: (plan: { id: string; name: string }) => void;
}) {
  return (
    <div className={`p-8 rounded-3xl border flex flex-col ${popular ? 'border-black ring-1 ring-black shadow-lg relative' : 'border-gray-200 bg-white'}`}>
      {popular && (
        <span className="absolute -top-4 left-1/2 -translate-x-1/2 bg-black text-white px-3 py-1 rounded-full text-xs font-bold tracking-wide">
          MOST POPULAR
        </span>
      )}
      <h3 className="text-lg font-semibold text-gray-900 mb-2">{title}</h3>
      <div className="mb-6">
        <span className="text-4xl font-bold">{price}</span>
        <span className="text-gray-500">/mo</span>
      </div>
      <ul className="space-y-4 mb-8 flex-1 text-sm text-gray-600">
        <li className="flex items-center gap-3">
          <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0" /> {channels} Channels
        </li>
        <li className="flex items-center gap-3">
          <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0" /> {posts} Posts/mo
        </li>
        <li className="flex items-center gap-3">
          <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0" /> {replies} Auto-replies/mo
        </li>
      </ul>
      <button
        onClick={() => onSelect({ id: title.toLowerCase(), name: title })}
        className={`w-full py-3 rounded-xl font-medium transition-colors ${popular ? 'bg-black text-white hover:bg-gray-800' : 'bg-gray-100 text-gray-900 hover:bg-gray-200'}`}>
        Select {title}
      </button>
    </div>
  );
}
