import { useState } from "react";
import { useApp } from "../context";
import { PolicyTree } from "../components/PolicyTree";
import { LevelBadge, StatusBadge, RiskBadge } from "../components/Badges";
import type { Policy, PolicyLevel, PolicyStatus, RiskLevel } from "../types";

const EMPTY_POLICY: Omit<Policy, "id" | "createdAt" | "updatedAt" | "executionCount" | "lastExecutedAt"> = {
  name: "",
  description: "",
  level: "L1_SCRIPT",
  status: "DRAFT",
  parentId: null,
  childIds: [],
  rule: "",
  riskLevel: "MEDIUM",
  law25Linked: false,
  law25Section: "",
};

export function PolicyEngine() {
  const { state, dispatch } = useApp();
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [showNewForm, setShowNewForm] = useState(false);
  const [newPolicy, setNewPolicy] = useState({ ...EMPTY_POLICY });
  const [filterLevel, setFilterLevel] = useState<PolicyLevel | "ALL">("ALL");
  const [filterStatus, setFilterStatus] = useState<PolicyStatus | "ALL">("ALL");

  const selected = state.policies.find((p) => p.id === selectedId);

  const filtered = state.policies.filter((p) => {
    if (filterLevel !== "ALL" && p.level !== filterLevel) return false;
    if (filterStatus !== "ALL" && p.status !== filterStatus) return false;
    return true;
  });

  // Nodes whose parent is outside the filtered set become roots in the visible tree
  const filteredIds = new Set(filtered.map((p) => p.id));
  const rootIds = filtered
    .filter((p) => p.parentId === null || !filteredIds.has(p.parentId))
    .map((p) => p.id);

  const handleCreate = () => {
    const now = new Date().toISOString();
    const pol: Policy = {
      ...newPolicy,
      id: `pol-${Date.now()}`,
      createdAt: now,
      updatedAt: now,
      executionCount: 0,
      lastExecutedAt: null,
      childIds: [],
    };
    dispatch({ type: "ADD_POLICY", policy: pol });
    if (pol.parentId) {
      const parent = state.policies.find((p) => p.id === pol.parentId);
      if (parent) {
        dispatch({
          type: "UPDATE_POLICY",
          id: pol.parentId,
          patch: { childIds: [...parent.childIds, pol.id], updatedAt: now },
        });
      }
    }
    setShowNewForm(false);
    setNewPolicy({ ...EMPTY_POLICY });
    setSelectedId(pol.id);
  };

  const handleStatusToggle = (pol: Policy) => {
    const next: PolicyStatus =
      pol.status === "ACTIVE" ? "SUSPENDED" :
      pol.status === "SUSPENDED" ? "ACTIVE" :
      pol.status === "DRAFT" ? "ACTIVE" : "ARCHIVED";
    dispatch({ type: "UPDATE_POLICY", id: pol.id, patch: { status: next, updatedAt: new Date().toISOString() } });
  };

  return (
    <div style={{ display: "flex", height: "100%", overflow: "hidden" }}>
      {/* ── Left panel: tree + filters ── */}
      <div style={{
        width: 340,
        flexShrink: 0,
        borderRight: "1px solid var(--border)",
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
      }}>
        {/* Tree toolbar */}
        <div style={{
          padding: "12px 14px",
          borderBottom: "1px solid var(--border)",
          background: "var(--deep)",
        }}>
          <div style={{ display: "flex", gap: 6, marginBottom: 8 }}>
            <select
              className="input"
              value={filterLevel}
              onChange={(e) => setFilterLevel(e.target.value as PolicyLevel | "ALL")}
              style={{ fontSize: 11, padding: "5px 8px" }}
            >
              <option value="ALL">All Levels</option>
              <option value="L3_META">L3 Meta</option>
              <option value="L2_POLICY">L2 Policy</option>
              <option value="L1_SCRIPT">L1 Script</option>
            </select>
            <select
              className="input"
              value={filterStatus}
              onChange={(e) => setFilterStatus(e.target.value as PolicyStatus | "ALL")}
              style={{ fontSize: 11, padding: "5px 8px" }}
            >
              <option value="ALL">All Status</option>
              <option value="ACTIVE">Active</option>
              <option value="DRAFT">Draft</option>
              <option value="SUSPENDED">Suspended</option>
            </select>
          </div>
          <button
            className="btn primary"
            style={{ width: "100%", justifyContent: "center" }}
            onClick={() => setShowNewForm(true)}
          >
            + New Policy
          </button>
        </div>

        {/* Stats row */}
        <div style={{
          display: "flex",
          gap: 0,
          borderBottom: "1px solid var(--border)",
          background: "var(--raised)",
        }}>
          {(["L3_META", "L2_POLICY", "L1_SCRIPT"] as PolicyLevel[]).map((lvl) => {
            const count = state.policies.filter((p) => p.level === lvl).length;
            const colors = { L3_META: "var(--gold)", L2_POLICY: "var(--teal)", L1_SCRIPT: "var(--blue)" };
            const labels = { L3_META: "L3", L2_POLICY: "L2", L1_SCRIPT: "L1" };
            return (
              <div key={lvl} style={{
                flex: 1,
                padding: "8px",
                textAlign: "center",
                borderRight: lvl !== "L1_SCRIPT" ? "1px solid var(--border)" : "none",
              }}>
                <div style={{ fontFamily: "'Syne', sans-serif", fontSize: 16, fontWeight: 800, color: colors[lvl] }}>
                  {count}
                </div>
                <div style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: 9, color: "var(--text-dim)" }}>
                  {labels[lvl]}
                </div>
              </div>
            );
          })}
        </div>

        {/* Tree */}
        <div style={{ flex: 1, overflowY: "auto", padding: "8px 6px" }}>
          <PolicyTree
            policies={filtered}
            rootIds={rootIds}
            onSelect={(p) => setSelectedId(p.id)}
            selectedId={selectedId || undefined}
          />
        </div>
      </div>

      {/* ── Right panel: detail / form ── */}
      <div style={{ flex: 1, overflow: "auto", padding: "20px 24px" }}>
        {showNewForm ? (
          <NewPolicyForm
            value={newPolicy}
            policies={state.policies}
            onChange={(patch) => setNewPolicy((p) => ({ ...p, ...patch }))}
            onSave={handleCreate}
            onCancel={() => setShowNewForm(false)}
          />
        ) : selected ? (
          <PolicyDetail
            policy={selected}
            allPolicies={state.policies}
            onStatusToggle={() => handleStatusToggle(selected)}
          />
        ) : (
          <Empty />
        )}
      </div>
    </div>
  );
}

function PolicyDetail({
  policy,
  allPolicies,
  onStatusToggle,
}: {
  policy: Policy;
  allPolicies: Policy[];
  onStatusToggle: () => void;
}) {
  const parent = allPolicies.find((p) => p.id === policy.parentId);
  const children = allPolicies.filter((p) => p.parentId === policy.id);

  return (
    <div style={{ maxWidth: 700 }}>
      <div className="fade-up" style={{ display: "flex", alignItems: "flex-start", gap: 12, marginBottom: 20 }}>
        <div style={{ flex: 1 }}>
          <div style={{ display: "flex", gap: 6, marginBottom: 8, flexWrap: "wrap", alignItems: "center" }}>
            <LevelBadge level={policy.level} />
            <StatusBadge status={policy.status} />
            <RiskBadge risk={policy.riskLevel} />
            {policy.law25Linked && policy.law25Section && (
              <span className="badge badge-gold">Law 25 s.{policy.law25Section}</span>
            )}
          </div>
          <h2 style={{ fontSize: 18, fontWeight: 700 }}>{policy.name}</h2>
          <p style={{ fontSize: 12, color: "var(--text-dim)", marginTop: 6, lineHeight: 1.5 }}>
            {policy.description}
          </p>
        </div>
        <button className="btn" onClick={onStatusToggle} style={{ flexShrink: 0 }}>
          {policy.status === "ACTIVE" ? "Suspend" : policy.status === "SUSPENDED" ? "Reactivate" : "Activate"}
        </button>
      </div>

      {/* Rule */}
      <div className="card fade-up-1" style={{ marginBottom: 14 }}>
        <div className="card-header">Governance Rule</div>
        <div className="card-body">
          <pre style={{
            fontFamily: "'IBM Plex Mono', monospace",
            fontSize: 11,
            lineHeight: 1.7,
            color: "var(--text)",
            whiteSpace: "pre-wrap",
            wordBreak: "break-word",
          }}>
            {policy.rule}
          </pre>
        </div>
      </div>

      {/* Invariant */}
      {policy.invariant && (
        <div className="card fade-up-2" style={{
          marginBottom: 14,
          borderColor: "rgba(200,160,64,0.3)",
          background: "rgba(200,160,64,0.04)",
        }}>
          <div className="card-header" style={{ color: "var(--gold)" }}>
            ⟳ Recursion Invariant
          </div>
          <div className="card-body">
            <p style={{
              fontFamily: "'IBM Plex Mono', monospace",
              fontSize: 11,
              lineHeight: 1.7,
              color: "var(--gold)",
              fontStyle: "italic",
            }}>
              "{policy.invariant}"
            </p>
          </div>
        </div>
      )}

      {/* Stats */}
      <div className="fade-up-3" style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: 10,
        marginBottom: 14,
      }}>
        {[
          { label: "Executions", value: policy.executionCount.toLocaleString() },
          {
            label: "Last Run",
            value: policy.lastExecutedAt
              ? new Date(policy.lastExecutedAt).toLocaleString("en-CA", { month: "short", day: "2-digit", hour: "2-digit", minute: "2-digit" })
              : "Never",
          },
          {
            label: "Updated",
            value: new Date(policy.updatedAt).toLocaleDateString("en-CA"),
          },
        ].map(({ label, value }) => (
          <div key={label} style={{
            background: "var(--raised)",
            border: "1px solid var(--border)",
            borderRadius: "var(--radius)",
            padding: "10px 12px",
          }}>
            <div style={{
              fontFamily: "'IBM Plex Mono', monospace",
              fontSize: 9,
              color: "var(--text-dim)",
              textTransform: "uppercase",
              letterSpacing: "0.08em",
              marginBottom: 4,
            }}>
              {label}
            </div>
            <div style={{ fontFamily: "'Syne', sans-serif", fontSize: 14, fontWeight: 700 }}>{value}</div>
          </div>
        ))}
      </div>

      {/* Hierarchy */}
      <div className="card fade-up-4">
        <div className="card-header">Hierarchy</div>
        <div className="card-body" style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          {parent && (
            <div>
              <div style={{
                fontFamily: "'IBM Plex Mono', monospace",
                fontSize: 9,
                color: "var(--text-dim)",
                textTransform: "uppercase",
                marginBottom: 4,
              }}>Parent</div>
              <div style={{
                display: "flex",
                gap: 6,
                alignItems: "center",
                padding: "6px 10px",
                background: "var(--raised)",
                border: "1px solid var(--border)",
                borderRadius: "var(--radius)",
              }}>
                <LevelBadge level={parent.level} />
                <span style={{ fontSize: 12 }}>{parent.name}</span>
              </div>
            </div>
          )}
          {children.length > 0 && (
            <div>
              <div style={{
                fontFamily: "'IBM Plex Mono', monospace",
                fontSize: 9,
                color: "var(--text-dim)",
                textTransform: "uppercase",
                marginBottom: 4,
              }}>
                Children ({children.length})
              </div>
              {children.map((child) => (
                <div key={child.id} style={{
                  display: "flex",
                  gap: 6,
                  alignItems: "center",
                  padding: "6px 10px",
                  background: "var(--raised)",
                  border: "1px solid var(--border)",
                  borderRadius: "var(--radius)",
                  marginBottom: 4,
                }}>
                  <LevelBadge level={child.level} />
                  <StatusBadge status={child.status} />
                  <span style={{ fontSize: 12 }}>{child.name}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function NewPolicyForm({
  value, policies, onChange, onSave, onCancel,
}: {
  value: typeof EMPTY_POLICY;
  policies: Policy[];
  onChange: (patch: Partial<typeof EMPTY_POLICY>) => void;
  onSave: () => void;
  onCancel: () => void;
}) {
  return (
    <div style={{ maxWidth: 600 }}>
      <div className="fade-up" style={{ marginBottom: 20 }}>
        <h2 style={{ fontSize: 16, fontWeight: 700 }}>New Policy</h2>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        <div>
          <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>
            Name *
          </label>
          <input className="input" value={value.name} onChange={(e) => onChange({ name: e.target.value })} placeholder="Policy name..." />
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
          <div>
            <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>Level</label>
            <select className="input" value={value.level} onChange={(e) => onChange({ level: e.target.value as PolicyLevel })}>
              <option value="L1_SCRIPT">L1 Script</option>
              <option value="L2_POLICY">L2 Policy</option>
              <option value="L3_META">L3 Meta-Governance</option>
            </select>
          </div>
          <div>
            <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>Risk Level</label>
            <select className="input" value={value.riskLevel} onChange={(e) => onChange({ riskLevel: e.target.value as RiskLevel })}>
              <option value="LOW">Low</option>
              <option value="MEDIUM">Medium</option>
              <option value="HIGH">High</option>
              <option value="CRITICAL">Critical</option>
            </select>
          </div>
        </div>

        <div>
          <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>Parent Policy</label>
          <select className="input" value={value.parentId || ""} onChange={(e) => onChange({ parentId: e.target.value || null })}>
            <option value="">None (root)</option>
            {policies.map((p) => (
              <option key={p.id} value={p.id}>[{p.level}] {p.name}</option>
            ))}
          </select>
        </div>

        <div>
          <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>Description</label>
          <textarea className="input" value={value.description} onChange={(e) => onChange({ description: e.target.value })} placeholder="Policy description..." style={{ minHeight: 60 }} />
        </div>

        <div>
          <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>Governance Rule *</label>
          <textarea className="input" value={value.rule} onChange={(e) => onChange({ rule: e.target.value })} placeholder="The actual governance rule text..." style={{ minHeight: 90 }} />
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
          <div>
            <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>
              <input
                type="checkbox"
                checked={value.law25Linked}
                onChange={(e) => onChange({ law25Linked: e.target.checked })}
                style={{ marginRight: 6 }}
              />
              Law 25 Linked
            </label>
          </div>
          {value.law25Linked && (
            <div>
              <label style={{ fontSize: 11, color: "var(--text-dim)", display: "block", marginBottom: 5, fontFamily: "'IBM Plex Mono', monospace", textTransform: "uppercase", letterSpacing: "0.07em" }}>Section</label>
              <input className="input" value={value.law25Section || ""} onChange={(e) => onChange({ law25Section: e.target.value })} placeholder="e.g. 12.1" />
            </div>
          )}
        </div>

        <div style={{ display: "flex", gap: 10 }}>
          <button
            className="btn primary"
            onClick={onSave}
            disabled={!value.name || !value.rule}
          >
            Create Policy
          </button>
          <button className="btn" onClick={onCancel}>Cancel</button>
        </div>
      </div>
    </div>
  );
}

function Empty() {
  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      height: "60%",
      color: "var(--text-ghost)",
      gap: 12,
    }}>
      <div style={{ fontSize: 32, opacity: 0.3 }}>◈</div>
      <div style={{
        fontFamily: "'IBM Plex Mono', monospace",
        fontSize: 11,
        textAlign: "center",
        lineHeight: 1.6,
      }}>
        Select a policy from the tree<br />
        to view its governance rules.
      </div>
    </div>
  );
}