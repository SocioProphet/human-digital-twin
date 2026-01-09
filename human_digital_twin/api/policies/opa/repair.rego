package repair

# "Repair" means we refuse to proceed until upstream invariants are restored.
# Emit triggers; the runtime decides how to route them (ticket, DAG step, message bus, etc.).

trigger["unit_ambiguity"] {
  input.validation.units_ok == false
}

trigger["consent_revoked"] {
  input.consent.allowed == false
}

trigger["pii_risk"] {
  input.deid.estimated_risk > 0.0
}
