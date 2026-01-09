# Human Digital Twin (HDT) — Ω Protocol Kit

This repository is a **protocol + reference implementation**: we define a minimal, reproducible “human API” surface
for *evaluating*, *promoting*, and *exporting* human-centric artifacts (observations, consented exports, capability proofs)
under **zero-trust** constraints.

The kit is intentionally modular:

- **Ω (Omega) promotion engine**: a small lattice that turns measurable signals into a *state* (ABSENT→…→DELIVERED).
- **Policy hooks**: OPA/Rego examples that gate “export” and trigger “repair” pushouts.
- **Schemas**: JSON Schema for the on-wire / on-disk representation of an Ω-evaluable extension.
- **TritRPC surface**: a YAML service contract (wire-format first; runtime second).
- **Pathflows**: a terminal runner that simulates progression across the lattice for regression tests and demos.

Nothing here is “the product.” It’s the **shared contract** we can embed into SourceOS/Sociosphere-style systems:
policy-guarded, audit-evidenced, human-consented, and composable.

---

## Conceptual model (why Ω exists)

### 1) We don’t export data; we export *claims with provenance*
A “human digital twin” becomes dangerous when it behaves like an *unaudited shadow identity*.
So we treat every outward projection as a **claim** that must be:

1. **Measurable** (scores / signals exist),
2. **Bounded** (privacy + consent + minimization),
3. **Accountable** (evidence and repair paths exist).

Ω is the *label* for “how much we trust this claim to leave the boundary.”

### 2) The 7-state Ω lattice
The default lattice is:

`ABSENT → SEEDED → NORMALIZED → LINKED → TRUSTED → ACTIONABLE → DELIVERED`

Each step corresponds to a stronger bundle of guarantees.
We compute promotions from three membership scores (all normalized to **[0, 1]**):

- **m_CBD**: *coherence / boundedness / de-dup* (is the thing clean and internally consistent?)
- **m_C'GT**: *consent / governance / trust* (do we have permission and legitimacy?)
- **m_NHY**: *delivery / usefulness* (did we actually deliver value without breaking rules?)

Think of these as **orthogonal axes**. We can be coherent but not consented; consented but not useful; useful but not coherent, etc.

### 3) Policies are first-class
The Ω engine provides a *proposal* (“this looks TRUSTED”), but policy decides:

- whether export is allowed,
- whether to trigger a “repair” cycle upstream (units mismatch, consent revoked, PII risk, etc.).

This split is deliberate: *math is not governance*.

---

## Repo layout

- `human_digital_twin/api/trpc/devine.trpc.yaml` — service contract (TritRPC surface)
- `human_digital_twin/api/services/eval/omega.py` — Ω promotion engine
- `human_digital_twin/api/policies/opa/*.rego` — policy samples (export + repair)
- `human_digital_twin/api/schemas/kfs-eval.json` — schema for Ω-evaluable extension
- `human_digital_twin/tools/pathflows/` — terminal runner + scenarios
- `tests/` — regression tests (promotion + schema)
- `capd/` — capability descriptor example (CapD)

---

## Quickstart (terminal)

One-liners, no ceremony:

```bash
python3 -m venv .venv && . .venv/bin/activate && pip install -e '.[dev]' && pytest -q && hdt-pathflows tools/pathflows/examples.yaml
```

Run the local UDS shim server (placeholder runtime):

```bash
. .venv/bin/activate && hdt-shim
```

In another terminal, send a request:

```bash
python3 - <<'PY'
import socket, json
sock="/tmp/devine_intel.sock"
req={"rpc":"Evaluate","prev":"ABSENT","kfs":{"m_cbd":0.7,"m_cgt":0.8,"m_nhy":0.6}}
s=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM); s.connect(sock)
s.sendall(json.dumps(req).encode()); data=s.recv(65536); s.close()
print(data.decode())
PY
```

---

## Best practices (the boring safety rails)

1. **Never treat Ω as identity.** Ω is an operational readiness label, not an ontology of the human.
2. **Clamp and audit inputs.** Every membership score should record units, sensors, transforms, and uncertainty.
3. **Policy-default deny.** Promotion can be permissive; export must not be.
4. **Separate compute from governance.** Keep the Ω engine deterministic and testable; keep policy explicit and reviewable.
5. **Repair is mandatory.** When inputs violate invariants, we don’t “force success”; we generate a repair plan and stop.
6. **Minimize.** Export the smallest sufficient artifact; keep raw private evidence local by default.

---

## What we inherited and what we fixed

The provided archive was a “patch kit” containing partial files with placeholder ellipses (`...`).
This repo **reconstructs** those fragments into a coherent, testable, export-ready package while preserving the intent:
Omega lattice, OPA policy gates, schema, and TritRPC surface.

---

## Next steps (the real work)

- Wire this TritRPC surface into the canonical Triune/TritRPC runtime.
- Replace the shim protocol with the real wire format + auth + evidence envelopes.
- Expand schema to a full FHIR-compatible Extension profile (if we want interoperability).
- Add de-identification scoring, measurement provenance, and audit evidence outputs.
