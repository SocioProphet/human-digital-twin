# Personhood-bound export readiness v0.1

## Status

Contract-only companion lane for Human Digital Twin export/readiness governance.

This document defines how HDT should evaluate and export claims derived from HolographMe `PersonhoodBindingRecord`, `IdentitySigilSeal`, Regis personhood/sigil graph records, and Identity Is Prime personhood proof artifacts.

It does not define personhood. It does not replace the Ω lattice. It constrains what may leave the boundary.

## Purpose

A personhood binding is high-consequence. It may be necessary to prove that a mesh identity is person-bound, but exporting raw ceremony evidence, guardian refs, credential refs, wallet refs, portrait refs, or graph internals can become surveillance lasagna.

HDT therefore treats personhood-bound identity as an outward claim with readiness, minimization, consent, provenance, and repair requirements.

The export target should be:

```text
This subject is person-bound at assurance level Pn for purpose Y under policy Z.
```

not:

```text
Here are the raw personhood ceremony, guardians, credentials, wallet, portrait, linked accounts, and recovery graph.
```

## Doctrine

Ω is readiness, not identity.

Personhood binding is a governed continuity claim, not the person.

Personhood-bound export is a scoped assertion, not raw evidence disclosure.

The export should disclose the smallest sufficient claim.

## Export claim shape

A personhood-bound export should minimally contain:

- `subjectRef` or pseudonymous subject reference;
- `assuranceLevel`;
- `bindingScope`;
- `allowedPurpose`;
- `policyDecisionRef`;
- `omegaState`;
- `evidenceClassSummary` rather than raw evidence;
- `validFrom` / `validTo` or revalidation reference;
- `revocationStatusRef`;
- `repairRef` when not exportable;
- non-claims.

## Export readiness requirements

A personhood-bound export is admissible only when:

1. Ω state is at least `TRUSTED` for advisory claims or `ACTIONABLE` for consequential claims.
2. Consent is active, purpose-bound, recipient-bound, and not expired.
3. The export contains an assurance claim, not raw personhood evidence.
4. Raw guardian, credential, portrait, wallet, and recovery refs are withheld unless explicitly required and separately approved.
5. The binding has recovery and revocation posture.
6. The claim has validity or revalidation bounds.
7. The export includes non-claims preventing wallet/account/portrait/device/agent/reputation collapse.
8. Policy decision metadata is present and replayable.

## Default deny cases

A personhood-bound export must be denied or converted to repair when:

- the export attempts to include raw ceremony evidence without explicit policy approval;
- the export includes wallet/account/portrait/device refs as personhood proof;
- the export omits consent or purpose;
- the export omits recovery or revocation status;
- the export claims global personhood or global identity correlation;
- the export claims biometric identity by default;
- the export exposes all identity contexts;
- the export is stale and lacks revalidation;
- the export is LLM-only without validation or policy artifact.

## Ω interpretation

Suggested interpretation for personhood-bound claims:

```text
ABSENT      no exportable binding claim
SEEDED      draft claim exists, not exportable
NORMALIZED  shape-valid but not policy/export-ready
LINKED      source artifacts cross-reference correctly
TRUSTED     advisory export allowed under active consent
ACTIONABLE  consequential export allowed under active consent and policy approval
DELIVERED   export emitted with receipt, minimization, and replay metadata
```

## Repair posture

If the claim is not exportable, the system should emit a repair decision rather than silently downgrade or leak raw evidence.

Repair examples:

- refresh consent;
- revalidate binding;
- add recovery policy;
- remove raw evidence from export;
- lower assurance claim;
- scope purpose/recipient;
- mark advisory-only;
- block export.

## Non-claims

A personhood-bound export does not make any wallet the person.

A personhood-bound export does not make any portrait biometric proof by default.

A personhood-bound export does not make any account, device, credential, agent, graph edge, or reputation record equivalent to the person.

A personhood-bound export does not authorize public correlation of all identity contexts.

A personhood-bound export does not reveal raw ceremony evidence unless separately authorized.

## First executable target

The first fixture lane should include:

- a valid advisory P3 personhood-bound export claim;
- a rejected raw-evidence export claim;
- a validator that checks shape and semantic export invariants using stdlib only.
