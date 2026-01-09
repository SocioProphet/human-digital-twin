"""IEML stub: encode core concepts with E,U,A,S,B,~T primitives.

This is a *placeholder* mapping. The goal is not to invent semantics in code,
but to prove the integration point: a semantic registry can be queried during
evaluation, policy explanation, and repair plan construction.

Best practice:
- treat this as a read-only mapping layer
- version it
- never mix ontology politics with runtime critical paths
"""
from typing import Dict

IEML_DICT: Dict[str, str] = {
    "Observation": "E.U",
    "Consent": "A.S",
    "Export": "B.T",
    "Linkage": "U.A",
}

def lookup(concept: str) -> str:
    return IEML_DICT.get(concept, "E")
