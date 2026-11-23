# RFC 0001 · Reproducible quantum experiments

Proposed · 2026-11-22.

## Product boundary

The product connects a versioned scientific formulation to an execution target
and an independent reference. It reuses native SDKs, simulators, provider APIs
and MCPs. The first composition is Qiskit MCP for circuits and Aer for local
execution.

## Proposed operations

- Discover available execution targets, supported input modes and limits.
- Validate an experiment and the exact backend capabilities it requires.
- Prepare and compile where applicable, preserving source and execution inputs.
- Submit, query and collect a run with stable local and provider identifiers.
- Compare samples or solutions with the reference, and expose checked artifacts.

Tag inputs by modality: gate circuit, annealing/optimization model, analog
sequence or photonic circuit. Keep provider metadata, native errors and execution
kind (classical reference, ideal/noisy simulation, hybrid service or physical
device) on the result. Where supported, record estimates and assumptions
separately from measured costs or resource use.

## Initial work

1. Pin upstream versions and validate native and MCP circuit preparation.
2. Compare native and MCP Aer results on ideal and simple noisy fixtures.
3. Freeze an attributed Helsinki network and candidate sites, produce the
   distance matrix and independently score all 28 feasible pairs.
4. Verify the binary model against the original objective, then run the same
   QAOA recipe through direct and MCP routes. Review artifacts and agent claims
   in fresh Codex and Hermes workspaces.
5. Evaluate physical or additional modalities only with a test matched to their
   documented capabilities and access.
