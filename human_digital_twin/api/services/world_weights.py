"""World weights (possible-worlds) model.

We model "worlds" as competing interpretations/routes for an artifact or action.
A world weight function is used to allocate attention, compute expected value,
or choose what to try next under uncertainty.

Default strategy: **degree-based weighting** over an edge list.

This is intentionally small and pure so it can be reused:
- inside a TritRPC method,
- inside a batch evaluator,
- inside an audit replay.

"""
from typing import Dict, List, Tuple

def degree_weights(graph_edges: List[Tuple[str, str]]) -> Dict[str, float]:
    deg: Dict[str, float] = {}
    for u, v in graph_edges:
        deg[u] = deg.get(u, 0.0) + 1.0
        deg[v] = deg.get(v, 0.0) + 1.0
    total = sum(deg.values()) or 1.0
    return {k: v/total for k, v in deg.items()}

def world_weights(strategy: str, **kwargs) -> Dict[str, float]:
    if strategy == "degree":
        return degree_weights(kwargs.get("edges", []))
    if strategy == "empirical":
        # Placeholder: combine degree with reliability r in [0,1]
        edges = kwargs.get("edges", [])
        rel = kwargs.get("reliability", {})
        base = degree_weights(edges)
        mixed = {k: base.get(k,0.0)*(0.5+0.5*float(rel.get(k,0.5))) for k in base}
        s = sum(mixed.values()) or 1.0
        return {k: v/s for k,v in mixed.items()}
    return {}
