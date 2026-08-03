# Twin dashboard architecture — Self ⟷ Body ⟷ Universe

*The governing spec for the twin's exploration surface. Not metaphysics; control + observability over a
recenterable model, aligned to the estate's existing ontologies. This document guides three surfaces —
this spec, the interaction prototype, and the live `client-vue` screen — so they cannot drift.*

## The synthesis (what the concept art is actually describing)

Stripped of iconography, the "Distributed Intelligent Mesh" is three twins sharing one substrate:

| ring | is | built in |
|------|----|----------|
| **SELF** (the cube) | the observer origin — *center the universe on any point* | new: light-cone model (`twin-time-uncertainty-model.md`); coordinate space `procyber/semantic/` |
| **BODY** | the human twin — readiness lattice, body-state | `human-digital-twin` (`theory.md`, `BODY_STATE_MODEL.md`) |
| **UNIVERSE** | the galactic twin — cube of space | `usol-space-library` (Horizons ephemeris, DIRBE, `fov`, `projection`) |
| **FLOW** | the distributed sensing mesh | `usol sensor_mesh.py`; HellGraph AtomSpace |
| **ANALYTICS** | temporal-coherence + observability | three-clock (`ProCybernetica three_clock.py`), `sensor_mesh` residuals |
| **AWARENESS** | the epistemic / certainty axis | KKO epistemic lattice; `usol projection` epistemic typing |

Nothing here is new ontology. Every ring maps to something already shipped.

## The 5D map

A "cube of space with all regions mapped" is **space³ × time × certainty**:

- **space³** — X/Y/Z, real coordinates from ephemeris; regions are entities/nodes in the canonical
  coordinate space (`procyber/semantic/`), never a bespoke voxel type.
- **time** — Horizons `VECTORS` trajectories give 3D-over-time (the 4th axis).
- **certainty** — the 5th axis: *how much science has filled a region in.* This is the KKO epistemic
  level + the sensor-mesh coherence, not a decorative gradient. Unmapped → well-mapped is
  `speculative → … → empirical/bounded`.

## The core mechanic — horoscope → cone → region

"Connect the dots from a horoscope and orientation, through time and space, to any region of the cube
constrained by that cone" is expressible entirely in existing primitives:

1. **Observer origin** — a spacetime point (e.g. a birth time + lat/long) = the light-cone apex / the
   Self cube's center. Recentering the cube = choosing a new origin.
2. **Orientation** — geocentric ephemeris at that origin yields the celestial-sphere frame (obliquity,
   ecliptic, ASC/MC). *A horoscope, stripped of interpretation, is exactly this — real astronomy USOL
   computes (`horizons` topocentric/observer tables).* `epistemic_level = empirical`.
3. **Cone constraint** — the light cone (and `usol fov.py`) bound which regions are causally
   reachable / observable from that origin. Selection is *constrained by the cone.*
4. **Region selection** — regions inside the cone, ranked/colored by the certainty axis.
5. **Lens (optional)** — an interpretive **projection** overlays meaning. Typed, capped, toggleable
   (below).

## Lenses: typed projections that may graduate — never a mismatch

The esoteric material (astrology, anthroposophy / Steiner, EarthRing correspondences, the
"Simulation Platform" mandala — note it is keyed with our own `111/114/214/666` semantic
coordinates) enters through the **existing** `usol` projection / "Books" seam, now bound to the
canonical epistemic lattice (`usol projection.py`, PR #4):

- A projection **annotates** substrate; it never mutates scientific data (enforced in code).
- Its `epistemic_level` is **capped below `empirical`** — an interpretive overlay can never certify
  itself as ground truth. Even an `exact` archetype placement certifies the *placement*, not the
  interpretation.
- A lens *may* be **`candidate_ontology`** — "an ontology of its own, not yet fully integrated or
  known." That is a **hypothesis to test**, not a fact. Graduation into a real ontology is an
  explicit, evidence-gated promotion **out** of the projection layer (the lift⊣ground adjunction in
  `procyber/semantic/`), never an in-layer tier bump.

This is the rule that prevents adopting the art as a rival vocabulary: **every lens is a governed,
capped, graduatable projection over real ephemeris + the canonical coordinate space.**

## Availability (what exists vs. the gap)

**Have:** ephemeris (`usol horizons`, `client-vue/src/space/ephemeris.ts`); the cone (`usol fov`);
the projection/Books seam (`usol data/projections/rev12-*`); light-cone model + viz; `sensor_mesh`;
`procyber/semantic/` coordinate space; the body twin; KKO epistemic lattice.

**Gap:** the **unified Self⟷Body⟷Universe surface** — the recenterable cube, the horoscope→cone→region
traversal, and the celestial-sphere/natal orientation view. No such screen exists yet; there is (by
design) no astrology/anthroposophy viz outside the typed projection layer.

## The three surfaces (build order)

1. **This spec** — the governing contract; keep the other two conformant to it.
2. **Interaction prototype** — a standalone artifact iterating the cube UX, **bound to this model**
   (regions = coordinate-space entities, cone = fov + light cone, lenses = typed projections). The
   earlier free-standing cube prototype is intentionally *not shipped* because it invented a bespoke
   region model — it must be rebound to this spec first.
3. **`client-vue` `SpaceTwin.vue` (`/space`)** — the live screen, built where `space/ephemeris.ts`
   already lives (Vue 3 + vendored deck.gl), fed by `usol`, rendering the cube + cone + typed lenses.

## Invariants (any surface must hold)

- Substrate and lens are separate; a lens never appears as fact.
- Certainty is shown, never faked; an unmapped region reads as unmapped, not empty-confident.
- Fail-closed observability: the sensor-mesh coherence for a region abstains below `n ≥ 30`
  (`usol sensor_mesh`).
- Recentering re-expresses everything relative to the chosen origin; nothing is privileged but the
  current center.
