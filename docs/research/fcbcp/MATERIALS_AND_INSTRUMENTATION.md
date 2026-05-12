# FCBCP materials and instrumentation scaffold

Status: research scaffold. Not a bill of materials for human-contact deployment and not an implementation authorization.

Owner: `SocioProphet/human-digital-twin`.

Related:

- `docs/research/fcbcp/FCBCP_SPEC_V1.md`
- `docs/research/fcbcp/TRUEMAN_MESH_PROFILE.md`
- `docs/research/fcbcp/BIOLOGICAL_MECHANISM_SPINE.md`
- `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md`

## 0. Purpose

This document captures the materials and instrumentation concepts from the source dossier as research components that can support simulation, phantom calibration, ex vivo study design, and forensic provenance.

No item in this document authorizes human-contact use. Any person-specific or human-contact path remains blocked by default and requires external review.

## 1. Surface tile scaffold

Research role:

- boundary impedance characterization;
- modeled or phantom surface coupling;
- vibrometry or pressure proxy measurement;
- local voltage/current/open-circuit measurement;
- forensic logging of calibration state.

Example scaffold terms:

- PVDF-PCNT composite layer;
- conductive tape/electrode layers;
- insulating substrate such as Kapton;
- spacer geometry;
- readout resistor and open-circuit voltage path;
- co-located EIS and vibrometry channels.

Required boundary:

```yaml
surface_tile:
  context: simulation | synthetic | phantom | ex_vivo | reviewed_external_process
  human_contact: blocked_by_default
  calibration_required: true
  measurement_only_default: true
  actuator_default: disabled
  provenance_required: true
```

## 2. Carbon nanotube / conductive composite notes

Research role:

- improve conductivity or sensitivity of sensor composites;
- support impedance, strain, or pressure-proxy readouts;
- tune material response in phantom or ex vivo fixtures.

Boundary:

Conductive composites are materials research components. They do not imply safe human-contact deployment or biological control. Any biological exposure requires separate toxicology, biocompatibility, containment, and review not provided by this repo.

## 3. Mesoporous silica and porous carrier notes

Research role:

- optical absorption/scattering studies;
- photothermal or photoacoustic kernel characterization;
- controlled release or cargo-loading concept discussions;
- phantom or ex vivo material calibration.

Boundary:

Porous carrier concepts must not be treated as human therapy, delivery, or exposure protocol. They may appear in research planning with explicit context and evidence tier.

## 4. Magnetic / magnetothermal particle notes

Research role:

- magnetothermal kernel modeling;
- magnetomechanical route modeling when particles/constructs are explicitly declared;
- phantom calibration of SAR or thermal response;
- material-batch provenance and safety modeling.

Boundary:

Magnetic-particle routes require declared particles or constructs. They must not be replaced by native-DNA biological magnet claims. Human exposure is blocked by default.

## 5. Native mass spectrometry and chemistry verification

Research role:

- verify ligand, construct, or material state;
- preserve batch identity;
- hash raw spectra or derived signatures;
- establish chemistry provenance for ex vivo or phantom studies.

Boundary:

Chemistry verification can support evidence tiering. It does not itself validate biological mechanism or human-contact safety.

## 6. Instrumentation evidence records

All materials and instruments should emit provenance records:

```yaml
instrumentation_record:
  batch_id: string
  device_id: string
  calibration_hash: string
  material_class: string
  context: simulation | synthetic | phantom | ex_vivo | reviewed_external_process
  measured_properties:
    electrical: optional
    thermal: optional
    optical: optional
    acoustic: optional
    magnetic: optional
  safety_notes: string
  evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
  policy_status: string
```

## 7. Required measurements before use in research profiles

Minimum measurement categories:

- impedance response;
- thermal response under modeled input;
- mechanical/acoustic response where relevant;
- optical absorption/scattering where relevant;
- magnetic/SAR response where relevant;
- stability and calibration drift;
- contamination/biocompatibility notes where biological contact is proposed externally.

## 8. Human Protection Layer constraints

Blocked by default:

- human-contact material deployment;
- raw physiological telemetry export;
- uncontrolled device actuation;
- material claims without calibration;
- native-DNA magnet/inductor/speaker substitutions;
- hidden or undeclared instrumentation authority.

Allowed by default:

- documentation;
- simulation;
- synthetic fixture;
- phantom fixture;
- ex vivo research description;
- provenance schema design;
- negative tests.

## 9. Relationship to Trueman Mesh

Trueman Mesh may reference materials and instrumentation only through declared profiles:

```text
material/instrument record
  -> calibration and provenance
  -> HSP-Map transfer estimate
  -> FCBCP simulation or research profile
  -> verifier / ledger
  -> HDT evidence claim or block
```

There is no direct path from a material record to human actuation.

## 10. Required future fixtures

- synthetic PVDF-PCNT tile calibration record;
- phantom impedance sweep fixture;
- material batch provenance fixture;
- magnetothermal particle record with human-contact blocked;
- optical carrier record with mechanism declared but no therapeutic claim;
- negative fixture where DNA-inductor substitution is rejected.
