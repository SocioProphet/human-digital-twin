# FCBCP falsifiable hypotheses

Status: research hypothesis scaffold. Not validated human-contact science.

Owner: `SocioProphet/human-digital-twin`.

Related:

- `docs/research/fcbcp/FCBCP_SPEC_V1.md`
- `docs/research/fcbcp/BIOLOGICAL_MECHANISM_SPINE.md`
- `docs/research/fcbcp/TIME_SCALE_LADDER.md`
- `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md`

## 0. Purpose

This document captures FCBCP's falsifiable hypotheses as research constraints. These hypotheses are not claims of safety, treatment, diagnosis, or human actuation validity.

Each hypothesis must specify:

- endpoint;
- context: simulation, synthetic, phantom, ex vivo, or externally reviewed human-contact process;
- measurement method;
- safety constraints;
- null model;
- falsification condition;
- evidence tier.

## H1 — Boundary transparency

Claim under test:

For a declared region and context, there may exist a frequency band in which measured surface-to-interior or surface-to-proxy transfer matches the declared tissue/boundary model within a prespecified tolerance.

Required evidence:

- HSP-Map entry;
- impedance or transfer estimate;
- uncertainty interval;
- phantom/synthetic/ex vivo context unless externally reviewed;
- model residual;
- safety status.

Falsification / revision triggers:

- measured transfer does not match the model within tolerance;
- model cannot distinguish layer effects from artifact;
- uncertainty is too large for planning;
- person-specific data lacks consent/policy basis.

Default status:

`research_hypothesis` / `SAFE_TO_SIMULATE` unless context upgrades through review.

## H2 — Driver linearity within safety envelope

Claim under test:

Within a declared safety envelope, an internal driver proxy, such as membrane-polarization proxy, may scale with predicted transfer and input amplitude over a limited range.

Required evidence:

- boundary-transfer estimate;
- driver proxy readout;
- amplitude/frequency grid;
- safety caps;
- uncertainty and residuals;
- sham or null controls.

Falsification / revision triggers:

- nonlinear response outside declared model;
- observed response appears without boundary transfer;
- safety caps exceeded;
- artifact explains the driver proxy.

Default status:

`research_hypothesis` / `SAFE_FOR_PHANTOM_TEST` or `SAFE_FOR_EX_VIVO_RESEARCH` only when protocol conditions are present.

## H3 — Cascade lag

Claim under test:

When a physical or membrane-level driver is confirmed, downstream second-messenger, RNA, protein, and chromatin responses should follow a biologically plausible time ordering.

Expected sequence:

```text
driver proxy -> second messenger -> RNA -> protein -> chromatin/tissue adaptation
```

Required evidence:

- time-stamped driver readout;
- second-messenger readout where claimed;
- RNA timepoints;
- protein/secretome/chromatin readouts where claimed;
- sham and matched-dose controls;
- declared falsification window.

Falsification / revision triggers:

- RNA response is claimed before plausible driver or signaling change;
- response matches sham;
- timing contradicts mechanism;
- no downstream response despite confirmed driver when response is required by the claim.

Default status:

`research_hypothesis`.

## H4 — Modality equivalence

Claim under test:

Two or more modalities tuned to produce comparable internal driver trajectories may produce statistically equivalent downstream biological responses within prespecified bounds.

Required evidence:

- modality-specific kernel definitions;
- iso-driver calibration;
- equivalence margin;
- endpoint definition;
- statistical plan;
- modality-specific artifact controls.

Falsification / revision triggers:

- modalities produce non-equivalent driver trajectories;
- equivalence fails within the prespecified bound;
- modality-specific artifact explains the effect;
- equivalence is inferred without driver matching.

Default status:

`research_hypothesis`.

## H5 — Mechanism gating

Claim under test:

If a pathway is claimed to operate through a specific channel, construct, absorber, thermal route, or mechanosensitive route, a targeted blocker or matched control should alter the response while non-target controls should not.

Required evidence:

- mechanism-specific blocker or control;
- sham exposure;
- matched-dose control;
- endpoint readout;
- statistical plan;
- failure condition.

Falsification / revision triggers:

- targeted blocker does not alter response;
- non-targeted blocker has the same effect;
- matched artifact control reproduces response;
- claimed mechanism lacks a specific intervention or readout.

Default status:

`research_hypothesis`.

## 6. Unsupported claims are not hypotheses here

The following are excluded mechanism claims, not FCBCP hypotheses:

- phantom-DNA fields;
- semantic wave-texts;
- DNA inductors;
- DNA speakers/microphones;
- holographic gene lasers;
- native DNA biological magnets;
- mechanism by geometric resemblance.

They may appear only as negative fixtures or historical claim-boundary discussion.

## 7. Human Protection Layer

No hypothesis authorizes human actuation or human-derived export.

Every hypothesis output must carry:

```yaml
evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
hpl_status: string
policy_decision: allow | deny | block | needs_review
human_actuation: blocked_by_default
raw_private_evidence_export: blocked_by_default
```
