"""Placeholder TritRPC-over-UDS server shim.

This is **not** the canonical TritRPC runtime. It's a local harness so we can:
- run deterministic tests in a terminal,
- exercise request/response envelopes,
- validate that the service surface is coherent.

Protocol (JSON over Unix domain socket, one request per connection):
Request:
  {"rpc":"Evaluate","prev":"ABSENT","kfs":{"m_cbd":0.7,"m_cgt":0.8,"m_nhy":0.6}}
Response:
  {"ok":true,"omega":"TRUSTED","prev":"ABSENT","next":"TRUSTED","m_cbd":0.7,"m_cgt":0.8,"m_nhy":0.6,"reasons":[...]}

Supported rpc:
- Evaluate
- Promote
- WorldWeights

"""

from __future__ import annotations

import json
import os
import socket
from typing import Any, Dict, Tuple, List

from ..services.eval.omega import EvalKFS, promote_omega
from ..services.world_weights import world_weights

SOCK_PATH = "/tmp/devine_intel.sock"

def _read_all(conn: socket.socket) -> bytes:
    chunks: List[bytes] = []
    while True:
        data = conn.recv(65536)
        if not data:
            break
        chunks.append(data)
        if len(data) < 65536:
            break
    return b"".join(chunks)

def _handle(req: Dict[str, Any]) -> Dict[str, Any]:
    rpc = req.get("rpc")
    if rpc in ("Evaluate","Promote"):
        prev = req.get("prev","ABSENT")
        kfs_d = req.get("kfs", {}) or {}
        k = EvalKFS(
            m_cbd=float(kfs_d.get("m_cbd", 0.0)),
            m_cgt=float(kfs_d.get("m_cgt", 0.0)),
            m_nhy=float(kfs_d.get("m_nhy", 0.0)),
        )
        omega, meta = promote_omega(prev, k)
        if rpc == "Evaluate":
            return {"ok": True, "omega": omega, **meta}
        # Promote: include a tiny placeholder repair plan list
        repair: List[str] = []
        if meta["m_cgt"] < 0.70:
            repair.append("increase_governance_trust[m_cgt<0.70]")
        if meta["m_cbd"] < 0.60:
            repair.append("normalize_inputs[m_cbd<0.60]")
        if meta["m_nhy"] < 0.80:
            repair.append("validate_delivery_signal[m_nhy<0.80]")
        return {"ok": True, "omega": omega, "prev": meta["prev"], "next": meta["next"], "repair": repair}

    if rpc == "WorldWeights":
        strategy = req.get("strategy","degree")
        edges = req.get("edges", []) or []
        # edges may arrive as list[list[str,str]]
        edges_t = [(e[0], e[1]) for e in edges if isinstance(e, (list, tuple)) and len(e) == 2]
        wmap = world_weights(strategy=strategy, edges=edges_t, reliability=req.get("reliability", {}))
        worlds = [{"id": k, "w": float(v)} for k, v in sorted(wmap.items())]
        return {"ok": True, "w_model": strategy, "worlds": worlds}

    return {"ok": False, "error": "unsupported rpc", "supported": ["Evaluate","Promote","WorldWeights"]}

def run_shim(sock_path: str = SOCK_PATH) -> None:
    if os.path.exists(sock_path):
        os.remove(sock_path)

    srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    srv.bind(sock_path)
    srv.listen(32)

    # Best-effort tight perms: owner-only
    try:
        os.chmod(sock_path, 0o600)
    except Exception:
        pass

    print(f"[hdt-shim] listening on {sock_path}")
    while True:
        conn, _ = srv.accept()
        try:
            raw = _read_all(conn)
            req = json.loads(raw.decode("utf-8") if raw else "{}")
            resp = _handle(req)
        except Exception as e:
            resp = {"ok": False, "error": str(e)}
        conn.sendall(json.dumps(resp).encode("utf-8"))
        conn.close()

def main() -> None:
    run_shim()

if __name__ == "__main__":
    main()
