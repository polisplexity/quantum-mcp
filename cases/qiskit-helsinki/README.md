# Qiskit / Helsinki quantum pilot

Pilot acceptance plan and first results · 2026-11-22.

## Part 1. Reuse Qiskit and prove the circuit path

- Pin [Qiskit MCP](https://github.com/Qiskit/mcp-servers/blob/main/qiskit-mcp-server/README.md),
  the Qiskit SDK and [Aer](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html).
  Discover actual callable operations. Reuse upstream tools for circuit
  creation, transpilation and export. Bridge Aer execution if it is absent
  from the selected upstream tool profile.
- Use a Bell-state fixture and a distinct unsupported-input fixture. The ideal
  probability reference is P(00) = P(11) = 1/2 and P(01) = P(10) = 0.
  Compare exact probabilities and matched seeded sampling under the same
  backend and options. Confirm circuit identity, register order and exports.
- Verify a second run with a declared noise model. Save raw counts and the
  noise configuration. Validate bounds for stochastic comparisons in advance.
  Run the same supported sequence through direct tools and actual MCP.

### Observed Bell result

The [2026-11-22 receipt](evidence/bell-20261122.json) records the original
Qiskit MCP calls and native versus MCP parity through the Aer fixture. The
ideal simulator produced 507 occurrences of 00 and 517 of 11 in 1,024 shots.
The independent 10% per-bit readout error simulation produced 162 odd-parity
outcomes in 1,024 shots. The exact ideal distribution used for acceptance
assigns probability 0.5 to each of 00 and 11.

```sh
# Python 3.11 or later, inside a virtual environment.
python -m pip install -r cases/qiskit-helsinki/requirements-pilot.txt
python cases/qiskit-helsinki/run_bell_pilot.py
```

## Part 2. Compare a small urban optimization problem

Question: which two of eight explicitly hypothetical public-service sites
reach the most mapped schools within 1,200 m walking distance in the study
area? Reuse the licensed frozen [Urban MCP walking case](https://github.com/polisplexity/urban-mcp/tree/main/cases/two-city-walking).
Produce a new versioned school-to-site distance matrix. Preserve road-network
and snapped identities, unreachable origins, distance units, and OSM
attribution. These are mapped objects and modeled distances.

1. Independently enumerate 28 legal pairs. The score is the union of schools
   covered by either site. Preserve all tied best pairs. Include fixtures for
   ties, overlap, exactly-at-threshold and unreachable distances.
2. Use binary site selections, enforce exactly two sites and score coverage at
   most once per school. Record the bit and variable mapping, original objective,
   allowed inputs and any auxiliary variables or penalties. Verify no optimum
   of the encoded model violates the original cardinality or coverage rules.
3. Check the actual encoded qubit count, circuit depth and runtime budget
   before using a simulator. An eight-site input can require additional
   coverage or slack variables. If the full version exceeds the budget,
   first run a preregistered small coverage fixture and label that scope
   explicitly. A circuit encoding precomputed scores for the 28 pairs can
   test transport and decoding, with the classical preprocessing accounted
   for separately.
4. Run the selected QAOA recipe across fixed seeds. Decode and validate every
   reported solution against the original objective. Report best feasible
   score, gap to exact optimum, feasible/optimal sample rates, total shots,
   iterations and full time. Preserve compilation and model-preparation costs.
5. Return the supported candidate sites and coverage as a reviewable artifact.
   Confirm two selected site IDs, covered school IDs, units and provenance.
   Test the same versioned task with fresh Codex and Hermes workspaces and
   compare numerical artifacts, as well as the claims in each response.

## Physical execution

A scoped physical-QPU experiment is a later case. Record target, transpilation,
shots and calibration metadata when available, and compare distributions using
a criterion fixed before running. The Aer pilot evaluates a simulator path.
The Helsinki optimization and physical-QPU test are pending.
