# Biological mechanism spine for FCBCP

Status: research mechanism scaffold. Not a validated therapeutic or diagnostic pathway.

Owner: `SocioProphet/human-digital-twin`.

Related:

- `docs/research/fcbcp/FCBCP_SPEC_V1.md`
- `docs/research/fcbcp/VALIDATED_PRECURSORS.md`
- `docs/research/fcbcp/WAVE_GENETICS_CLAIM_BOUNDARY.md`
- `docs/research/fcbcp/TIME_SCALE_LADDER.md`

## 0. Purpose

This document captures the lawful biological spine FCBCP may use for research modeling:

```text
boundary-coupled driver
  -> membrane / mechanical / thermal / photochemical state
  -> ion-channel or sensor pathway
  -> second messengers
  -> transcription factors
  -> RNA response
  -> protein/channel response
  -> chromatin/tissue adaptation
```

Every arrow is a hypothesis unless measured or otherwise validated for the declared context.

## 1. Core state variables

Seed state variables:

```yaml
state:
  Vm: membrane potential or membrane-polarization proxy
  C: second-messenger vector, e.g. calcium proxy when measured
  R: RNA or transcript proxy
  P: protein/channel/proxy vector
  D: chromatin/accessibility/proxy state
```

This is a modeling vocabulary. It is not a claim that all variables are directly observable in every experiment.

## 2. Physical-driver routes

### Electric route

```text
boundary transfer -> internal electric field proxy -> membrane polarization / current proxy -> Vm
```

Requires surface-transfer model, tissue attenuation, rate/amplitude caps, and safety status.

### Acoustic / ultrasound route

```text
pressure/intensity -> mechanical tension or displacement proxy -> mechanosensitive pathway -> C / Vm
```

Requires acoustic dose model, MI-like proxy, thermal monitoring, and mechanistic controls. It must not use DNA speaker/microphone claims.

### Optical route

```text
fluence/wavelength -> absorption/scattering -> photothermal / photoacoustic / photochemical / construct-specific route -> C / Vm / T
```

Requires optical transport assumptions, thermal model, wavelength controls, and construct declaration if applicable. It must not use holographic gene-laser claims.

### Thermal route

```text
temperature field -> thermal gating or stress pathway -> C / Vm / transcriptional response
```

Requires Pennes-style or equivalent heat model and cumulative thermal dose accounting.

### Magnetic + particle route

```text
magnetic field + declared particles/constructs -> magnetothermal or magnetomechanical route -> T / M -> C / Vm
```

Requires particle inventory, SAR/thermal model, and construct-specific mechanism. It must not use native-DNA biological magnet claims.

## 3. Second-messenger layer

Second messengers are the first biological layer where fast physical perturbations may become cellular signaling events.

Examples:

- calcium proxies;
- voltage-sensitive dye or GEVI proxy;
- GCaMP or related reporter proxy;
- stress-response proxies;
- mechanotransduction markers.

Required discipline:

- measure or explicitly model timing;
- separate direct physical artifact from biological signal;
- use sham and matched-dose controls;
- include uncertainty.

## 4. Transcriptional layer

RNA responses should be treated as delayed outputs, not immediate proof of field control.

Potential research readouts:

- early-response transcripts;
- bulk RNA-seq timepoints;
- targeted transcript panels;
- cfRNA/EV-associated RNA proxies where appropriate.

Canonical expected timing:

```text
physical/membrane effect: ms to s
second messengers: s to min
RNA response: tens of min to hours
protein response: hours
chromatin/tissue response: hours to days
```

A claimed transcript effect without plausible timing and intermediate readouts should be treated as underidentified.

## 5. Protein and channel layer

Protein and channel dynamics can provide feedback into membrane state and future responsiveness.

Examples:

- channel density changes;
- receptor or ligand occupancy;
- secretome/cytokine panels;
- protein proxy assays;
- native MS or similar chemistry/provenance tools for constructs/materials.

These are not assumed. They must be measured or declared as model-only.

## 6. Chromatin / storage layer

Chromatin/accessibility state is a slow variable that may constrain transcriptional response.

Allowed use:

- slow state variable in research models;
- context for DNA-as-storage metaphor;
- endpoint in multi-hour/day studies.

Blocked use:

- holographic genome semantics;
- DNA reading language;
- phantom-DNA imprinting;
- direct mechanism from helical or toroidal resemblance.

## 7. SNARE / vesicle / secretome readout path

Ca2+-triggered vesicle fusion and secretome changes may provide observable downstream readouts in appropriate models.

Allowed use:

- ex vivo validation endpoint;
- secretome panel design;
- vesicle/cytokine output interpretation.

Boundary:

This is a downstream biological mechanism, not evidence that external fields directly control genes. Mechanistic causality requires time ordering and controls.

## 8. 3D spheroid research model

3D spheroids or similar structured models are preferred over flat cell culture when validating tissue-like cascades.

Possible outputs:

- GEVI / GCaMP traces;
- RNA-seq at 0, 15, 30, 60, 120 minutes;
- cytokine/secretome panel at later intervals;
- migration or tube-formation assay where appropriate.

The 3D model supplies effect-size priors and endpoint discipline. It does not validate human actuation.

## 9. Mechanism gating

Mechanism-specific blockers or controls should be used where claims are made.

Examples:

- mechanosensitive pathway blocker for acoustic/mechanical claims;
- thermal matched controls for photothermal claims;
- non-absorbing wavelength controls for optical claims;
- construct-negative controls for opsin or particle-mediated mechanisms;
- sham exposure and matched-dose controls.

A proposed mechanism that survives no specific blocker/control is underidentified.

## 10. Falsification logic

A proposed pathway should be revised or rejected when:

- boundary transfer cannot be measured or modeled within tolerance;
- driver state cannot be observed or bounded;
- second-messenger timing is absent or contradictory;
- RNA response is instantaneous beyond plausible biology;
- RNA response is absent when the proposed driver is confirmed;
- mechanism-specific blockers do not change the effect;
- sham or non-target controls reproduce the effect;
- safety constraints are exceeded.

## 11. Relationship to HDT claims

Mechanism outputs become HDT claims only after minimization, evidence-tier labeling, consent/policy evaluation, and Human Protection Layer gates.

Canonical relation:

```text
research readout
  -> mechanism spine interpretation
  -> evidence claim
  -> Ω evaluation
  -> HPL gate
  -> minimal export or block
```

There is no direct path from biological measurement to person-level identity or high-impact decision.
