# Consent and Attestation Receipt Binding v0.1

## Purpose

This document explains how `human-digital-twin` policy, consent, and approval state should bind into a MAIPJ run receipt.

The governing idea is simple:

> A human-facing run is not complete merely because a model answered. It is complete when the system can show whether the action was allowed, whether consent was valid, whether approval was required, and where the attestation evidence lives.

## Receipt contribution

`human-digital-twin` is the authoritative source for:
- `context.policy_bundle_id` when policy is human-governed,
- `task.risk_class` where human policy sets it,
- `outcome.policy_pass`,
- `outcome.human_approved`,
- consent and approval references that belong in `evidence.attestation_refs` or related fields,
- policy/consent reasoning references needed for replay and audit.

## Minimal binding rules

### Policy evaluation
A governed run SHOULD emit a `policy.evaluated` event containing:
- `policy_bundle_id`
- `policy_pass`
- `risk_class`
- `approval_required`
- optional `reason`

### Consent state
If the run involves human data export, sensitive state transitions, or approval-gated content, the system SHOULD emit a `consent.checked` event with:
- `policy_bundle_id`
- `consent_state`
- optional `attestation_ref`

### Approval path
If approval is required, at least one of the following SHOULD appear:
- `approval.requested`
- `approval.granted`
- `approval.denied`

These events may supply:
- `approval_ref`
- `human_approved`
- `reason`
- `attestation_ref`

## Example mapping into a receipt

### From HDT events to receipt fields
- `payload.policy_bundle_id` -> `context.policy_bundle_id`
- `payload.risk_class` -> `task.risk_class` if not already fixed upstream
- `payload.policy_pass` -> `outcome.policy_pass`
- `payload.human_approved` -> `outcome.human_approved`
- `payload.attestation_ref` -> `evidence.attestation_refs[]`
- `payload.approval_ref` -> evidence or approval audit trail reference

## Replay implications

A run that depends on human approval or consent must not pretend to be fully replayable unless the replay path can also account for the approval/consent state.

Therefore:
- receipts SHOULD reference the relevant policy bundle and approval/consent evidence,
- `replay.supported` should be set carefully when approval state is ephemeral or externally anchored,
- non-replayability for human reasons should be explicit rather than hidden.

## Normative statements

1. Every high-risk human-facing run SHOULD emit a `policy.evaluated` event.
2. Every approval-gated run SHOULD expose whether approval was required and whether it was granted.
3. Every consent-sensitive run SHOULD expose consent state or a consent attestation reference.
4. Policy and approval metadata MUST NOT be inferred later from application logs alone if a first-class HDT event could have emitted it.
5. A receipt with missing policy bundle identity is incomplete for governed human-facing paths.

## Acceptance gate for v0.1

The HDT side is sufficient for v0.1 when:
1. one live or captured trace includes `policy.evaluated`,
2. approval requirement and approval outcome are visible when relevant,
3. at least one attestation or approval reference can be attached to evidence,
4. the receipt builder can map HDT events without custom case-specific logic.
