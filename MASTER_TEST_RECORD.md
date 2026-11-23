# Quantum MCP master test record

Edition: 2026-11-22.

| Scope | Status | Evidence boundary |
|---|---|---|
| Qiskit native MCP, SDK and Aer | Documented upstream | [Qiskit MCP](https://github.com/Qiskit/mcp-servers) and [Aer](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html) publish interfaces. |
| Inventory metadata | Local verification | The registry and generated inventory can be checked with the included validator. |
| Native and MCP Bell fixture | Passed 2026-11-22 | [Bell receipt](cases/qiskit-helsinki/evidence/bell-20261122.json). Original Qiskit MCP parsed, transpiled and exported the circuit. The local Aer MCP matched direct sampling in the ideal and noisy runs. Invalid QASM and oversized input were rejected. Early client attempts expected structuredContent, although the successful response was provided as a JSON text block. Both response forms are now handled. |
| Helsinki distance matrix and classical oracle | Planned | The adapted candidate-site matrix and reference are separate work from the existing walking case. |
| QAOA, agent reviews and physical QPU | Pending | Record simulation and hardware evidence independently. |

Record circuit or model hash, backend and mode, settings, seed where supported,
shots, error model or calibration evidence, elapsed and provider-reported time,
measurement uncertainty, artifact hashes, original objective and constraint
checks. A statistical result needs a declared acceptance criterion and sample
budget. Keep the native, actual MCP and agent evidence distinct.
