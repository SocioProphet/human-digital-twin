# Field-Coupled Bioelectronic Control Plane (FCBCP) v1 — research specification

Status: research-only specification. Not a human-actuation runtime. Not a therapeutic, diagnostic, or device-control implementation.

Owner: `SocioProphet/human-digital-twin`.

Protection doctrine: this profile is subject to `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md` and the upstream ProCybernetica Human Protection Layer and Claim Boundary Register.

## 0. Position

FCBCP is captured here as a falsifiable research profile for modeling boundary-coupled energy-to-state pathways in tissue systems. It is not an authorization to stimulate, actuate, treat, diagnose, or otherwise intervene on a human.

Allowed by default:

- documentation;
- schemas;
- toy/simulation models;
- synthetic fixtures;
- phantom fixtures;
- ex vivo research protocol descriptions;
- safety-envelope validation;
- negative tests for unsupported mechanisms.

Blocked by default:

- human actuation;
- uncontrolled human-contact protocols;
- raw physiological telemetry export;
- unsupported wave-genetics mechanisms;
- autonomous high-impact decisions about a person.

## 1. System definition

The Field-Coupled Bioelectronic Control Plane is a closed-loop research architecture that models how exterior energy modalities may couple through a calibrated boundary into lawful biological state variables.

A complete FCBCP research instance contains five components:

1. `tissue_model`: per-region, per-subject, age-adjusted model of layered dielectric, thermal, optical, acoustic, and microstructural properties.
2. `surface_array`: addressable research tiles capable of modeled actuation and concurrent sensing in simulation, phantom, or explicitly reviewed research contexts.
3. `state_observer`: estimator for latent biological and physical state variables from sensor returns and explicit model assumptions.
4. `compiler_scheduler`: robust scheduler that produces simulation or research-only waveform/program schedules under safety and policy constraints.
5. `verifier_ledger`: safety verifier and forensic ledger for every modeled or measured event.

## 2. Unified state-space spine

A research model may represent a local tissue parcel by state variables such as:

- `Vm`: membrane potential or membrane-polarization proxy;
- `C`: second-messenger vector, such as calcium-related proxies when explicitly measured;
- `R`: RNA/transcript vector or transcript proxy;
- `P`: protein/channel/proxy vector;
- `D`: chromatin or epigenetic accessibility proxy.

The conceptual cascade is:

```text
external field / modality
  -> boundary transfer
  -> internal driver
  -> membrane or mechanical/thermal/photochemical state
  -> second messengers
  -> transcriptional response
  -> protein/channel response
  -> slower chromatin/tissue adaptation
```

This cascade is a research model, not a guarantee. Each link must be validated for the declared tissue, modality, dose, timing, and readout.

## 3. Modality kernels

FCBCP treats modalities as transfer kernels into internal driver variables. Kernels are separately declared, separately validated, and separately safety-gated.

| Modality | Applied field | Internal driver | Required boundary |
|---|---|---|---|
| Electric | external electric field / contact potential | membrane polarization / current proxy | surface impedance, transfer function, rate/amplitude caps |
| Acoustic / ultrasound | pressure field | membrane tension, mechanotransduction proxy | acoustic intensity, MI-like safety proxy, thermal proxy |
| Optical | fluence / wavelength | photothermal, photoacoustic, photochemical, opsin/construct route if present | optical absorption/scattering, thermal model, wavelength controls |
| Thermal | temperature field | temperature-gated channel/protein dynamics | Pennes-style or equivalent heat model, cumulative thermal dose |
| Magnetic + particles | magnetic field with declared particles/constructs | magnetothermal or magnetomechanical route | particle inventory, SAR/thermal model, construct-specific mechanism |

No modality is accepted by name alone. Each requires a declared mechanism, safety envelope, and evidence tier.

## 4. Boundary closure

FCBCP uses boundary accounting as the physical closure principle.

Required model elements:

- boundary/interface definition;
- impedance or transfer model;
- power/energy accounting;
- uncertainty estimate;
- safety caps;
- policy status.

For electromagnetic descriptions, Poynting-flux accounting and surface-equivalent source language may be used as modeling constructs. They do not imply that the surface is literally identical to the interior; they define how exterior fields are represented and audited under declared assumptions.

## 5. Corrected feasibility assumptions

The research profile preserves the following corrections:

1. Isolated-cell coupling formulas do not directly transfer to intact tissue without attenuation and coupling factors.
2. Tissue shielding, gap-junction coupling, tortuosity, extracellular paths, and local geometry can materially reduce internal coupling.
3. Stratum corneum behavior, contact impedance, hydration, and dielectric breakdown constraints matter.
4. Sub-MHz biological coupling should not be explained by classical metallic skin-depth alone; dispersive impedance and Maxwell-Wagner-style layer contrast are central.
5. Single-pole Debye models are too coarse for predictive HSP-Map work; Cole-Cole-style multi-relaxation tissue models are preferred.
6. DNA/RNA/computer language is taxonomy/metaphor unless rewritten as biochemical kinetics and validated mechanism.
7. MPC or scheduler models require explicit thermal accumulation and cumulative dose constraints.
8. Sample-count heuristics are not power analysis; endpoint-specific statistical plans are required.

## 6. Safety and policy constraints

Every FCBCP profile must carry explicit constraints:

```yaml
safety_constraints:
  human_actuation: blocked_by_default
  simulation_allowed: true
  phantom_allowed: true
  ex_vivo_allowed: protocol_required
  in_vivo_or_human_contact: external_review_required
  dose_model_required: true
  thermal_model_required: true
  runtime_monitor_required_for_real_world_path: true
  emergency_stop_required_for_real_world_path: true
  raw_private_evidence_export: blocked_by_default
```

The default status for any FCBCP human-contact program is:

```text
BLOCKED_HUMAN_ACTUATION
```

until an external ethics/regulatory/safety review path is explicitly recorded outside this repository.

## 7. MPC / scheduler profile

A scheduler may be documented or simulated, but it must not control real human-contact hardware from this repository.

Minimum scheduler constraints:

- membrane-polarization cap or driver cap;
- temperature ceiling;
- cumulative thermal dose or equivalent dose integral;
- acoustic/mechanical safety proxy if applicable;
- SAR or EM power proxy if applicable;
- allowed frequency/wavelength/band limits;
- duty-cycle limits;
- uncertainty margin;
- policy admission state;
- evidence tier.

A scheduler output is a research artifact unless separately reviewed.

## 8. Forensic ledger profile

Every modeled, simulated, phantom, ex vivo, or reviewed real-world event should emit an append-only event record.

Minimum fields:

```yaml
session_id: string
program_id: string
block_id: string
tile_id: string
sensor_id: string
t_iso8601_utc: string
region_id: string
modality: E | US | Opt | Therm | MagMNP
stimulus:
  f_hz: optional
  amplitude: optional
  phase: optional
  duty: optional
  lambda_nm: optional
  fluence_Jcm2: optional
  MI: optional
  H_Am: optional
observations:
  Z_mag: optional
  Z_phase: optional
  T_obs: optional
  p_obs: optional
  V_oc: optional
  I_obs: optional
  Phi_obs: optional
estimates:
  Vm_est_mV: optional
  Ca_est: optional
  R_proxy: optional
  P_proxy: optional
  D_proxy: optional
safety_flags:
  dVm_violated: boolean
  SAR_violated: boolean
  MI_violated: boolean
  dT_violated: boolean
policy:
  policy_version: string
  hpl_status: string
hashes:
  compiler_hash: string
  estimator_hash: string
  verifier_hash: string
  record_hash: string
  prev_hash: string
```

## 9. Binding exclusions

FCBCP excludes the following as validated mechanisms:

- phantom-DNA fields;
- persistent post-DNA-removal field imprints;
- semantic language reading by DNA or chromatin;
- DNA, nucleosomes, or RNA acting as lumped inductors, loudspeakers, microphones, or laser gain media in vivo;
- mechanism inferred from geometric resemblance alone;
- native DNA as a biological magnet absent engineered ferromagnetic or superparamagnetic construct;
- semantic wave-texts or unreplicated wave-genetics mechanisms.

These claims may appear only as excluded claims, historical review, or metaphor-only discussion under the Claim Boundary Register.

## 10. Research claims and non-claims

FCBCP may claim and test:

- frequency-selective boundary coupling under declared assumptions;
- lawful membrane or physical driver coupling under safety caps;
- lagged biological cascades from fast physical state to slower transcripts/proteins;
- modality-equivalence hypotheses when iso-driver trajectories are experimentally demonstrated;
- closed-loop controllability in simulation, phantom, or reviewed research contexts.

FCBCP does not claim:

- human actuation safety;
- therapeutic effect;
- diagnostic validity;
- semantic wave-genetics;
- DNA/RNA/chromatin as in-vivo circuit elements;
- validated control of transcription from exterior fields without experiment;
- replacement of human consent or agency by a digital twin.

## 11. Relationship to HDT and Atlas

Canonical relation:

```text
FCBCP research event
  -> FCBCP safety/audit result
  -> HDT evidence claim
  -> Ω evaluation
  -> Human Protection Layer gate
  -> policy decision
  -> minimal export or block
```

There is no direct path from FCBCP simulation validity to human export or action.

## 12. Next implementation work

- Add HSP-Map schema.
- Add Trueman Mesh simulation-only profile.
- Add validated precursor document.
- Add biological mechanism spine.
- Add negative mechanism fixtures/tests.
- Add FCBCP research-session schema after reconciliation stabilizes field names.
