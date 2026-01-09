# Theory notes: Ω as a readiness lattice

This is not metaphysics; it's control theory for boundary-crossing artifacts.

## Why a lattice instead of a single scalar?
A scalar score invites magical thinking: "0.82 means safe."
But “safe” is multidimensional: coherence, consent, usefulness, privacy risk, provenance quality.

So we:
1) compute continuous membership measures per axis,
2) map them into a *small set of discrete states* that can be governed.

Discrete states are easier to reason about in policy reviews, audits, and incident postmortems.

## The three axes (default)
- **CBD** (coherence/boundedness/dedup): Are we describing a stable object?
- **C'GT** (consent/governance/trust): Are we permitted and legitimate?
- **NHY** (delivery/usefulness): Did we deliver value without violating constraints?

We expect additional axes later (privacy, uncertainty, adversarial exposure). The lattice stays small; the measurements can grow.

## Promotion is monotone
This reference implementation only *promotes*.
Demotion (e.g., consent revoked) is modeled as a policy-triggered repair cycle, not a silent downgrade.

Why? Because silent demotion hides boundary events; repair makes them explicit.

## Where OPA fits
OPA policies operate over an *input envelope* that includes:
- the artifact (resource),
- consent state,
- validation results,
- de-id risk estimates,
- environment context.

OPA is excellent for:
- default-deny + explicit allow,
- explaining why something was blocked,
- emitting structured triggers for repair pipelines.
