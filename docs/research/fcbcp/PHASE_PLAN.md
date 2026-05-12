# FCBCP research phase plan

Status: research planning scaffold. Not an active human-subjects protocol and not a device-control plan.

Owner: `SocioProphet/human-digital-twin`.

## 0. Purpose

This phase plan captures the staged FCBCP research program as a sequence of increasingly constrained evidence contexts.

Default rule:

```text
Simulation and documentation are allowed.
Human actuation is blocked by default.
Human-contact or in-vivo work requires an external ethics/regulatory/safety process and is not authorized by this repository.
```

## Phase 0 — Instrumentation and calibration

Context:

- synthetic fixtures;
- phantom fixtures;
- calibration-only records.

Goals:

- define tile/instrumentation records;
- define impedance / thermal / acoustic / optical calibration routines;
- recover known phantom parameters within prespecified tolerance;
- generate forensic calibration hashes.

Pass criteria:

- calibration record emitted;
- uncertainty recorded;
- safety status recorded;
- no human-contact authorization.

Default status:

`SAFE_FOR_SYNTHETIC_TEST` or `SAFE_FOR_PHANTOM_TEST`.

## Phase 1 — HSP-Map acquisition scaffold

Context:

- synthetic population profiles;
- phantom or public/literature-derived priors;
- person-specific data only with consent and privacy controls.

Goals:

- populate HSP-Map schema;
- fit transfer estimates;
- capture age/population priors;
- record provenance.

Pass criteria:

- region schema valid;
- transfer table present;
- uncertainty present;
- consent/policy state present when person-specific;
- raw private evidence not exported by default.

Default status:

`SAFE_TO_SIMULATE` for synthetic data; `private_local_only` for person-specific raw data.

## Phase 2 — Ex vivo or non-human lab validation scaffold

Context:

- ex vivo models;
- 3D spheroids;
- biological readout validation under reviewed lab protocol.

Goals:

- test H2/H3/H4 in controlled settings;
- measure driver proxies;
- measure lagged RNA/protein/secretome outputs;
- distinguish modality-specific artifacts.

Pass criteria:

- endpoint-specific statistical plan;
- sham and matched controls;
- timing metadata;
- evidence tier recorded;
- HPL status recorded.

Default status:

`SAFE_FOR_EX_VIVO_RESEARCH` only when protocol requirements are present.

## Phase 3 — Mechanism gating scaffold

Context:

- ex vivo or reviewed lab context.

Goals:

- test targeted blockers or controls;
- distinguish mechanosensitive, photothermal, photochemical, thermal, electric, and particle-mediated routes;
- reject underidentified mechanism claims.

Pass criteria:

- blocker/control design declared;
- mechanism-specific endpoint declared;
- non-target controls present;
- failure conditions declared.

Default status:

`SAFE_FOR_EX_VIVO_RESEARCH` or `BLOCKED_UNDERIDENTIFIED`.

## Phase 4 — Closed-loop simulation / in vitro research scaffold

Context:

- simulation;
- synthetic/phantom fixtures;
- in vitro or ex vivo research only with reviewed protocol.

Goals:

- implement scenario-MPC or scheduler logic in simulation;
- prove safety invariant checks;
- log forensic records;
- verify no human-actuation path exists.

Pass criteria:

- safety invariants emitted;
- policy status emitted;
- uncertainty margin present;
- no runtime human-contact action.

Default status:

`SAFE_TO_SIMULATE` or reviewed research-only.

## Phase 5 — Human-contact boundary

Context:

- external ethics/regulatory/safety process only.

This repository does not authorize Phase 5.

Any future human-contact work requires:

- independent review;
- informed consent and revocation path;
- physical safety model;
- runtime monitoring;
- emergency stop;
- privacy/minimization plan;
- redress/appeal process;
- external regulatory/ethics documentation;
- explicit separation from this research scaffold.

Default status:

`BLOCKED_HUMAN_ACTUATION` or `REQUIRES_ETHICS_REVIEW` / `REQUIRES_REGULATORY_REVIEW`.

## Phase-gate summary

| Phase | Allowed default | Blocked default |
|---|---|---|
| 0 | synthetic/phantom calibration | human-contact deployment |
| 1 | synthetic HSP-Map, consented local person-specific modeling | raw private export |
| 2 | ex vivo under protocol | human inference/export without policy |
| 3 | mechanism-gating under protocol | unsupported mechanism promotion |
| 4 | closed-loop simulation | live human actuation |
| 5 | external reviewed process only | repo-authorized human actuation |
