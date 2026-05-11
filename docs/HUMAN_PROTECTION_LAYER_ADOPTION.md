# Human Protection Layer adoption for Human Digital Twin

Status: adoption stub referencing ProCybernetica reconciliation draft.

Authoritative doctrine source: `SocioProphet/ProCybernetica/docs/reconciliation/HUMAN_PROTECTION_LAYER.md`.

## 0. Position

Human Digital Twin (HDT) adopts the Human Protection Layer as a mandatory gate for human-boundary claims, consented exports, Atlas profiles, FCBCP/HSP-Map research profiles, and any future human-contact or human-derived evidence workflow.

HDT remains a protocol and reference implementation for evaluating, promoting, and exporting human-centric artifacts under zero-trust constraints. The Human Protection Layer clarifies that a human twin is never the human, an Ω label is never identity, and a valid claim is not automatically exportable.

## 1. HDT-specific protection rule

HDT exports claims with provenance, not raw unaudited human identity or raw private evidence.

Default policy:

- raw private evidence stays local;
- derived claims require provenance;
- human-derived exports require consent or a recorded policy/legal basis;
- Ω readiness is a governance label, not truth or identity;
- human actuation is blocked by default;
- FCBCP/HSP-Map is research-only unless an external ethics/regulatory pathway authorizes otherwise;
- unsupported biological mechanism claims are blocked from export as validated claims.

## 2. Required HPL gates for HDT

Every HDT human-boundary export must evaluate:

1. Claim boundary: mechanism status, evidence tier, limitations, unsupported-claim block.
2. Consent/autonomy: consent scope, revocation, purpose limitation.
3. Privacy/minimization: raw evidence attached false by default, minimal claim export.
4. Physical safety: human actuation blocked by default.
5. Cognitive safety: no hidden persuasion, no covert sensitive inference export.
6. Cyber/misuse safety: no side-effectful tool path without declared authority.
7. Redress: inspect, challenge, revoke, appeal paths where applicable.

## 3. FCBCP and HSP-Map adoption

FCBCP and HSP-Map may be represented in HDT only under research/profile status until separate external approval exists.

Allowed by default:

- documentation;
- schemas;
- toy transfer models;
- simulation-only Atlas fixtures;
- synthetic/phantom fixtures;
- policy tests;
- negative tests for unsupported mechanisms.

Blocked by default:

- human actuation;
- uncontrolled human-contact protocols;
- exporting raw physiological telemetry;
- treating phantom-DNA, wave-text, DNA-inductor, DNA-speaker, holographic-gene-laser, or native-DNA-biological-magnet claims as validated mechanisms;
- autonomous high-impact decisions about a person.

## 4. HDT minimum export envelope

All human-derived claim exports should include:

```yaml
resource_id: string
omega_state: ABSENT | SEEDED | NORMALIZED | LINKED | TRUSTED | ACTIONABLE | DELIVERED
evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
claim: string
claim_boundary:
  mechanism_status: validated | hypothesis | metaphor_only | excluded | unknown
  unsupported_claim_blocked: boolean
consent:
  required: boolean
  present: boolean
  scope: [string]
privacy:
  raw_private_evidence_attached: false
  minimization_basis: string
physical_safety:
  human_actuation: blocked | simulation_only | protocol_required | approved_external_process
redress:
  inspect: boolean
  challenge: boolean
  revoke: boolean
  appeal: boolean
policy:
  decision: allow | deny | block | needs_review
  reasons: [string]
provenance:
  evidence_hash: string
  policy_version: string
```

## 5. Required tests before promotion

HDT should add or maintain tests proving:

- raw private evidence is not exportable by default;
- missing consent blocks consent-required human-derived exports;
- Ω promotion alone cannot authorize export;
- human actuation is blocked by default;
- FCBCP/HSP-Map profiles remain simulation/research-only by default;
- unsupported biological mechanisms cannot appear as validated mechanism labels;
- appeal/redress metadata is required for high-impact outputs.

## 6. Atlas relationship

For Digital Control Atlas work, HDT owns only the human-boundary profile. HDT does not own world-chart governance, ProCybernetica control law, Superconscious planning authority, or AgentPlane replay authority.

Canonical relation:

```text
AtlasAuditResult -> HDT EvidenceClaim -> Ω Evaluation -> Policy Decision -> Minimal Export or Block
```

There is no direct path from Atlas validity to HDT export.
