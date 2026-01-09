"""Ω promotion engine for the Human Digital Twin (HDT).

We model a *readiness lattice* over artifacts that may cross a boundary (export, delegation, publication).

Key idea:
- **scores** are continuous (0..1) and come from measurements,
- **states** are discrete (ABSENT..DELIVERED) and are the governance-friendly labels.

The engine is deterministic and explainable:
- same inputs => same output
- always returns *reasons* for promotions
- clamps inputs and flags anomalies early

The lattice (default):
ABSENT → SEEDED → NORMALIZED → LINKED → TRUSTED → ACTIONABLE → DELIVERED
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

STATES: List[str] = [
    "ABSENT",
    "SEEDED",
    "NORMALIZED",
    "LINKED",
    "TRUSTED",
    "ACTIONABLE",
    "DELIVERED",
]

# Default thresholds (kept in sync with capd/di-eval.capd.json)
THRESH = {
    "cbd_norm": 0.60,
    "cbd_link": 0.75,
    "cgt_trust": 0.70,
    "nhy_deliver": 0.80,
    "all_actionable": 0.75,
}

@dataclass(frozen=True)
class EvalKFS:
    """KFS membership scores, each in [0,1]."""
    m_cbd: float
    m_cgt: float
    m_nhy: float

def _clamp01(x: float) -> float:
    try:
        xf = float(x)
    except Exception:
        return 0.0
    if xf < 0.0: return 0.0
    if xf > 1.0: return 1.0
    return xf

def _state_index(s: str) -> int:
    return STATES.index(s) if s in STATES else 0

def evaluate(kfs: EvalKFS, prev: str = "ABSENT") -> Tuple[str, Dict[str, Any]]:
    """Compute the next Ω state and return (state, meta).

    Promotions are monotone w.r.t. previous state:
    - we do not automatically *demote* here (demotion is a policy decision)
    - we also refuse to 'skip' guarantees without meeting thresholds
    """
    m_cbd = _clamp01(kfs.m_cbd)
    m_cgt = _clamp01(kfs.m_cgt)
    m_nhy = _clamp01(kfs.m_nhy)

    reasons: List[str] = []
    s = _state_index(prev)

    # SEEDED: any meaningful signal exists
    if s < 1 and max(m_cbd, m_cgt, m_nhy) > 0.0:
        s = 1
        reasons.append("seeded[signal>0]")

    # NORMALIZED: coherence/boundedness is strong enough
    if s < 2 and m_cbd >= THRESH["cbd_norm"]:
        s = 2
        reasons.append(f"normalized[cbd>={THRESH['cbd_norm']:.2f}]")

    # LINKED: we have enough linkage confidence to connect contexts
    if s < 3 and m_cbd >= THRESH["cbd_link"]:
        s = 3
        reasons.append(f"linked[cbd>={THRESH['cbd_link']:.2f}]")

    # TRUSTED: governance/consent/trust membership is adequate
    if s < 4 and m_cgt >= THRESH["cgt_trust"]:
        s = 4
        reasons.append(f"trusted[cgt>={THRESH['cgt_trust']:.2f}]")

    # ACTIONABLE: all axes are sufficiently high (avoid action on one-axis hype)
    if s < 5 and min(m_cbd, m_cgt, m_nhy) >= THRESH["all_actionable"]:
        s = 5
        reasons.append(f"actionable[all>={THRESH['all_actionable']:.2f}]")

    # DELIVERED: delivery/usefulness is high enough (separate from consent!)
    if s < 6 and m_nhy >= THRESH["nhy_deliver"]:
        s = 6
        reasons.append(f"delivered[nhy>={THRESH['nhy_deliver']:.2f}]")

    next_state = STATES[s]
    meta = {
        "reasons": reasons,
        "m_cbd": m_cbd,
        "m_cgt": m_cgt,
        "m_nhy": m_nhy,
        "prev": prev if prev in STATES else "ABSENT",
        "next": next_state,
    }
    return next_state, meta

def promote_omega(prev: str, kfs: EvalKFS) -> Tuple[str, Dict[str, Any]]:
    """Compatibility wrapper for older naming."""
    return evaluate(kfs=kfs, prev=prev)
