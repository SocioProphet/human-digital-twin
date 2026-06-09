#!/usr/bin/env python3
"""Validate personhood-bound export readiness fixtures.

This validator is intentionally stdlib-only. It checks the HDT export posture:
export scoped person-bound assurance claims, not raw personhood evidence.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_DIR = ROOT / "examples"

ALLOWED_EXPORT_STATES = {"TRUSTED", "ACTIONABLE", "DELIVERED"}
RAW_EVIDENCE_MARKERS = ("ev_", "wallet:", "portrait:", "guardian:", "recovery://", "credential:", "vc://")
REQUIRED_NON_CLAIM_PHRASES = (
    "wallet the person",
    "portrait biometric proof by default",
    "does not authorize public correlation",
    "does not reveal raw ceremony evidence",
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_shape(record: dict[str, Any], *, source_label: str) -> None:
    for field in [
        "record_type",
        "schema_version",
        "export_id",
        "subject_ref",
        "personhood_binding_ref",
        "identity_sigil_seal_ref",
        "binding_scope",
        "assurance_level",
        "allowed_purpose",
        "recipient_ref",
        "omega_state",
        "policy_decision_ref",
        "evidence_class_summary",
        "raw_evidence_refs_exported",
        "withheld_raw_evidence_classes",
        "revocation_status_ref",
        "transition_receipt_ref",
        "non_claims",
    ]:
        require(field in record, f"{source_label}: missing {field}")
    require(record["record_type"] == "PersonhoodBoundExportReadiness", f"{source_label}: invalid record_type")
    require(str(record["schema_version"]).startswith("0.1."), f"{source_label}: invalid schema_version")


def semantic_diagnostics(record: dict[str, Any]) -> list[str]:
    diagnostics: list[str] = []
    omega_state = record.get("omega_state")
    non_claims = "\n".join(str(item).lower() for item in record.get("non_claims", []))
    purpose = str(record.get("allowed_purpose", "")).lower()
    recipient = str(record.get("recipient_ref", "")).lower()

    if omega_state not in ALLOWED_EXPORT_STATES:
        diagnostics.append(f"omega_state {omega_state} is not export-ready")

    if not record.get("policy_decision_ref"):
        diagnostics.append("policy_decision_ref required")
    if not record.get("personhood_binding_ref"):
        diagnostics.append("personhood_binding_ref required")
    if not record.get("identity_sigil_seal_ref"):
        diagnostics.append("identity_sigil_seal_ref required")
    if not record.get("allowed_purpose"):
        diagnostics.append("allowed_purpose required")
    if not record.get("recipient_ref"):
        diagnostics.append("recipient_ref required")
    if not record.get("revocation_status_ref"):
        diagnostics.append("revocation_status_ref required")
    if not record.get("transition_receipt_ref"):
        diagnostics.append("transition_receipt_ref required")

    if record.get("raw_evidence_refs_exported") is not False:
        diagnostics.append("raw personhood evidence refs must not be exported by default")
    raw_refs = [str(item) for item in record.get("raw_evidence_refs", [])]
    for ref in raw_refs:
        if ref.startswith(RAW_EVIDENCE_MARKERS):
            diagnostics.append(f"raw evidence ref leaked: {ref}")

    summary = set(record.get("evidence_class_summary", []))
    for required in {"self_attestation", "liveness_or_presence", "recovery_policy", "revocation_policy"}:
        if required not in summary:
            diagnostics.append(f"evidence_class_summary missing {required}")

    if "public" in recipient or "public" in purpose:
        if "public_profile" in purpose and record.get("assurance_level", "").startswith(("P3_", "P4_", "P5_")):
            diagnostics.append("public profile export must not expose high-assurance personhood claim")

    if record.get("valid_to") is None and not record.get("repair_ref"):
        diagnostics.append("open-ended personhood export requires repair_ref or revalidation bound")

    for phrase in REQUIRED_NON_CLAIM_PHRASES:
        if phrase not in non_claims:
            diagnostics.append(f"missing non-claim phrase: {phrase}")

    if "global human worth" in "\n".join(str(item).lower() for item in record.get("evidence_class_summary", [])):
        diagnostics.append("personhood export must not encode global human worth")

    return diagnostics


def expected_result(path: Path) -> str:
    return "fail" if ".rejected." in path.name or path.name.startswith("bad-") else "pass"


def main() -> int:
    examples = sorted(EXAMPLE_DIR.glob("personhood_bound_export*.json"))
    if not examples:
        raise SystemExit("No personhood-bound export examples found")

    checked = []
    for path in examples:
        record = load_json(path)
        validate_shape(record, source_label=path.name)
        diagnostics = semantic_diagnostics(record)
        actual = "fail" if diagnostics else "pass"
        expected = expected_result(path)
        checked.append({"example": path.name, "expected": expected, "actual": actual, "diagnostics": diagnostics})
        if actual != expected:
            raise AssertionError(json.dumps(checked[-1], indent=2))

    print(json.dumps({"ok": True, "checked": checked}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
