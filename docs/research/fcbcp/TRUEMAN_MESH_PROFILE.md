# Trueman Mesh — simulation-only research profile

Status: simulation/research profile. Not a runtime authorization layer. Not a hardware-control implementation.

Owner: `SocioProphet/human-digital-twin`.

Related:

- `docs/research/fcbcp/FCBCP_SPEC_V1.md`
- `docs/research/fcbcp/HSP_MAP_SPEC.md`
- `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md`

## 0. Purpose

Trueman Mesh is the FCBCP planning vocabulary for turning a declared research objective into a simulated, safety-checked, evidence-producing schedule.

It is not a permission system. It cannot authorize human actuation. It cannot bypass the Human Protection Layer. It cannot convert research hypotheses into validated biological claims.

## 1. Control-plane decomposition

A Trueman Mesh profile has six layers.

### 1.1 Intent layer

Defines the objective, scope, subject class, evidence tier, and allowed context.

```yaml
intent:
  objective_kind: Vm_proxy | transcript_proxy | calibration | phantom | ex_vivo | other
  target_region: string
  horizon_s: number
  evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
  allowed_context: simulation | synthetic | phantom | ex_vivo | reviewed_external_process
```

### 1.2 Compiler

Maps the intent and HSP-Map transfer estimates into candidate schedules.

Compiler outputs are simulation artifacts unless separately reviewed.

### 1.3 Scheduler

Orders blocks over time. The scheduler must preserve duty caps, rest windows, dose margins, and policy status.

### 1.4 Estimator

Consumes modeled or measured observations to update state estimates and uncertainty.

### 1.5 Verifier

Checks safety invariants, Human Protection Layer gates, claim boundary, and profile status.

### 1.6 Forensic logger

Emits append-only evidence records with hashes, policy version, and blocked/allowed status.

## 2. Program grammar

Seed grammar for simulation-only profiles:

```yaml
program:
  header:
    name: string
    target: string
    objective: string
    horizon_s: number
    context: simulation | synthetic | phantom | ex_vivo
  policy:
    human_actuation: blocked_by_default
    evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
    safety_caps: {}
  blocks:
    - kind: WAVE | SWEEP | PULSE | QUIET | MEASURE | CALIBRATE
      region: string
      duration_s: number
      parameters: {}
      safety: {}
      policy_status: string
```

No block kind implies permission to control real hardware.

## 3. Allowed default contexts

Allowed by default:

- simulation;
- synthetic fixture;
- phantom fixture;
- ex vivo protocol description;
- replay of public-safe synthetic data;
- negative-test fixture.

Blocked by default:

- human actuation;
- live human-contact hardware control;
- autonomous schedule execution;
- export of raw physiological telemetry;
- schedules based on excluded mechanisms;
- high-impact output without redress.

## 4. Safety constraints

Every program must declare:

```yaml
safety:
  dVm_cap_mV: optional
  thermal_cap_C: optional
  cumulative_thermal_dose_cap: optional
  SAR_cap_Wkg: optional
  MI_cap: optional
  duty_cap: optional
  band_limits: optional
  uncertainty_margin: required
  human_actuation: blocked_by_default
```

A missing safety constraint does not mean unconstrained. It means blocked or underidentified.

## 5. Policy status

Every program and block must carry a policy status.

Recommended statuses:

- SAFE_TO_SIMULATE;
- SAFE_FOR_SYNTHETIC_TEST;
- SAFE_FOR_PHANTOM_TEST;
- SAFE_FOR_EX_VIVO_RESEARCH;
- REQUIRES_ETHICS_REVIEW;
- REQUIRES_REGULATORY_REVIEW;
- BLOCKED_HUMAN_ACTUATION;
- BLOCKED_UNSUPPORTED_CLAIM;
- BLOCKED_PRIVACY_RISK;
- BLOCKED_UNDERIDENTIFIED;
- SPECULATIVE_ONLY.

## 6. Claim-boundary enforcement

A Trueman Mesh program may not use excluded mechanisms as operative assumptions.

Blocked mechanism labels include:

- phantom_dna_field;
- semantic_wave_text;
- dna_inductor;
- dna_speaker_microphone;
- holographic_gene_laser;
- native_dna_biological_magnet;
- geometry_implies_circuit_element;
- unreplicated_field_genetics_mechanism.

Allowed metaphor-only labels must remain labeled as metaphor and cannot drive compiler decisions.

## 7. Forensic telemetry shape

Every simulation or research event should emit:

```yaml
event:
  session_id: string
  program_id: string
  block_id: string
  t_iso8601_utc: string
  region_id: string
  context: simulation | synthetic | phantom | ex_vivo | reviewed_external_process
  modality: E | US | Opt | Therm | MagMNP | Measure | Calibrate
  stimulus: {}
  observations: {}
  estimates: {}
  safety_flags: {}
  hpl_status: string
  policy_decision: allow | deny | block | needs_review
  hashes:
    compiler_hash: string
    verifier_hash: string
    record_hash: string
    prev_hash: string
```

## 8. Example simulation-only program

```yaml
program:
  header:
    name: vm_to_rna_proxy_research_fixture_v0
    target: synthetic_forearm_patch
    objective: transcript_proxy_research
    horizon_s: 7200
    context: simulation
  policy:
    human_actuation: blocked_by_default
    evidence_tier: E2
    status: SAFE_TO_SIMULATE
  blocks:
    - kind: CALIBRATE
      region: synthetic_forearm_patch
      duration_s: 300
      parameters:
        measurement: impedance_sweep
      policy_status: SAFE_TO_SIMULATE
    - kind: WAVE
      region: synthetic_forearm_patch
      duration_s: 1200
      parameters:
        frequency_hz: symbolic
        amplitude: auto_by_safety_cap
      safety:
        dVm_cap_mV: 0.5
        thermal_cap_C: required
      policy_status: SAFE_TO_SIMULATE
    - kind: QUIET
      region: synthetic_forearm_patch
      duration_s: 1800
      parameters:
        measurement_window: true
      policy_status: SAFE_TO_SIMULATE
```

This fixture is for simulation and schema validation only. It must not be interpreted as a human protocol.

## 9. Relationship to Superconscious

Superconscious may propose or reason over Trueman Mesh programs, but may not authorize them.

Canonical relation:

```text
Superconscious task decomposition
  -> HPLScope.assessed
  -> candidate Trueman Mesh simulation profile
  -> policy admission request
  -> safe trace / replay plan
  -> block or downstream review
```

## 10. Required tests

- Program cannot omit policy status.
- Program cannot mark human actuation as allowed by default.
- Excluded mechanisms cannot appear in compiler assumptions.
- Missing safety caps produce `BLOCKED_UNDERIDENTIFIED` or `needs_review`.
- Simulation-safe status cannot be upgraded to human-contact status without external review record.
- Superconscious planning trace cannot authorize a Trueman Mesh program.
