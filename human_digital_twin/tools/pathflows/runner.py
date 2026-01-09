"""Path-flow runner: exercises Evaluate/Promote over sample scenarios.

This is a terminal-friendly harness: feed scenarios, get a JSON report.
The point is *repeatability* rather than realism.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Tuple

import yaml

from ...api.services.eval.omega import EvalKFS, promote_omega

def run_scenario(name: str, steps: int) -> Tuple[str, int, Dict[str, Any]]:
    prev = "ABSENT"
    meta: Dict[str, Any] = {}
    for k in range(steps):
        # Toy scores; swap for real measurements.
        kfs = EvalKFS(m_cbd=0.6 + 0.05*k, m_cgt=0.55 + 0.05*k, m_nhy=0.50 + 0.05*k)
        prev, meta = promote_omega(prev, kfs)
        if prev == "DELIVERED":
            return prev, k + 1, meta
    return prev, steps, meta

def main(scenarios_path: str = "tools/pathflows/examples.yaml") -> int:
    sc = list(yaml.safe_load(Path(scenarios_path).read_text(encoding="utf-8")))
    out: Dict[str, Any] = {}
    for s in sc:
        omega, steps, meta = run_scenario(s["name"], int(s["expect"]["steps_max"]))
        out[s["name"]] = {"omega": omega, "steps": steps, "meta": meta}
    Path("tools/pathflows/report.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
