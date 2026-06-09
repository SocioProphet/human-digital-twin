# Best practices

## Measurement hygiene
- Keep raw evidence local; compute normalized scores as derived artifacts.
- Record provenance: sensor, method, units, uncertainty.
- Clamp scores in runtime, but treat out-of-range values as a *validation failure* upstream.

## Privacy by default
- Export only the minimal “claim” necessary.
- Attach Ω, reasons, and policy decision metadata; do not attach raw logs unless required.
- For personhood-bound identity, export assurance, purpose, policy, and revocation posture; do not export raw ceremony evidence, guardian refs, wallet refs, portrait refs, credential refs, or recovery graph by default.

## Policy reviewability
- Keep policies small, named, versioned.
- Avoid embedding complex arithmetic in Rego; put math in the engine, gating in policy.
- Treat personhood-bound exports as default-deny unless purpose, recipient, consent, policy decision, validity, and revocation metadata are present.

## Runtime separation
- TritRPC spec is the contract.
- Shims and runtimes are replaceable.
- Never let a test shim become production glue without hardening (auth, evidence, logging, rate limits).

## Identity non-collapse
- Never treat Ω as identity.
- Never treat a personhood-bound export as the person.
- Never let wallet, account, portrait, device, credential, agent, graph edge, or reputation become equivalent to the person.
- Public profile exports must not expose high-assurance personhood evidence unless a separate policy explicitly approves that disclosure.
