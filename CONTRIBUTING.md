# Contributing

We keep the scope narrow: protocol surface + reference implementation.

Guidelines:
- Prefer deterministic, pure functions for core logic (easy replay).
- Add tests for every new threshold or policy.
- Keep dependencies minimal and open-source.
- No cloud assumptions. Local-first, reproducible by default.
