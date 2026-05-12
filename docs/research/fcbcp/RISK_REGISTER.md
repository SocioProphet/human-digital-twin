# FCBCP risk register scaffold

Status: research risk scaffold. Not a safety certification.

Owner: `SocioProphet/human-digital-twin`.

## 0. Purpose

This register captures the main FCBCP risks and required mitigations. It is intentionally conservative: unresolved safety, consent, mechanism, or misuse risk blocks promotion.

## 1. Risk classes

| Risk class | Description | Default status |
|---|---|---|
| physical_safety | risk to body or tissue | blocked unless reviewed |
| privacy | raw/private evidence risk | blocked by default for export |
| consent_autonomy | missing or inadequate consent | blocked |
| cognitive_safety | manipulation, hidden persuasion, sensitive inference | blocked or needs review |
| mechanism_overclaim | unsupported mechanism promoted as validated | blocked |
| statistical_underpower | inadequate design or endpoint model | underidentified |
| materials_safety | unreviewed materials or constructs | blocked for human contact |
| instrumentation_authority | undeclared sensing/actuation authority | blocked |
| misuse | surveillance, coercive profiling, unsafe automation | blocked or needs review |
| publication_boundary | public/private/redaction error | needs review |

## 2. Seed risks

### R1 — Tissue attenuation smaller/larger than assumed

Risk:

Boundary-transfer and tissue-coupling estimates may be wrong, making schedules ineffective or unsafe.

Mitigation:

- require transfer residuals;
- carry uncertainty;
- use phantom/synthetic calibration;
- block human actuation by default;
- mark underidentified when transfer is uncertain.

### R2 — Stratum corneum / boundary breakdown or contact artifact

Risk:

Surface conditions, contact impedance, hydration, or breakdown can invalidate transfer assumptions.

Mitigation:

- impedance measurement;
- contact-condition logging;
- conservative caps;
- no human-contact authorization;
- artifact controls.

### R3 — Thermal accumulation

Risk:

Long-horizon or repeated exposure can accumulate heat even when instantaneous caps appear safe.

Mitigation:

- stateful thermal model;
- cumulative dose cap;
- duty cycle limits;
- thermal observations where relevant;
- block missing thermal model.

### R4 — Modality artifact confounding

Risk:

Photothermal, photoacoustic, mechanical, electrical, and chemical effects may be conflated.

Mitigation:

- matched-dose controls;
- non-absorbing wavelength controls;
- sham controls;
- modality-specific blockers;
- declare mechanism uncertainty.

### R5 — Mechanism overclaim

Risk:

Metaphor or unsupported mechanism is promoted as validated science.

Mitigation:

- Claim Boundary Register;
- negative fixtures;
- evidence-tier labels;
- HPL claim-boundary gate.

### R6 — Human actuation creep

Risk:

Simulation or research schedule is misread as a protocol for human-contact hardware.

Mitigation:

- human_actuation: blocked_by_default;
- simulation-only fixture labels;
- external review requirement;
- no runtime/hardware code in this repo;
- tests proving blocked status.

### R7 — Raw physiological telemetry export

Risk:

Person-specific raw observations become a shadow dossier or are exported without consent/minimization.

Mitigation:

- raw_private_evidence_export: blocked_by_default;
- minimal claim envelope;
- consent scope;
- redress/revocation path;
- local/private default.

### R8 — Statistical underpower or endpoint drift

Risk:

Biological conclusions are drawn from arbitrary sample counts, uncontrolled endpoints, or post hoc analysis.

Mitigation:

- endpoint-specific statistical plan;
- power/effect-size priors;
- preregistration where relevant;
- FDR/equivalence controls;
- underidentified status when missing.

### R9 — Materials and biocompatibility uncertainty

Risk:

Materials suitable for phantom instrumentation are incorrectly treated as safe for biological or human contact.

Mitigation:

- material provenance;
- context labels;
- no human-contact authorization;
- separate material safety review.

### R10 — Misuse as surveillance or coercive profiling

Risk:

HSP-Map/FCBCP-derived data could be misused for identification, inference, targeting, or coercive intervention.

Mitigation:

- privacy/minimization gate;
- cognitive safety gate;
- misuse review;
- blocked export of raw data;
- redress and challenge path.

## 3. Risk envelope

Every FCBCP research artifact should include:

```yaml
risk:
  classes: [string]
  severity: low | medium | high | critical | unknown
  status: accepted | mitigated | blocked | needs_review | underidentified
  mitigations: [string]
  hpl_status: string
  evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
```

## 4. Promotion rule

High or critical risk cannot be promoted from research-only to operational profile inside this repo.

Any future operational work must live behind external review and policy authority.
