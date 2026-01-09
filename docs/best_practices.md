# Best practices

## Measurement hygiene
- Keep raw evidence local; compute normalized scores as derived artifacts.
- Record provenance: sensor, method, units, uncertainty.
- Clamp scores in runtime, but treat out-of-range values as a *validation failure* upstream.

## Privacy by default
- Export only the minimal “claim” necessary.
- Attach Ω, reasons, and policy decision metadata; do not attach raw logs unless required.

## Policy reviewability
- Keep policies small, named, versioned.
- Avoid embedding complex arithmetic in Rego; put math in the engine, gating in policy.

## Runtime separation
- TritRPC spec is the contract.
- Shims and runtimes are replaceable.
- Never let a test shim become production glue without hardening (auth, evidence, logging, rate limits).
