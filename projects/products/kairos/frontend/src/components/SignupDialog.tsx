"use client";

import { useState } from "react";
import { Copy, Check, X } from "lucide-react";
import { ApiError, signup, startCheckout, storeKey, storedKey } from "@/lib/api";

/**
 * Signup is the first half of checkout, not a separate flow: `/v1/billing/checkout`
 * requires a bearer key, and a visitor has none until an account exists. So this
 * creates the account, shows the key once (the API will never return it again),
 * and only then opens Stripe.
 */
type Stage =
  | { name: "form" }
  | { name: "working" }
  | { name: "key"; apiKey: string; trialEndsAt: string }
  | { name: "error"; message: string };

export function SignupDialog({
  planId,
  planName,
  onClose,
}: {
  planId: string;
  planName: string;
  onClose: () => void;
}) {
  const [stage, setStage] = useState<Stage>({ name: "form" });
  const [email, setEmail] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [copied, setCopied] = useState(false);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStage({ name: "working" });
    try {
      const result = await signup({ email: email.trim(), displayName: displayName.trim() });
      storeKey(result.apiKey);
      setStage({ name: "key", apiKey: result.apiKey, trialEndsAt: result.trialEndsAt });
    } catch (err) {
      const message =
        err instanceof ApiError && err.code === "conflict"
          ? "An account already exists for that email. Use your existing key on the dashboard."
          : err instanceof ApiError
            ? err.message
            : "Could not reach the API. Check your connection and try again.";
      setStage({ name: "error", message });
    }
  };

  const proceedToCheckout = async () => {
    const key = storedKey();
    if (!key) {
      setStage({ name: "error", message: "The key was not saved. Copy it and use the dashboard." });
      return;
    }
    setStage({ name: "working" });
    try {
      const { url } = await startCheckout(planId, key);
      if (url) {
        window.location.href = url;
      } else {
        setStage({
          name: "error",
          message: "Stripe returned no checkout URL. Your trial is active either way.",
        });
      }
    } catch (err) {
      setStage({
        name: "error",
        message:
          err instanceof ApiError
            ? `Checkout could not start: ${err.message}`
            : "Checkout could not start. Your trial is active either way.",
      });
    }
  };

  const copyKey = async (apiKey: string) => {
    try {
      await navigator.clipboard.writeText(apiKey);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      /* Clipboard access can be denied; the key is selectable on screen. */
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-xl p-8 relative">
        <button
          onClick={onClose}
          aria-label="Close"
          className="absolute top-4 right-4 text-gray-400 hover:text-gray-900"
        >
          <X className="w-5 h-5" />
        </button>

        {stage.name === "key" ? (
          <>
            <h2 className="text-xl font-semibold mb-2">Save your API key</h2>
            <p className="text-sm text-gray-500 mb-4">
              This is shown once and cannot be retrieved again. Your 14-day trial runs to{" "}
              {new Date(stage.trialEndsAt).toLocaleDateString()}.
            </p>

            <div className="flex items-center gap-2 mb-6">
              <code className="flex-1 text-xs bg-gray-50 border rounded-lg px-3 py-2 break-all">
                {stage.apiKey}
              </code>
              <button
                onClick={() => copyKey(stage.apiKey)}
                aria-label="Copy API key"
                className="shrink-0 border rounded-lg p-2 hover:bg-gray-50"
              >
                {copied ? <Check className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
              </button>
            </div>

            <button
              onClick={proceedToCheckout}
              className="w-full bg-black text-white py-3 rounded-xl font-medium hover:bg-gray-800"
            >
              Continue to {planName} checkout
            </button>
            <a
              href="/dashboard"
              className="block text-center text-sm text-gray-500 hover:text-gray-900 mt-3"
            >
              Skip for now, stay on the trial
            </a>
          </>
        ) : (
          <>
            <h2 className="text-xl font-semibold mb-2">Start your {planName} trial</h2>
            <p className="text-sm text-gray-500 mb-6">
              Fourteen days, autopilot off by default. We create your account first, because
              checkout needs the key it issues.
            </p>

            <form onSubmit={submit} className="space-y-3">
              <input
                type="text"
                required
                value={displayName}
                onChange={(e) => setDisplayName(e.target.value)}
                placeholder="Your name"
                className="w-full border rounded-lg px-4 py-2"
              />
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@example.com"
                className="w-full border rounded-lg px-4 py-2"
              />

              {stage.name === "error" && (
                <p className="text-sm text-red-600" role="alert">
                  {stage.message}
                </p>
              )}

              <button
                type="submit"
                disabled={stage.name === "working"}
                className="w-full bg-black text-white py-3 rounded-xl font-medium hover:bg-gray-800 disabled:opacity-40"
              >
                {stage.name === "working" ? "Creating your account…" : "Create account"}
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
}
