"""Stdio MCP that runs the bounded Aer fixture with a fixed shot budget."""

from typing import Any

from mcp.server.fastmcp import FastMCP

from bell_fixture import simulate


server = FastMCP("Polisplexity Quantum Aer fixture")


@server.tool()
def sample_bell_fixture(qasm_text: str, noisy: bool = False) -> dict[str, Any]:
    """Sample the supplied small measured two-qubit fixture with Qiskit Aer."""
    return simulate(qasm_text, noisy)


if __name__ == "__main__":
    server.run()
