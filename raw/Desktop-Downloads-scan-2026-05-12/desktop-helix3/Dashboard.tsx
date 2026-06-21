import { useApp } from "../context";
import { ComplianceGauge } from "../components/ComplianceGauge";
import { RiskBadge, VerdictBadge, HITLStatusBadge } from "../components/Badges";

export function Dashboard() {
  const { state, dispatch } = useApp();

  const totalPolicies  = state.policies.length;
  const activePolicies = state.policies.filter((p) => p.status === "ACTIVE").length;
  const draftPolicies  = state.policies.filter((p) => p.status === "DRAFT").length;

  const recentAudits   = state.auditTraces.slice(0, 5);
  const pendingHITL    = state.hitlQueue.filter((h) => h.status === "PENDING" || h.status === "ESCALATED");

  const overallScore = state.systems.length === 0
    ? 0
    : Math.round(
        state.systems.reduce((a, s) => a + s.complianceScore, 0) / state.systems.length
      );

  const law25Issues = state.assessments.filter(
    (a) => a.status === "NOT_STARTED" || a.status === "IN_PROGRESS"
  ).length;

  return (
    <div style={{ padding: "24px 28px", maxWidth: 1400 }}>
      {/* Page header */}
      <div className="fade-up" style={{ marginBottom: 24 }}>
        <h1 style={{
          fontFamily: "'Syne', sans-serif",
          fontSize: 22,
          fontWeight: 800,
          color: "var(--text)",
          letterSpacing: "-0.01em",
        }}>
          Governance Overview
        </h1>
        <p style={{ fontSize: 12, color: "var(--text-dim)", marginTop: 4, fontFamily: "'IBM Plex Mono', monospace" }}>
          Recursive Policy Engine · Law 25 Compliance · HELIX v2.6
        </p>
      </div>

      {/* Top row: metrics */}
      <div className="fade-up-1" style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))",
        gap: 12,
        marginBottom: 20,
      }}>
        <MetricCard
          value={overallScore + "%"}
          label="Law 25 Score"
          sub={`Across ${state.systems.length} systems`}
          color={overallScore >= 80 ? "var(--green)" : overallScore >= 60 ? "var(--amber)" : "var(--red)"}
        />
        <MetricCard
          value={activePolicies.toString()}
          label="Active Policies"
          sub={`${totalPolicies} total · ${draftPolicies} draft`}
          color="var(--gold)"
        />
        <MetricCard
          value={pendingHITL.length.toString()}
          label="HITL Pending"
          sub={pendingHITL.filter((h) => h.status === "ESCALATED").length + " escalated"}
          color={pendingHITL.length > 0 ? "var(--amber)" : "var(--green)"}
        />
        <MetricCard
          value={state.auditTraces.length.toString()}
          label="Audit Entries"
          sub={`${recentAudits.filter((a) => a.verdict === "FAIL").length} failures`}
          color="var(--teal)"
        />
        <MetricCard
          value={law25Issues.toString()}
          label="PIA Gaps"
          sub="Assessments incomplete"
          color={law25Issues > 0 ? "var(--red)" : "var(--green)"}
        />
      </div>

      {/* Main grid */}
      <div className="fade-up-2" style={{
        display: "grid",
        gridTemplateColumns: "1fr 1.4fr",
        gap: 16,
        marginBottom: 16,
      }}>
        {/* Compliance gauges */}
        <div className="card">
          <div className="card-header">System Compliance</div>
          <div className="card-body" style={{ display: "flex", flexWrap: "wrap", gap: 20, justifyContent: "center" }}>
            {state.systems.map((sys) => (
              <div key={sys.id} style={{ textAlign: "center" }}>
                <ComplianceGauge score={sys.complianceScore} size={100} />
                <div style={{
                  fontFamily: "'IBM Plex Mono', monospace",
                  fontSize: 9,
                  color: "var(--text-dim)",
                  marginTop: 2,
                  maxWidth: 90,
                  textAlign: "center",
                  lineHeight: 1.3,
                }}>
                  {sys.name.split(" ").slice(0, 2).join(" ")}
                </div>
                <div style={{ marginTop: 4 }}>
                  <RiskBadge risk={sys.riskLevel} />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Recent audits */}
        <div className="card">
          <div className="card-header">
            Recent Audit Traces
            <button
              className="btn"
              onClick={() => dispatch({ type: "NAVIGATE", route: "audit-log" })}
              style={{ fontSize: 9, padding: "3px 8px" }}
            >
              View All
            </button>
          </div>
          <div style={{ overflowX: "auto" }}>
            <table className="data-table">
              <thead>
                <tr>
                  <th>Policy</th>
                  <th>System</th>
                  <th>Verdict</th>
                  <th>Governor</th>
                  <th>Time</th>
                </tr>
              </thead>
              <tbody>
                {recentAudits.map((trace) => (
                  <tr key={trace.id}>
                    <td>
                      <div style={{ fontSize: 11, fontWeight: 500 }}>{trace.policyName}</div>
                    </td>
                    <td style={{ fontSize: 11, color: "var(--text-dim)" }}>{trace.systemName.split(" ")[0]}</td>
                    <td><VerdictBadge verdict={trace.verdict} /></td>
                    <td>
                      {trace.governorAction ? (
                        <span style={{
                          fontFamily: "'IBM Plex Mono', monospace",
                          fontSize: 9,
                          color: trace.governorAction === "TERMINATE_RECURSION" ? "var(--red)" : "var(--green)",
                        }}>
                          {trace.governorAction === "TERMINATE_RECURSION" ? "TERMINATE" : "CONTINUE"}
                        </span>
                      ) : (
                        <span style={{ color: "var(--text-ghost)", fontSize: 11 }}>—</span>
                      )}
                    </td>
                    <td style={{
                      fontFamily: "'IBM Plex Mono', monospace",
                      fontSize: 10,
                      color: "var(--text-dim)",
                      whiteSpace: "nowrap",
                    }}>
                      {new Date(trace.timestamp).toLocaleTimeString("en-CA", {
                        hour: "2-digit", minute: "2-digit",
                      })}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* HITL queue preview */}
      <div className="fade-up-3">
        <div className="card">
          <div className="card-header">
            Human-in-the-Loop Queue
            {pendingHITL.length > 0 && (
              <span className="badge badge-red">{pendingHITL.length} pending</span>
            )}
            <button
              className="btn"
              onClick={() => dispatch({ type: "NAVIGATE", route: "law25" })}
              style={{ fontSize: 9, padding: "3px 8px" }}
            >
              Manage Queue
            </button>
          </div>
          <div className="card-body">
            {pendingHITL.length === 0 ? (
              <p style={{ fontSize: 12, color: "var(--text-dim)", fontStyle: "italic" }}>
                No pending HITL requests. All Law 25 review rights satisfied.
              </p>
            ) : (
              <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
                {pendingHITL.slice(0, 3).map((req) => (
                  <div key={req.id} style={{
                    display: "flex",
                    alignItems: "flex-start",
                    gap: 12,
                    padding: "10px 12px",
                    background: "var(--raised)",
                    border: `1px solid ${req.status === "ESCALATED" ? "rgba(192,56,56,0.4)" : "var(--border)"}`,
                    borderRadius: "var(--radius)",
                  }}>
                    <div style={{ flexShrink: 0, paddingTop: 2 }}>
                      <HITLStatusBadge status={req.status} />
                    </div>
                    <div style={{ flex: 1 }}>
                      <div style={{ fontSize: 11, fontWeight: 500, lineHeight: 1.4 }}>
                        {req.decisionSummary.slice(0, 120)}…
                      </div>
                      <div style={{
                        display: "flex", gap: 8, marginTop: 5,
                        fontFamily: "'IBM Plex Mono', monospace", fontSize: 9, color: "var(--text-dim)",
                      }}>
                        <span>{req.systemName}</span>
                        <span>·</span>
                        <span>Right: {req.law25Right}</span>
                        <span>·</span>
                        <span>{req.requestedBy}</span>
                      </div>
                    </div>
                    <span className={`badge ${req.urgency === "CRITICAL" ? "badge-red" : req.urgency === "URGENT" ? "badge-amber" : "badge-dim"}`}>
                      {req.urgency}
                    </span>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function MetricCard({
  value, label, sub, color,
}: {
  value: string;
  label: string;
  sub?: string;
  color: string;
}) {
  return (
    <div className="metric">
      <div className="metric-value" style={{ color }}>{value}</div>
      <div className="metric-label">{label}</div>
      {sub && <div className="metric-sub">{sub}</div>}
    </div>
  );
}