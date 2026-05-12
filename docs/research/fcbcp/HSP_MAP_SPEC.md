# Human Surface-Penetration Map (HSP-Map) — research specification

Status: research-only specification. Not a diagnostic model, not a treatment model, and not a human-actuation authority.

Owner: `SocioProphet/human-digital-twin`.

Protection doctrine: subject to `docs/HUMAN_PROTECTION_LAYER_ADOPTION.md`, FCBCP research boundaries, and the ProCybernetica Claim Boundary Register.

## 0. Purpose

The HSP-Map is a research atlas for representing region-specific boundary and tissue properties relevant to modeled field, thermal, optical, acoustic, and sensor-transfer behavior.

It exists to support simulation, safety analysis, synthetic/phantom fixtures, and carefully reviewed research designs. It must not be used to infer, diagnose, treat, or actuate a human without external review and consent/policy gates.

## 1. Model primitive

An HSP-Map entry is a region-scoped composite bio-feature vector.

```yaml
hsp_map_entry:
  region_id: string
  region_name: string
  subject_scope: synthetic | phantom | ex_vivo | individual | population
  evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
  geometry: {}
  dielectric: {}
  thermal: {}
  optical: {}
  acoustic: {}
  microstructure: {}
  lumped_fit: {}
  transfer: {}
  coupling: {}
  age_scalars: {}
  safety_caps: {}
  provenance: {}
  policy:
    human_actuation: blocked_by_default
    raw_private_evidence_export: blocked_by_default
```

## 2. Region partition

Seed 18-region partition:

1. scalp;
2. forehead_face;
3. neck;
4. anterior_chest;
5. back;
6. upper_arm;
7. forearm;
8. palm;
9. dorsal_hand;
10. fingertips;
11. abdomen;
12. lower_back_flank;
13. thigh;
14. knee_patella;
15. calf;
16. sole;
17. dorsal_foot_ankle;
18. perineum_axilla.

This partition is a modeling scaffold. It is not a claim that these regions are sufficient for all anatomy or all persons.

## 3. Geometry fields

```yaml
geometry:
  d_SC_m: number
  d_epi_m: number
  d_derm_m: number
  d_fat_m: number
  d_muscle_m: number
  d_bone_m: number
  area_m2: optional
  uncertainty_cov: optional
```

All geometry fields must be explicit about source: measured, literature-derived, synthetic, phantom, or inferred.

## 4. Dielectric fields

Predictive use should prefer layered multi-relaxation / Cole-Cole style models over single-pole Debye approximations.

```yaml
dielectric:
  layers:
    - SC
    - epidermis
    - dermis
    - fat
    - muscle
    - bone
  per_layer:
    SC:
      eps_inf: number
      sigma_s: number
      cole_cole_terms:
        - delta_eps: number
          tau_s: number
          alpha: number
        - delta_eps: number
          tau_s: number
          alpha: number
        - delta_eps: number
          tau_s: number
          alpha: number
        - delta_eps: number
          tau_s: number
          alpha: number
```

Frequency-dependent material properties must not be compressed into a single universal penetration number.

## 5. Thermal fields

```yaml
thermal:
  rho_kg_m3: number
  c_J_kgK: number
  k_W_mK: number
  omega_blood: optional
  T_baseline_C: number
  perfusion_model: optional
  uncertainty_cov: optional
```

Thermal accumulation must be stateful when long-horizon schedules are modeled.

## 6. Optical fields

```yaml
optical:
  wavelength_range_nm: [400, 1300]
  table:
    - lambda_nm: number
      mu_a_mm_inv: number
      mu_s_prime_mm_inv: number
      g: number
  source: measured | literature | synthetic | phantom
```

Optical fields require separation of photothermal, photoacoustic, photochemical, and construct-specific paths.

## 7. Acoustic fields

```yaml
acoustic:
  rho_ac_kg_m3: number
  c_m_s: number
  alpha_by_frequency: []
  Z_ac: number
  source: measured | literature | synthetic | phantom
```

Acoustic and ultrasound kernels must use tissue-scale mechanotransduction and acoustic dose models, not DNA speaker/microphone claims.

## 8. Microstructure fields

```yaml
microstructure:
  ducts_per_cm2: optional
  hair_density_cm2: optional
  roughness_rms_m: optional
  hydration_pct: optional
  sebum_or_surface_state: optional
  contact_condition: optional
```

These fields are sensitive and should be treated as private when person-specific.

## 9. Lumped fit and transfer fields

```yaml
lumped_fit:
  R_SC_ohm: optional
  C_SC_F: optional
  R_deep_ohm: optional
  W_warburg: optional
  uncertainty_cov: optional

transfer:
  T_omega:
    - f_hz: number
      magnitude: number
      phase_rad: number
  fit_status: measured | modeled | synthetic | phantom
  residual: optional
```

The transfer function is an estimate with uncertainty, not a guarantee of internal biological effect.

## 10. Coupling fields

```yaml
coupling:
  kappa_tiss_omega:
    - f_hz: number
      value: number
      uncertainty: optional
  cell_radius_distribution_m: optional
  membrane_filter_model: optional
  tissue_attenuation_model: optional
```

Isolated-cell formulas must be treated as insufficient for intact tissue unless a tissue attenuation/coupling model is declared.

## 11. Age and population scalars

```yaml
age_scalars:
  alpha_dSC: optional
  alpha_eps_SC: optional
  alpha_sigma_muscle: optional
  alpha_dfat: optional
  alpha_hydration: optional
  alpha_perfusion: optional
  class: neonate | child | adult | older_adult | unknown
```

Age scalars are priors, not person-level truth. Person-specific use requires consent, minimization, and provenance.

## 12. Safety caps

```yaml
safety_caps:
  dVm_max_mV: optional
  SAR_Wkg: optional
  MI_max: optional
  dT_max_C: optional
  Omega_max: optional
  duty_max: optional
  band_limits: optional
  human_actuation: blocked_by_default
```

Safety caps are required for simulation and research protocols. They do not authorize real-world actuation.

## 13. Provenance fields

```yaml
provenance:
  measurement_dates: []
  device_ids: []
  calibration_hashes: []
  source_refs: []
  evidence_hash: string
  consent_receipt_ref: optional
  policy_version: string
```

Person-specific HSP-Map data is private by default.

## 14. Design-band heuristics

Design-band heuristics must be declared as heuristics, not universal law.

Seed bands:

- 0-10 Hz: calibration / impedance characterization emphasis;
- 10-500 Hz: membrane-band modeling candidate under explicit transfer and safety constraints;
- 0.5-100 kHz: bulk electrokinetic / impedance-imaging style modeling, dose-gated;
- above 100 kHz to MHz: diagnostic or displacement-current regimes, tightly dose-gated.

These bands require tissue, region, contact, and endpoint-specific validation.

## 15. Human Protection Layer constraints

HSP-Map entries involving people must evaluate:

- consent scope;
- raw private evidence export status;
- evidence tier;
- redress path;
- policy status;
- human actuation block;
- unsupported mechanism block.

Default status for person-specific maps:

```text
private_local_only unless consented minimal export is explicitly allowed
```

## 16. Relationship to FCBCP

HSP-Map provides the tissue/boundary atlas consumed by FCBCP simulations and research profiles.

Canonical relation:

```text
HSP-Map entry
  -> transfer/coupling estimate
  -> FCBCP safety/audit result
  -> HDT evidence claim
  -> Ω evaluation
  -> HPL gate
  -> minimal export or block
```

There is no direct path from HSP-Map fit to human actuation.
