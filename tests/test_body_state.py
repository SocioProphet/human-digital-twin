"""Body-state model schema — conformance + the two safety invariants.

The body-state contract (api/schemas/body-state/body-state-model.schema.json) is the
twin's digital state x(t) plus the dynamical-model representation. Because x(t) and its
predictions are dispositive personal data, the schema plugs into the Ω protection envelope
and enforces two gates structurally. These tests lock them in:

  1. learned-only / divergent forward model  ->  cannot be ACTIONABLE, cannot actuate
     ("learned proposes, physics disposes")
  2. ACTIONABLE / DELIVERED  ->  requires present consent AND an allow decision
     ("validity is not permission")
"""
import json
from pathlib import Path

from referencing import Registry, Resource
from jsonschema import Draft202012Validator

SCHEMAS = Path(__file__).resolve().parents[1] / "human_digital_twin" / "api" / "schemas"


def _validator():
    bs = json.loads((SCHEMAS / "body-state" / "body-state-model.schema.json").read_text())
    env = json.loads((SCHEMAS / "hpl" / "human-protection-envelope.json").read_text())
    reg = Registry().with_resources([
        (bs["$id"], Resource.from_contents(bs)),
        (env["$id"], Resource.from_contents(env)),
    ])
    return bs, Draft202012Validator(bs, registry=reg)


def _protection(actuation="protocol_required", consent_present=True, decision="allow"):
    return {
        "program_id": "pilot", "profile_id": "p1", "subject_scope": "individual",
        "protected_person_risk": "medium", "evidence_tier": "E3", "status": "draft",
        "claim_boundary": {"mechanism_status": "validated", "unsupported_claim_blocked": True},
        "consent": {"required": True, "present": consent_present, "scope": ["vitals"]},
        "privacy": {"raw_private_evidence_attached": False, "minimization_basis": "aggregates only"},
        "physical_safety": {"human_actuation": actuation},
        "cognitive_safety": {"hidden_persuasion": "blocked", "high_impact_decision": "review_required"},
        "misuse_review": {"required": True, "completed": True},
        "redress": {"inspect": True, "challenge": True, "revoke": True, "appeal": True},
        "policy": {"decision": decision, "reasons": ["ok"]},
        "provenance": {"evidence_hash": "abc", "policy_version": "v1"},
    }


def _instance(reconciliation="physics_verified", omega="TRUSTED", **prot):
    return {
        "twin_id": "t1", "profile_id": "p1", "as_of": "2026-07-02T06:00:00Z", "omega_state": omega,
        "compartments": [{"system": "cardio", "variables": [{"name": "hr", "value": 62, "unit": "bpm", "estimate_sd": 2.1}]}],
        "state_estimation": {"method": "ekf", "sensor_refs": ["wearable:hrv"], "innovation_norm": 0.3},
        "dynamical_model": {"mechanistic": {"model_ref": "cvode:v2", "verified_compute": True}, "reconciliation": reconciliation},
        "protection": _protection(**prot),
    }


def test_schema_is_well_formed():
    bs, _ = _validator()
    Draft202012Validator.check_schema(bs)


def test_physics_verified_actionable_is_valid():
    _, v = _validator()
    inst = _instance("physics_verified", "ACTIONABLE")
    assert list(v.iter_errors(inst)) == []


def test_learned_only_cannot_be_actionable_or_actuate():
    _, v = _validator()
    inst = _instance("learned_only", "ACTIONABLE", actuation="approved_external_process")
    assert list(v.iter_errors(inst)), "safety gate must reject learned-only actionable/actuation"


def test_divergent_forward_model_is_gated():
    _, v = _validator()
    inst = _instance("divergent", "DELIVERED", actuation="protocol_required")
    assert list(v.iter_errors(inst)), "divergent reconciliation must not reach DELIVERED"


def test_actionable_requires_consent_and_allow():
    _, v = _validator()
    assert list(v.iter_errors(_instance("physics_verified", "DELIVERED", consent_present=False)))
    assert list(v.iter_errors(_instance("physics_verified", "ACTIONABLE", decision="needs_review")))
