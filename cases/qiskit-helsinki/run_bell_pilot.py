"""Exercise original Qiskit MCP preparation and bounded Aer MCP execution."""

import argparse
import asyncio
from contextlib import AsyncExitStack
import importlib.metadata
import json
from pathlib import Path
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from bell_fixture import BELL_QASM, SHOTS, simulate


async def open_session(stack, args):
    config = StdioServerParameters(command=sys.executable, args=args)
    read, write = await stack.enter_async_context(stdio_client(config))
    session = await stack.enter_async_context(ClientSession(read, write))
    await session.initialize()
    return session


async def call(session, name, arguments):
    result = await session.call_tool(name, arguments)
    if result.isError:
        message = " ".join(block.text for block in result.content if block.type == "text")
        raise RuntimeError(f"MCP operation failed: {name}: {message[:500]}")
    payload = result.structuredContent
    if payload is None and len(result.content) == 1 and result.content[0].type == "text":
        payload = json.loads(result.content[0].text)
    if not isinstance(payload, dict):
        raise ValueError(f"MCP operation returned no JSON object: {name}")
    return payload


async def check():
    analytical = {"00": 0.5, "01": 0.0, "10": 0.0, "11": 0.5}
    async with AsyncExitStack() as stack:
        qiskit = await open_session(stack, ["-c", "from qiskit_mcp_server.server import main; main()"])
        aer = await open_session(stack, [str(Path(__file__).with_name("aer_fixture_mcp.py"))])
        upstream_tools = [tool.name for tool in (await qiskit.list_tools()).tools]

        load_args = {"qasm_string": BELL_QASM, "qasm_version": "2.0"}
        loaded = await call(qiskit, "load_circuit_from_qasm_tool", load_args)
        compiled = await call(qiskit, "transpile_circuit_tool", {
            "circuit": loaded["circuit_qpy"], "circuit_format": "qpy",
            "basis_gates": ["h", "cx"], "optimization_level": 0, "seed_transpiler": 8142,
        })
        exported = await call(qiskit, "export_circuit_to_qasm_tool", {
            "circuit_qpy": compiled["transpiled_circuit"]["circuit_qpy"], "qasm_version": "2.0",
        })
        invalid = await call(qiskit, "load_circuit_from_qasm_tool", {
            **load_args, "qasm_string": "not a circuit",
        })
        denied = await aer.call_tool("sample_bell_fixture", {"qasm_text": "x" * 2049})
        oversize_register = await aer.call_tool("sample_bell_fixture", {
            "qasm_text": BELL_QASM.replace("qreg q[2]", "qreg q[999999]"),
        })
        if invalid["status"] != "error" or not denied.isError or not oversize_register.isError:
            raise ValueError("An invalid circuit fixture was accepted")

        runs = []
        for noisy in (False, True):
            native = simulate(BELL_QASM, noisy)
            observed = await call(aer, "sample_bell_fixture", {
                "qasm_text": exported["qasm_string"], "noisy": noisy,
            })
            if observed["ideal_probabilities"] != analytical:
                raise ValueError("Transpiled circuit differs from the analytical reference")
            if observed["counts"] != native["counts"]:
                raise ValueError("Matched native and MCP samples differ")
            counts = observed["counts"]
            odd_fraction = (counts.get("01", 0) + counts.get("10", 0)) / SHOTS
            if sum(counts.values()) != SHOTS:
                raise ValueError("Incomplete sampling")
            if noisy and not 0.10 <= odd_fraction <= 0.26:
                raise ValueError("Noisy samples are inconsistent with 10% independent readout error")
            if not noisy and (odd_fraction or abs(counts.get("00", 0) / SHOTS - 0.5) > 0.07):
                raise ValueError("Ideal samples are inconsistent with a Bell distribution")
            runs.append({**observed, "native_parity": True, "odd_fraction": odd_fraction})

        return {
            "transport": "stdio", "fixture": "measured two-qubit Bell circuit",
            "dependency_versions": {p: importlib.metadata.version(p)
                                    for p in ("qiskit", "qiskit-aer", "qiskit-mcp-server", "mcp")},
            "upstream_tools": upstream_tools,
            "upstream_preparation": ["load_circuit_from_qasm_tool", "transpile_circuit_tool",
                                     "export_circuit_to_qasm_tool"],
            "invalid_qasm_rejected": True, "oversized_fixture_rejected": True,
            "oversized_register_rejected": True,
            "noisy_readout_flip_probability_per_bit": 0.1, "runs": runs,
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report = json.dumps(asyncio.run(check()), indent=2) + "\n"
    if args.out:
        args.out.write_text(report, encoding="utf-8", newline="\n")
    print(report, end="")


if __name__ == "__main__":
    main()
