# FCBCP statistical plan scaffold

Status: research planning scaffold. Not a completed preregistration.

Owner: `SocioProphet/human-digital-twin`.

## 0. Purpose

This document captures the statistical discipline required before FCBCP research claims can be promoted beyond conceptual or simulation status.

The key rule:

```text
sample-count heuristics are not power analysis.
```

Calibration grids may use fixed frequency-amplitude designs for identifiability, but biological endpoints require endpoint-specific statistical plans.

## 1. Design separation

### Calibration / identifiability grids

A 6x6 frequency-amplitude grid may be used for calibration, persistent excitation, transfer estimation, or synthetic/phantom fixture coverage.

This does not establish biological efficacy or safety.

### Biological endpoint studies

Biological endpoints require:

- endpoint definition;
- effect-size prior;
- variance model;
- sample-size calculation;
- randomization/blocking plan;
- sham/control definition;
- equivalence or superiority plan;
- multiple-comparison plan;
- missing-data plan;
- preregistration or protocol reference.

## 2. Primary model classes

Recommended model families:

- linear mixed-effects models;
- generalized mixed-effects models;
- hierarchical Bayesian models where priors are explicit;
- TOST equivalence testing for modality equivalence;
- FDR correction for transcript panels;
- time-series or state-space models for repeated timepoint data.

Subject, site, batch, region, and run should be random effects where applicable.

## 3. Hypothesis mapping

| Hypothesis | Statistical requirement |
|---|---|
| H1 boundary transparency | transfer residual model with uncertainty and prespecified tolerance |
| H2 driver linearity | slope/linearity model across frequency-amplitude grid with residual checks |
| H3 cascade lag | time-ordered model with driver, second messenger, RNA, protein, and controls |
| H4 modality equivalence | TOST or equivalent model with prespecified equivalence margin |
| H5 mechanism gating | interaction model showing targeted blocker effect differs from non-target control |

## 4. Required metadata

```yaml
statistical_plan:
  endpoint: string
  hypothesis: H1 | H2 | H3 | H4 | H5 | other
  context: simulation | synthetic | phantom | ex_vivo | reviewed_external_process
  effect_size_prior: string
  alpha: optional
  power_target: optional
  equivalence_margin: optional
  random_effects: [string]
  fixed_effects: [string]
  multiple_comparison_plan: string
  missing_data_plan: string
  preregistration_ref: optional
  evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
  hpl_status: string
```

## 5. Failure conditions

A result should not be promoted when:

- sample size is arbitrary or unexplained;
- endpoint was changed after seeing data without disclosure;
- no sham or matched controls exist;
- multiple comparisons are uncorrected;
- equivalence is claimed from non-significance;
- mechanism is inferred without blocker/control data;
- raw private data export is required for review;
- human-contact context lacks external review.

## 6. Human Protection Layer

Statistical strength does not override consent, privacy, physical safety, cognitive safety, redress, or policy status.

A strong statistical result can still be blocked from export or action.
