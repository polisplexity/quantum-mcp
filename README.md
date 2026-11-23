# Polisplexity Quantum MCP

Open project for letting MCP-capable clients prepare, execute and verify
reproducible quantum computing experiments alongside classical references.

Start with the [integration inventory](docs/INVENTORY.md), the first
[Qiskit/Helsinki case](cases/qiskit-helsinki/README.md) and
[the architecture proposal](docs/rfc/0001-quantum-experiment-contract.md).
See [the master record](MASTER_TEST_RECORD.md) for evidence and outstanding runs.

The first path composes the native Qiskit MCP, Qiskit SDK and Aer. The
urban benchmark joins a Helsinki walking network and a small site-selection
instance to a classical exact reference. Circuit, annealing, analog and
photonic experiments have distinct inputs and execution semantics.

## Current stage

Research inventory and bounded pilot. The original Qiskit MCP prepared a Bell
circuit over stdio and the Aer fixture MCP produced the same ideal and noisy
samples as the direct reference with matched seeds. The Helsinki optimization
case and physical hardware remain planned.
The catalog verifier needs Python 3.10 or later and the standard library.

```sh
python tools/validate_inventory.py
```

Original project material is offered under [MIT](LICENSE). See
[how to contribute](CONTRIBUTING.md).
