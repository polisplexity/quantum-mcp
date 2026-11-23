# Polisplexity Quantum MCP integration inventory

Edition 2026-11-22 · 44 entries.

Generated from [the source registry](../registry/tools.json).
The catalog includes deployment targets, connectors, dependencies,
reference tools and workloads. Each entry describes a proposed test.
See the [master record](../MASTER_TEST_RECORD.md) for observed results.

Decisions: pilot (first case), evaluate (near-term candidate), alternate
(substitute), dependency (used inside another tool), reference (human
or benchmark reference), research (later experiment).

## Contents

- [Qiskit MCP Server](#qiskit-mcp) — Qiskit ecosystem
- [Qiskit SDK](#qiskit-sdk) — Qiskit ecosystem
- [Qiskit Aer](#qiskit-aer) — Qiskit ecosystem
- [Qiskit IBM Runtime MCP](#qiskit-runtime-mcp) — Qiskit ecosystem
- [Qiskit IBM Transpiler MCP](#qiskit-transpiler-mcp) — Qiskit ecosystem
- [Qiskit Docs MCP](#qiskit-docs-mcp) — Qiskit ecosystem
- [Qiskit Gym MCP](#qiskit-gym-mcp) — Qiskit ecosystem
- [Qiskit Optimization Mapper](#qiskit-opt-mapper) — Optimization and validation
- [QAOA with Qiskit](#qaoa) — Optimization and validation
- [Classical exact enumeration](#exact-baseline) — Optimization and validation
- [OR-Tools CP-SAT](#or-tools) — Optimization and validation
- [HiGHS](#highs) — Optimization and validation
- [QOBLIB](#qoblib) — Optimization and validation
- [Urban MCP walking accessibility](#urban-walking) — Applications
- [OLDT Canvas](#oldt-canvas) — Applications
- [Google Cirq](#cirq) — Circuit SDKs and simulation
- [Google qsim](#qsim) — Circuit SDKs and simulation
- [PennyLane](#pennylane) — Circuit SDKs and simulation
- [PennyLane Lightning](#lightning) — Circuit SDKs and simulation
- [NVIDIA CUDA-Q](#cuda-q) — Circuit SDKs and simulation
- [NVIDIA cuQuantum](#cuquantum) — Circuit SDKs and simulation
- [QuTiP](#qutip) — Circuit SDKs and simulation
- [pytket](#pytket) — Circuit SDKs and simulation
- [Amazon Braket](#braket) — Physical and hosted execution
- [Azure Quantum](#azure-quantum) — Physical and hosted execution
- [IonQ](#ionq) — Physical and hosted execution
- [Quantinuum Nexus](#quantinuum) — Physical and hosted execution
- [Rigetti pyQuil and QCS](#rigetti) — Physical and hosted execution
- [IQM Client](#iqm) — Physical and hosted execution
- [D-Wave dimod](#dwave-dimod) — Annealing and hybrid optimization
- [D-Wave Leap](#dwave-leap) — Annealing and hybrid optimization
- [Pasqal Pulser](#pasqal-pulser) — Analog and photonic computing
- [QuEra via Braket AHS](#quera-ahs) — Analog and photonic computing
- [Quandela Perceval](#perceval) — Analog and photonic computing
- [OpenQASM 3](#openqasm) — Interchange and assurance
- [Quantum Intermediate Representation](#qir) — Interchange and assurance
- [Mitiq](#mitiq) — Interchange and assurance
- [Microsoft Quantum Resource Estimator](#resource-estimator) — Interchange and assurance
- [Polisplexity HPC simulation dispatch](#hpc-simulator-bridge) — Applications
- [Qiskit Experiments](#qiskit-experiments) — Interchange and assurance
- [Qiskit Nature](#qiskit-nature) — Scientific applications
- [OpenFermion](#openfermion) — Scientific applications
- [Microsoft QDK and Q#](#qsharp) — Circuit SDKs and simulation
- [MQT Bench](#mqt-bench) — Interchange and assurance

<a id="qiskit-mcp"></a>
## Qiskit MCP Server

**Family** — Qiskit ecosystem. **Decision** — pilot. **Status** — candidate.

- **Upstream interface** — Upstream MCP for circuit construction, transpilation and QASM/QPY export
- **Reuse** — Preserve upstream schemas, circuit references and serialization.
- **Build** — Add a supported tool profile and bind circuit IDs and inputs to experiment manifests.
- **Acceptance test** — Discover the tools in a fresh workspace, create and transpile a Bell circuit, export it, and compare with direct SDK usage. Check bad input and unsupported instructions.
- **Sources** — [Upstream source 1](https://raw.githubusercontent.com/Qiskit/mcp-servers/main/qiskit-mcp-server/README.md)

<a id="qiskit-sdk"></a>
## Qiskit SDK

**Family** — Qiskit ecosystem. **Decision** — pilot. **Status** — candidate.

- **Upstream interface** — QuantumCircuit, transpiler, Statevector and result schemas
- **Reuse** — Use the SDK for the direct reference calculation and compiled-circuit validation.
- **Build** — Pin SDK, target, seeds and classical-register decoding.
- **Acceptance test** — Check analytic Bell probabilities, circuit equivalence up to global phase where applicable and preservation of register order.
- **Sources** — [Upstream source 1](https://docs.quantum.ibm.com/api/qiskit)

<a id="qiskit-aer"></a>
## Qiskit Aer

**Family** — Qiskit ecosystem. **Decision** — pilot. **Status** — candidate.

- **Upstream interface** — AerSimulator for ideal, noisy and selected GPU simulation modes
- **Reuse** — Reuse native simulation methods, noise models and backend metadata.
- **Build** — Expose a narrow executor with recorded method, seed, shots and limits, and route its results back to the circuit record.
- **Acceptance test** — Compare exact ideal probabilities and seeded counts across direct and MCP runs. Run a separate noise-model fixture and verify its expected effect.
- **Sources** — [Upstream source 1](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)

<a id="qiskit-runtime-mcp"></a>
## Qiskit IBM Runtime MCP

**Family** — Qiskit ecosystem. **Decision** — evaluate. **Status** — candidate.

- **Upstream interface** — Upstream MCP with hardware discovery, primitives and jobs
- **Reuse** — Reuse published discovery, job and primitive contracts where access exists.
- **Build** — Preserve device, service job ID, primitive, limits and whether execution used a physical QPU.
- **Acceptance test** — Prove the local-testing path first. Later verify an authorized Bell run, native metadata and statistical checks with capped shots.
- **Sources** — [Upstream source 1](https://github.com/Qiskit/mcp-servers/blob/main/qiskit-ibm-runtime-mcp-server/README.md), [Upstream source 2](https://quantum.cloud.ibm.com/docs/en/guides/local-testing-mode)

<a id="qiskit-transpiler-mcp"></a>
## Qiskit IBM Transpiler MCP

**Family** — Qiskit ecosystem. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — Upstream transpiler service MCP
- **Reuse** — Reuse supported compilation when an authorized case needs it.
- **Build** — Record source/compiled hashes, backend target and circuit depth and two-qubit gate counts.
- **Acceptance test** — Compile the same fixture locally and through the service. Check target compatibility, numerical equivalence and unsupported-target errors.
- **Sources** — [Upstream source 1](https://github.com/Qiskit/mcp-servers/tree/main/qiskit-ibm-transpiler-mcp-server)

<a id="qiskit-docs-mcp"></a>
## Qiskit Docs MCP

**Family** — Qiskit ecosystem. **Decision** — reference. **Status** — candidate.

- **Upstream interface** — Read-only documentation MCP
- **Reuse** — Use original API and tutorial retrieval.
- **Build** — Retain source URL and SDK version relevant to a run; keep retrieval separate from execution evidence.
- **Acceptance test** — Resolve a known API query to the correct version and record failure when a historical version cannot be found.
- **Sources** — [Upstream source 1](https://github.com/Qiskit/mcp-servers/tree/main/qiskit-docs-mcp-server)

<a id="qiskit-gym-mcp"></a>
## Qiskit Gym MCP

**Family** — Qiskit ecosystem. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Community MCP for learning-based synthesis and routing
- **Reuse** — Reuse its supported environments and fixtures.
- **Build** — Map an admitted synthesis goal and separate circuit artifacts from generated policies.
- **Acceptance test** — Replay a small benchmark; compare equivalence and circuit cost against a conventional compiler on the same target.
- **Sources** — [Upstream source 1](https://github.com/Qiskit/mcp-servers/tree/main/qiskit-gym-mcp-server)

<a id="qiskit-opt-mapper"></a>
## Qiskit Optimization Mapper

**Family** — Optimization and validation. **Decision** — pilot. **Status** — candidate.

- **Upstream interface** — QUBO/Ising converters for supported formulations
- **Reuse** — Use published binary problem conversion and Hamiltonian tools.
- **Build** — Record mapping from site and coverage variables to bits, auxiliary variables, penalty and decoding.
- **Acceptance test** — Compare every feasible small assignment against a direct original-objective evaluator; include failed cardinality and overlap fixtures.
- **Sources** — [Upstream source 1](https://github.com/Qiskit/qiskit-opt-mapper)

<a id="qaoa"></a>
## QAOA with Qiskit

**Family** — Optimization and validation. **Decision** — pilot. **Status** — candidate.

- **Upstream interface** — QAOA ansatz, classical optimizer and sampler
- **Reuse** — Reuse existing algorithm blocks and the configured sampler.
- **Build** — Implement the bounded Helsinki experiment, explicit seeds and independent feasibility and score validation.
- **Acceptance test** — Compare fixed-seed runs to the exact optimum. Report objective gap, feasible and optimal sampling rates, shots and full time.
- **Sources** — [Upstream source 1](https://quantum.cloud.ibm.com/docs/en/tutorials/quantum-approximate-optimization-algorithm)

<a id="exact-baseline"></a>
## Classical exact enumeration

**Family** — Optimization and validation. **Decision** — pilot. **Status** — candidate.

- **Upstream interface** — Python combinations and exact scoring of the original objective
- **Reuse** — Use the standard library and a versioned distance matrix.
- **Build** — Create the independent oracle with ties and set-union coverage.
- **Acceptance test** — Verify all 28 choices for two sites out of eight, with fixtures for ties, unreachable schools and no double counting.
- **Sources** — [Upstream source 1](https://docs.python.org/3/library/itertools.html#itertools.combinations)

<a id="or-tools"></a>
## OR-Tools CP-SAT

**Family** — Optimization and validation. **Decision** — evaluate. **Status** — candidate.

- **Upstream interface** — Integer and Boolean constraints, status and bounds
- **Reuse** — Use CP-SAT to scale the classical comparator.
- **Build** — Model the same coverage and preserve solver bounds, time limits and status.
- **Acceptance test** — Match exhaustive results on small cases and report feasible versus proved optimal on a larger case.
- **Sources** — [Upstream source 1](https://developers.google.com/optimization/cp/cp_solver/)

<a id="highs"></a>
## HiGHS

**Family** — Optimization and validation. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — LP/MIP solver
- **Reuse** — Use the native integer solver as a second comparator.
- **Build** — Encode the same scoring problem and preserve tolerance and bound metadata.
- **Acceptance test** — Compare exact objectives and admissible ties with enumeration and CP-SAT.
- **Sources** — [Upstream source 1](https://highs.dev/)

<a id="qoblib"></a>
## QOBLIB

**Family** — Optimization and validation. **Decision** — evaluate. **Status** — candidate.

- **Upstream interface** — Published benchmark instances and comparison evidence
- **Reuse** — Select versioned instances and review their individual reuse terms.
- **Build** — Map fixture identity, known bounds and solver settings to run records.
- **Acceptance test** — Reproduce a supported small instance and label observed and published metrics separately.
- **Sources** — [Upstream source 1](https://github.com/ZIB-AOPT/QOBLIB)

<a id="urban-walking"></a>
## Urban MCP walking accessibility

**Family** — Applications. **Decision** — pilot. **Status** — candidate.

- **Upstream interface** — Existing OSMnx case, licensed snapshots and rules
- **Reuse** — Reuse the Helsinki network, mapped school IDs, snap rules and provenance.
- **Build** — Compute a new school-to-candidate matrix with eight documented hypothetical sites.
- **Acceptance test** — Compare routes and matrix orientation with native OSMnx; verify unreachable values, threshold behavior, coverage IDs and attribution.
- **Sources** — [Upstream source 1](https://github.com/polisplexity/urban-mcp/tree/main/cases/two-city-walking)

<a id="oldt-canvas"></a>
## OLDT Canvas

**Family** — Applications. **Decision** — evaluate. **Status** — candidate.

- **Upstream interface** — Versioned studies and scenario results
- **Reuse** — Reuse supported import and revision contracts.
- **Build** — Convert validated placements to inspectable GeoJSON bound to an alternative.
- **Acceptance test** — Open the result in a test Twin and verify site identities, geometry, revision and separation from the baseline.
- **Sources** — [Upstream source 1](https://polisplexity.tech/products/open-local-digital-twin)

<a id="cirq"></a>
## Google Cirq

**Family** — Circuit SDKs and simulation. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — Cirq circuits, simulator and devices
- **Reuse** — Reuse the native SDK and device constraints.
- **Build** — Map compatible circuits and retain measurement keys and qubit order.
- **Acceptance test** — Compare ideal probabilities for equivalent circuits and reject unsupported gates explicitly.
- **Sources** — [Upstream source 1](https://quantumai.google/cirq)

<a id="qsim"></a>
## Google qsim

**Family** — Circuit SDKs and simulation. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Cirq-compatible state-vector simulator
- **Reuse** — Reuse native CPU and supported GPU simulation.
- **Build** — Expose a profile only for a measurable supported workload.
- **Acceptance test** — Compare probabilities with Cirq and record time and memory as qubits or circuit counts grow.
- **Sources** — [Upstream source 1](https://quantumai.google/qsim)

<a id="pennylane"></a>
## PennyLane

**Family** — Circuit SDKs and simulation. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — QNodes, devices and hybrid differentiation
- **Reuse** — Use QNodes and a supported device and gradient method.
- **Build** — Register a bounded variational experiment with versioned configuration.
- **Acceptance test** — Check one expectation and gradient against analytic or finite-difference results, then compare direct and MCP paths.
- **Sources** — [Upstream source 1](https://docs.pennylane.ai/en/stable/)

<a id="lightning"></a>
## PennyLane Lightning

**Family** — Circuit SDKs and simulation. **Decision** — research. **Status** — candidate.

- **Upstream interface** — CPU, GPU and tensor simulator devices; supported MPI modes
- **Reuse** — Use existing device plugins and simulation options.
- **Build** — Bind device, precision, mode and resource limits to the local GPU or HPC job.
- **Acceptance test** — Compare CPU results with a permitted GPU or MPI path and record precision and any approximation.
- **Sources** — [Upstream source 1](https://docs.pennylane.ai/projects/lightning/en/stable/index.html)

<a id="cuda-q"></a>
## NVIDIA CUDA-Q

**Family** — Circuit SDKs and simulation. **Decision** — evaluate. **Status** — candidate.

- **Upstream interface** — Circuit kernels and simulation and physical targets
- **Reuse** — Use native target selection, libraries and measured results.
- **Build** — Add a recipe dispatchable to local GPU or HPC with precisely identified backend and parallel settings.
- **Acceptance test** — Compare Bell and parameterized fixtures across supported CPU/GPU paths before testing authorized distributed execution.
- **Sources** — [Upstream source 1](https://nvidia.github.io/cuda-quantum/latest/using/backends/simulators.html)

<a id="cuquantum"></a>
## NVIDIA cuQuantum

**Family** — Circuit SDKs and simulation. **Decision** — dependency. **Status** — candidate.

- **Upstream interface** — cuStateVec and cuTensorNet
- **Reuse** — Reuse the dependency supported by the selected simulator.
- **Build** — Record library, method, version and compatible resources in the parent recipe.
- **Acceptance test** — Verify that the parent simulator identifies its mode and agrees with a known CPU reference within tolerance.
- **Sources** — [Upstream source 1](https://docs.nvidia.com/cuda/cuquantum/latest/)

<a id="qutip"></a>
## QuTiP

**Family** — Circuit SDKs and simulation. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Quantum dynamics and open-system solvers
- **Reuse** — Use the native solvers for an admitted dynamics or noise reference.
- **Build** — Add a bounded recipe for Hamiltonian, time and observables.
- **Acceptance test** — Compare a two-level system to the analytic result and preserve time and measurement units.
- **Sources** — [Upstream source 1](https://qutip.readthedocs.io/en/stable/)

<a id="pytket"></a>
## pytket

**Family** — Circuit SDKs and simulation. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — Compiler and target extensions
- **Reuse** — Use native compiler passes and the chosen provider extension.
- **Build** — Preserve target and settings, layout, source and result circuit hashes.
- **Acceptance test** — Check ideal equivalence for a fixture and target-specific errors for unsupported gates.
- **Sources** — [Upstream source 1](https://docs.quantinuum.com/tket/)

<a id="braket"></a>
## Amazon Braket

**Family** — Physical and hosted execution. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — SDK, managed simulators, devices and Hybrid Jobs
- **Reuse** — Reuse provider APIs and native device and job metadata.
- **Build** — Bind backend and job type, lifecycle, S3 result references and reported resource consumption.
- **Acceptance test** — Use an authorized simulator fixture, verify native artifacts and status, then require a capped physical fixture for QPU support.
- **Sources** — [Upstream source 1](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html), [Upstream source 2](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs.html)

<a id="azure-quantum"></a>
## Azure Quantum

**Family** — Physical and hosted execution. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — Workspace targets and native job APIs
- **Reuse** — Reuse an approved provider route and supported job format.
- **Build** — Record target, input format, workspace scope and artifact identity.
- **Acceptance test** — Compare an authorized simulator fixture with the local reference and verify failure or expiry reconciliation.
- **Sources** — [Upstream source 1](https://learn.microsoft.com/en-us/azure/quantum/qc-target-list)

<a id="ionq"></a>
## IonQ

**Family** — Physical and hosted execution. **Decision** — research. **Status** — candidate.

- **Upstream interface** — IonQ API and selected provider route
- **Reuse** — Reuse circuit limits, native gates and job records from one supported route.
- **Build** — Normalize supported circuit features without hiding native results or uncertainty.
- **Acceptance test** — Check an ideal fixture with the supported simulator and verify a bounded physical sample with stated statistical criteria.
- **Sources** — [Upstream source 1](https://docs.ionq.com/)

<a id="quantinuum"></a>
## Quantinuum Nexus

**Family** — Physical and hosted execution. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Nexus and supported compiler and emulator interfaces
- **Reuse** — Reuse the selected workspace and native compilation and measurement metadata.
- **Build** — Record compiler settings, circuit target and permissions.
- **Acceptance test** — Use an authorized emulator to verify a small circuit and target restrictions before validating a physical run.
- **Sources** — [Upstream source 1](https://docs.quantinuum.com/nexus/)

<a id="rigetti"></a>
## Rigetti pyQuil and QCS

**Family** — Physical and hosted execution. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Quil, pyQuil and provider routes
- **Reuse** — Use native circuit tools and the selected simulator or service.
- **Build** — Track circuit format, provider ID and target-specific restrictions and calibration when provided.
- **Acceptance test** — Compare a direct simulation with the tool output, then verify compiled gates against an authorized target before submission.
- **Sources** — [Upstream source 1](https://pyquil-docs.rigetti.com/)

<a id="iqm"></a>
## IQM Client

**Family** — Physical and hosted execution. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Native circuit client and supported device routes
- **Reuse** — Reuse native circuit validation and submission.
- **Build** — Preserve device, calibration when available, mapping and native status.
- **Acceptance test** — Verify allowed and unsupported gate/layout fixtures and compare a permitted sample with a simulator reference.
- **Sources** — [Upstream source 1](https://docs.meetiqm.com/iqm-client/)

<a id="dwave-dimod"></a>
## D-Wave dimod

**Family** — Annealing and hybrid optimization. **Decision** — evaluate. **Status** — candidate.

- **Upstream interface** — BQM/CQM representations and exact local samplers
- **Reuse** — Use model objects and local exact samplers.
- **Build** — Map site IDs and coverage to variables and decode back to the original score.
- **Acceptance test** — Compare every returned valid result to the exhaustive evaluator and verify conflicts, constraints and alternative optima.
- **Sources** — [Upstream source 1](https://docs.dwavequantum.com/en/latest/ocean/stack.html)

<a id="dwave-leap"></a>
## D-Wave Leap

**Family** — Annealing and hybrid optimization. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — Direct QPU and hybrid samplers
- **Reuse** — Use published sampler and limit interfaces.
- **Build** — Keep direct quantum annealing and hybrid method IDs, embedding or constraints, limits and reported timing.
- **Acceptance test** — Compare valid results and optimality gaps to an exact reference, check over-limit handling and preserve reported timings.
- **Sources** — [Upstream source 1](https://docs.dwavequantum.com/en/latest/ocean/api_ref_system/samplers.html)

<a id="pasqal-pulser"></a>
## Pasqal Pulser

**Family** — Analog and photonic computing. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Pulse sequences, emulator and remote backends
- **Reuse** — Reuse native device and sequence validation and supported emulation.
- **Build** — Create a modality-specific record with array geometry, units and pulse sequence.
- **Acceptance test** — Run a small documented emulator case and reject invalid geometry before execution, comparing observables to the published reference.
- **Sources** — [Upstream source 1](https://docs.pasqal.com/pulser/v1.0.0/tutorials/backends/)

<a id="quera-ahs"></a>
## QuEra via Braket AHS

**Family** — Analog and photonic computing. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Braket Analog Hamiltonian Simulation
- **Reuse** — Use native analog SDK and an authorized device or simulator route.
- **Build** — Record atom geometry, control waveform, shots and execution target.
- **Acceptance test** — Compare a small fixture with an independent emulator and verify physical execution reports sampling and device constraints.
- **Sources** — [Upstream source 1](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html)

<a id="perceval"></a>
## Quandela Perceval

**Family** — Analog and photonic computing. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Optical circuits and photonic simulators
- **Reuse** — Use original circuits, processors and sampling interfaces.
- **Build** — Keep modes, photon input and post-selection in a photonics-specific manifest.
- **Acceptance test** — Check an analytic two-mode beam-splitter example and distinguish total from post-selected events.
- **Sources** — [Upstream source 1](https://perceval.quandela.net/Perceval-Whitepaper.pdf)

<a id="openqasm"></a>
## OpenQASM 3

**Family** — Interchange and assurance. **Decision** — dependency. **Status** — candidate.

- **Upstream interface** — Circuit language and versioned feature set
- **Reuse** — Reuse the supported SDK parser or exporter.
- **Build** — Track program version and supported features and errors.
- **Acceptance test** — Round-trip a known circuit and compare semantics; explicitly reject unsupported constructs and register ordering conflicts.
- **Sources** — [Upstream source 1](https://openqasm.com/)

<a id="qir"></a>
## Quantum Intermediate Representation

**Family** — Interchange and assurance. **Decision** — dependency. **Status** — candidate.

- **Upstream interface** — LLVM IR representation and profile definitions
- **Reuse** — Use provider-supported compiler and profile definitions.
- **Build** — Record profile and compiler version and verify advertised capabilities.
- **Acceptance test** — Pass a compatible fixture and produce a clear failure for an unsupported profile.
- **Sources** — [Upstream source 1](https://www.qir-alliance.org/qir-book/concepts/what-is-qir.html)

<a id="mitiq"></a>
## Mitiq

**Family** — Interchange and assurance. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Error-mitigation toolkit and frontends
- **Reuse** — Reuse supported mitigation methods and preserve original measurements.
- **Build** — Record variants, fitting choices, seeds and additional shots.
- **Acceptance test** — Check noisy expected values against an ideal reference, comparing raw and mitigated estimates across seeds with uncertainty and overhead.
- **Sources** — [Upstream source 1](https://mitiq.readthedocs.io/en/stable/)

<a id="resource-estimator"></a>
## Microsoft Quantum Resource Estimator

**Family** — Interchange and assurance. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Resource estimation with explicit architecture assumptions
- **Reuse** — Reuse estimator and compatible input tooling.
- **Build** — Preserve qubit and error-model assumptions, estimated units and version.
- **Acceptance test** — Repeat a documented estimate and change one hardware assumption to verify both the result and its provenance.
- **Sources** — [Upstream source 1](https://learn.microsoft.com/en-us/azure/quantum/intro-to-resource-estimation)

<a id="hpc-simulator-bridge"></a>
## Polisplexity HPC simulation dispatch

**Family** — Applications. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Versioned experiment plus HPC job and artifact manifests
- **Reuse** — Reuse the simulator and the HPC adapter's lifecycle.
- **Build** — Bind experiment ID, circuit hash and simulator settings to the HPC receipt and re-import results.
- **Acceptance test** — Run the same small circuit locally and after HPC dispatch, compare probabilities and retain both run records.
- **Sources** — [Upstream source 1](https://nvidia.github.io/cuda-quantum/latest/using/backends/simulators.html)

<a id="qiskit-experiments"></a>
## Qiskit Experiments

**Family** — Interchange and assurance. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Existing experiment definitions and analysis for characterization
- **Reuse** — Reuse a documented characterization or tomography experiment and its analysis tools.
- **Build** — Keep circuit families, run dates, shots, uncertainties and device configuration with the outcome.
- **Acceptance test** — Run a synthetic calibration fixture with a known signal. Verify fitted values, uncertainty and native/MCP parity.
- **Sources** — [Upstream source 1](https://github.com/qiskit-community/qiskit-experiments)

<a id="qiskit-nature"></a>
## Qiskit Nature

**Family** — Scientific applications. **Decision** — research. **Status** — candidate.

- **Upstream interface** — Quantum chemistry and other scientific problem mapping
- **Reuse** — Use native second-quantized operators and supported mappings for a specific small problem.
- **Build** — Bind source problem data, basis, mapper and reference energy to an experiment recipe.
- **Acceptance test** — Compare a reproducible small molecule case against classical exact diagonalization and validate energy units and symmetry assumptions.
- **Sources** — [Upstream source 1](https://github.com/qiskit-community/qiskit-nature)

<a id="openfermion"></a>
## OpenFermion

**Family** — Scientific applications. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — Fermionic operators and mappings to qubit operators
- **Reuse** — Reuse operator construction and a supported transformation for an independent reference.
- **Build** — Preserve operator ordering, basis and source data identity in an application-specific contract.
- **Acceptance test** — Compare an analytically known small operator before and after mapping and reproduce its spectral reference.
- **Sources** — [Upstream source 1](https://quantumai.google/openfermion/)

<a id="qsharp"></a>
## Microsoft QDK and Q#

**Family** — Circuit SDKs and simulation. **Decision** — alternate. **Status** — candidate.

- **Upstream interface** — Q# programs and documented local simulators and tooling
- **Reuse** — Use the QDK compiler and supported simulators for Q#-native recipes.
- **Build** — Record program and compiler version, simulation target and exchange capabilities for the chosen workload.
- **Acceptance test** — Run a fixed two-qubit example locally and compare the emitted measurements with the analytic distribution and a second simulator.
- **Sources** — [Upstream source 1](https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview)

<a id="mqt-bench"></a>
## MQT Bench

**Family** — Interchange and assurance. **Decision** — evaluate. **Status** — candidate.

- **Upstream interface** — Versioned quantum circuit benchmark generation
- **Reuse** — Reuse supported circuit families and abstraction levels as compiler and simulator fixtures.
- **Build** — Store benchmark name, level, program and exact settings in the experiment manifest.
- **Acceptance test** — Generate a small circuit twice at a pinned version and verify source/compiled equivalence and reported circuit metrics.
- **Sources** — [Upstream source 1](https://mqt.readthedocs.io/projects/bench/en/stable/)
