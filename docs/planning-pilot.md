# Planning Pilot: Abstract Export Repair

This pilot binds the abstract-reasoning governance slice into the Human Digital Twin (HDT) repository.

## Why this pilot exists

HDT already models readiness as a small governed lattice rather than a single scalar score.
This makes it a suitable consumer for explicit planning, rule verification, counterexample search, and backtracking.

The pilot tests one narrow scenario:
- a human-centric export request exists,
- coherence is sufficient,
- consent evidence is stale,
- a planner must decide whether to export, repair consent, defer, or escalate.

The pilot treats this as an `ABSTRACT` reasoning lane rather than a plain retrieval lane.

## Core rule

The export branch is not admissible solely because a language model proposes it.

The selected branch must be backed by:
- a branch-admissibility policy,
- a declared verification mode,
- a program-candidate or equivalent rule representation,
- a counterexample search result,
- a replan path if validation fails.

## Pilot outputs

The pilot produces or references:
- `AbstractBenchmarkCase`
- `PlanNode`
- `ProgramCandidateArtifact`
- `CounterexampleArtifact`
- `ControlGateArtifact`
- `AbstractBenchmarkRun`
- `AbstractBenchmarkReport`

## Success condition

The pilot is successful when:
- llm-only export is denied,
- repair-consent is selected as the admissible branch,
- a counterexample can force backtracking when the candidate rule is wrong,
- the final run and report remain traceable to policy, verification, and evidence artifacts.
