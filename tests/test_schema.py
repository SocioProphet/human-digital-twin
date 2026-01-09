import json
from jsonschema import validate
from human_digital_twin.api.services.eval.omega import EvalKFS, promote_omega
from pathlib import Path

def test_kfs_eval_schema_validates():
    schema = json.loads(Path("human_digital_twin/api/schemas/kfs-eval.json").read_text(encoding="utf-8"))
    omega, meta = promote_omega("ABSENT", EvalKFS(m_cbd=0.8, m_cgt=0.8, m_nhy=0.6))
    doc = {
        "url": "https://socioprophet.dev/ext/kfs-eval",
        "valueCoding": {"system": "Ω", "code": omega},
        "extension": [
            {"url": "m_cbd", "valueDecimal": meta["m_cbd"]},
            {"url": "m_cgt", "valueDecimal": meta["m_cgt"]},
            {"url": "m_nhy", "valueDecimal": meta["m_nhy"]},
        ],
    }
    validate(instance=doc, schema=schema)
