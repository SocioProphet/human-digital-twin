# The Twin as a Body-State Model — adding the model representation

## What the twin *is*

The Human Digital Twin is not a biomimetic metaphor for the platform. It is a **digital state
model of a physical human body**: a live estimated state `x(t)` of the person's organ-compartment
sub-systems (cardio, metabolic, immune, neuro, …), kept synchronized to the real body by state
estimation over consented sensor streams (biometrics, HRV, kinematics, labs, wearables, EHR).

This is the engineering digital-twin sense — physical entity ⇄ synchronized virtual state — and it is
the *Digital Twin Synchronization* band of the unified cognitive-systems map (physical sensor data →
Kalman/assimilation → sim engine → anthropometric profile). The Ω Protocol Kit in this repo already
supplies the **governance spine** for that state (consent, readiness lattice, protection envelope,
provenance). What was missing is the thing that makes a *state* into a *twin*.

## The gap this note closes: a stored state is not a twin

A snapshot of `x(t)` is a dashboard. A twin must be **predictive** — it needs a model that evolves
`x(t) → x(t+1)`. That model is the **model representation**, and it is hybrid by construction:

- **Mechanistic** — physiology ODEs, PK/PD, compartment dynamics. Explicit, interpretable, and run
  under the **verified-compute** gate (an executed forward step, not a free-text guess). This is the
  same verified-computation moat, applied to the body.
- **Learned surrogate** — a data-driven model of the personal residual the equations miss, distilled
  from the person's *own consented history* (never generic web data, never model-of-model slop). Its
  weights are an attested artifact (SBOM entry in the governance ledger), versioned and revocable.
- **The gate reconciles them** — *learned proposes, physics disposes.* A forward step that is
  `learned_only` or `divergent` (physics did not verify it) **must not** cross a boundary as
  actionable and **must not** drive human actuation.

On a body twin this reconciliation is not optional governance; it is the safety floor. A learned model
must be structurally unable to promote a physiological trajectory the mechanistic model rejects.

## It plugs into Ω — it does not go around it

`x(t)` and its predictions are dispositive personal data that may cross a boundary (clinician export,
agent delegation, actuation). So a body-state instance is an **Ω-evaluable artifact**:

- It carries an `omega_state` on the existing lattice
  `ABSENT → SEEDED → NORMALIZED → LINKED → TRUSTED → ACTIONABLE → DELIVERED`
  (`api/services/eval/omega.py`).
- It embeds the **Human Protection Envelope** by `$ref`
  (`api/schemas/hpl/human-protection-envelope.json`) — consent, privacy, physical/cognitive safety,
  policy decision, provenance. *Validity is not permission; policy status is mandatory.*
- Two safety invariants are enforced **in the schema** (verified — see the validation in the PR):
  1. `reconciliation ∈ {learned_only, divergent}` ⇒ `omega_state ≤ TRUSTED` and
     `human_actuation ∈ {blocked, blocked_by_default, simulation_only}`.
  2. `omega_state ∈ {ACTIONABLE, DELIVERED}` ⇒ `consent.present = true` **and**
     `policy.decision = allow`.

The new contract is `api/schemas/body-state/body-state-model.schema.json`.

## Rollout — bedrock → services → substrate

| Phase | The body-state model in it | Concrete in this repo / estate |
|---|---|---|
| **Roll platform bedrock** | the **representation and its guardrails** — no dynamics yet | the body-state schema + the Ω lattice + the protection envelope + consent/attestation. The state's *shape* and its permission floor. |
| **Stand up long-running services** | the **coupled model as a live service** | mechanistic sim engine (verified compute) + learned-surrogate serving + the reconciling gate, always-on and per-twin; state estimation running continuously at the sync rate; the TritRPC surface (`api/trpc/`) fronts `evaluate`/`evolve`. |
| **Deploy the substrate** | **bind** sensors + state + model + governance into a deployed twin instance | one attested digital body per person, federating with peer twins under signed federation. Lands on `human-digital-twin` + `gaia-world-model` (twin substrate). |

## Why the moat maps here exactly

The mechanistic half runs under the **same verified-compute machinery** measured by the frontier-math
board (`Noetica/agent-machine/scripts/frontier-math-bench.ts`): the physiology forward step is a
verified computation, gated identically to any operator. The learned half is the Wave B distillation
target. The gate between them is the product — and it is most defensible precisely where the stakes are
a real person's state.

## Honest state

Today the twin has the **symbolic/governance layer shipped** (Ω lattice, protection envelope, consent,
provenance) and now a **conformant body-state contract with the model representation specified and its
safety gates verified**. It becomes a *running* predictive twin once (a) the mechanistic sim engine and
(b) the learned surrogate are served behind the gate as long-running services. The schema is the bedrock
artifact your team builds against; the services phase makes it live.
