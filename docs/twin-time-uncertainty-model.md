# Twin time & uncertainty: the light-cone model

This is not metaphysics; it is how the twin **represents and measures time under uncertainty**, in
the same spirit as [`theory.md`](./theory.md) — a small governed model behind a running instrument,
not a scalar with magical thinking attached.

A rendered visualization accompanies this note:
[`assets/twin-lightcone-model.html`](./assets/twin-lightcone-model.html) (self-contained, theme-aware —
open it in a browser or embed it in the twin surface as an `<iframe>`/component).

## The conceptual picture

At the most fundamental level the substrate is a universal process of **spherical symmetry forming
and breaking**. In a light-cone diagram the two-dimensional surface of the sphere runs *across* the
vertical time axis:

- the **convex outer surface** carries positive charge — **emission**, the widening *future*;
- the **concave inner surface** carries negative charge — **absorption**, the *past*;
- the **apex** is a continuous exchange of energy (photon absorption ⇄ emission). Because the
  universe is never at absolute zero, this exchange never stops — which is exactly why the twin can
  treat time as a *measured, continuous process* rather than a fixed coordinate.

At the smallest scale the sphere of uncertainty is bounded by Heisenberg:

```
Δx · Δp  >  ħ / 4π
```

The `4π` is the full solid angle of the sphere the twin samples over.

> Scope discipline (per the estate research-track boundary): the deeper physics of this model
> (the μ₂ / 26-D / UFT program) is **research, not code**. What is built and shipped is the one
> platform-buildable slice below. We do not encode unproven physics as if it were validated.

## The buildable slice: the apex is where three clocks are read at once

The conceptual light cone is realized as a running observability instrument — the **Domain-22
three-clock** slice. Every observation the twin makes is stamped on three notions of time, and the
disagreement between them *is* the uncertainty sphere made numeric:

| clock | in the diagram | meaning |
|-------|----------------|---------|
| `wall`   | the space axis | physical wall-clock time |
| `causal` | the time axis (at right angles to wall) | Lamport-style per-event order |
| `epoch`  | which turn of the symmetry | coarse generation/phase counter |

Four unit-free residuals quantify the disagreement:

- `ε_order` — wall-vs-causal ordering disagreement (normalized Kendall discordance)
- `staleness` — worst gap between consecutive readings
- `ε_rate` — observed vs expected tick rate
- `ε_phase` — epoch vs the epoch predicted by wall time

**Fail-closed:** below the sample floor (`n ≥ 30`) — or with a collapsed wall span — the instrument
**abstains** rather than reporting a confident-but-empty number. A control that reports on three
samples is not measuring anything (this mirrors the estate `n ≥ 30` measurement floor).

### Reference implementation

- `procyber/observability/three_clock.py` in **ProCybernetica** — stdlib-only, teeth-both-ways
  tests (a clean window passes with zero residuals; each defect and the sub-floor case fail with a
  named reason). Shipped as
  [ProCybernetica#121](https://github.com/SocioProphet/ProCybernetica/pull/121).

## Why this lives here

The twin's readiness lattice ([`theory.md`](./theory.md)) governs *whether* a boundary-crossing
artifact may move; this note governs *when* — the twin's representation of time and the confidence it
attaches to any temporal claim. Both are the same posture: continuous membership measures mapped into
a small set of governed, fail-closed states.
