# FCBCP time-scale ladder

Status: research timing scaffold. Not a validated endpoint model.

Owner: `SocioProphet/human-digital-twin`.

## 0. Purpose

This document captures the timing discipline required for FCBCP research. It prevents instant-mechanism overclaims by requiring every proposed pathway to respect plausible physical and biological time scales.

The core rule:

```text
fast physics may gate slower biology;
slower biology should not be claimed as instantaneous without extraordinary evidence.
```

## 1. Seed ladder

| Layer | Dominant process | Typical scale | FCBCP role |
|---|---|---:|---|
| Ionic polarization / dielectric response | material polarization and layer response | ns to us | high-frequency material/boundary behavior |
| Channel gating / fast conformational response | channel or sensor kinetics | us to ms | fast biological transduction candidate |
| Membrane RC / membrane polarization | membrane filtering and polarization | ms to 100 ms | membrane-state driver |
| Mechanical/thermal/optical local driver | pressure, tension, temperature, absorption | ms to s/min depending on modality | modality-specific internal driver |
| Second messengers | calcium, stress, signaling proxies | s to min | first biological signaling layer |
| Early transcripts | immediate early genes / targeted RNAs | tens of min to hours | RNA response window |
| Protein/channel response | translation, trafficking, receptor/channel changes | hours | feedback and execution layer |
| Chromatin remodeling | accessibility, epigenetic state, loop changes | hours to days | slow storage/access layer |
| Tissue bioelectric repatterning | network adaptation, gap junction/channel changes | hours to days | multicellular state adaptation |
| Organismal homeostatic drift | endocrine, immune, tissue remodeling | days to weeks | not an FCBCP short-run control claim |

## 2. Research implication

Any FCBCP hypothesis must declare its expected timing.

Examples:

- `Vm` or a membrane proxy may respond quickly if the boundary driver is real.
- Second messengers should trail the physical driver.
- RNA should generally trail second messengers.
- Protein and chromatin should trail RNA.

A claimed RNA effect at time zero is suspect unless the design directly measures an already-existing transcript pool or sampling artifact.

## 3. Falsification rules

A pathway becomes underidentified or falsified when:

- claimed transcript effects precede measurable physical or signaling drivers;
- sham controls produce the same timing profile;
- non-targeted controls produce the same response;
- blockers do not alter the claimed pathway;
- thermal or mechanical artifacts explain the response;
- response timing is inconsistent with the proposed biological mechanism.

## 4. Relation to storage/code/computer metaphor

The ladder disciplines the metaphor:

- DNA as storage means slow biological state and accessibility, not a literal drive.
- RNA as code means transient regulatory/translation substrate, not Turing code.
- Human as computer means distributed biological system, not replacement of personhood.

## 5. Required metadata

FCBCP events and research protocols should include:

```yaml
timing:
  expected_driver_latency: string
  expected_second_messenger_latency: string
  expected_rna_latency: string
  expected_protein_latency: string
  expected_chromatin_latency: string
  sampling_times: [string]
  falsification_condition: string
```

## 6. Human Protection Layer

Timing plausibility does not authorize human actuation. It only helps classify research claims.

Any human-derived timing data remains private by default and exportable only as minimized, consented claims with evidence tier and policy status.
