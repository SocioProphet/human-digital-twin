from human_digital_twin.api.services.eval.omega import EvalKFS, promote_omega

def test_monotone_promotion():
    prev = "ABSENT"
    # Increasing scores should not demote
    for i in range(10):
        kfs = EvalKFS(m_cbd=min(1.0, 0.1*i), m_cgt=min(1.0, 0.1*i), m_nhy=min(1.0, 0.1*i))
        nxt, meta = promote_omega(prev, kfs)
        assert meta["prev"] == prev if prev in ["ABSENT","SEEDED","NORMALIZED","LINKED","TRUSTED","ACTIONABLE","DELIVERED"] else meta["prev"] == "ABSENT"
        assert nxt in ["ABSENT","SEEDED","NORMALIZED","LINKED","TRUSTED","ACTIONABLE","DELIVERED"]
        # index is monotone
        order = ["ABSENT","SEEDED","NORMALIZED","LINKED","TRUSTED","ACTIONABLE","DELIVERED"]
        assert order.index(nxt) >= order.index(prev)
        prev = nxt

def test_delivered_threshold():
    prev, meta = promote_omega("ACTIONABLE", EvalKFS(m_cbd=1.0, m_cgt=1.0, m_nhy=0.81))
    assert prev == "DELIVERED"
