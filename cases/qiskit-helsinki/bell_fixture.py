"""Bounded two-qubit Aer fixture, shared by the native and MCP paths."""

import hashlib
import re

from qiskit import qasm2
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, ReadoutError


BELL_QASM = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg m[2];
h q[0];
cx q[0],q[1];
measure q[0] -> m[0];
measure q[1] -> m[1];
"""
SHOTS = 1024
SEED = 8142


def simulate(qasm_text, noisy=False):
    if len(qasm_text) > 2048:
        raise ValueError("Pilot only accepts the bounded two-qubit fixture")
    registers = re.findall(r"\b(qreg|creg)\s+[a-zA-Z_]\w*\s*\[\s*(\d+)\s*\]", qasm_text)
    if sorted(registers) != [("creg", "2"), ("qreg", "2")]:
        raise ValueError("Expected one two-bit register of each kind")
    circuit = qasm2.loads(qasm_text, include_path=())
    if circuit.num_qubits != 2 or circuit.num_clbits != 2 or circuit.size() > 8:
        raise ValueError("Pilot only accepts a small measured two-qubit circuit")
    if any(entry.operation.name not in {"h", "cx", "measure", "barrier"} for entry in circuit.data):
        raise ValueError("Fixture includes an unsupported gate")
    ideal = Statevector.from_instruction(circuit.remove_final_measurements(inplace=False))
    probabilities = {key: round(float(ideal.probabilities_dict().get(key, 0)), 12)
                     for key in ("00", "01", "10", "11")}
    options = {"method": "density_matrix", "max_parallel_threads": 1}
    if noisy:
        noise = NoiseModel()
        noise.add_all_qubit_readout_error(ReadoutError([[0.9, 0.1], [0.1, 0.9]]))
        options["noise_model"] = noise
    sim = AerSimulator(**options)
    counts = dict(sorted(sim.run(circuit, shots=SHOTS, seed_simulator=SEED).result().get_counts().items()))
    return {
        "execution_kind": "noisy-simulation" if noisy else "ideal-simulation",
        "qasm_sha256": hashlib.sha256(qasm_text.encode()).hexdigest(),
        "seed_simulator": SEED,
        "shots": SHOTS,
        "ideal_probabilities": probabilities,
        "counts": counts,
    }
