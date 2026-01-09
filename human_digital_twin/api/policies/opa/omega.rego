package omega

default allow_export = false

# Export is a boundary-crossing event. Default deny, then explicitly grant.
# We only allow export when:
# - the resource contains our kfs-eval extension
# - consent is allowed (input.consent.allowed)
# - the resource is at least TRUSTED, and
# - m_cgt meets a threshold (governance/trust membership)
allow_export {
  some e
  e := input.resource.extension[_]
  e.url == "https://socioprophet.dev/ext/kfs-eval"
  e.valueCoding.system == "Ω"
  e.valueCoding.code == "TRUSTED"  # tighten as needed: ACTIONABLE/DELIVERED
  input.consent.allowed == true

  some m
  m := e.extension[_]
  m.url == "m_cgt"
  m.valueDecimal >= 0.75
}
