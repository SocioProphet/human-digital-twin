.PHONY: venv test fmt lint pathflows shim

venv:
	python3 -m venv .venv && . .venv/bin/activate && pip install -e '.[dev]'

test:
	. .venv/bin/activate && pytest -q

lint:
	. .venv/bin/activate && ruff check .

fmt:
	. .venv/bin/activate && ruff format .

pathflows:
	. .venv/bin/activate && hdt-pathflows tools/pathflows/examples.yaml

shim:
	. .venv/bin/activate && hdt-shim
