"""Validate the inventory and keep the human-readable index in sync."""

import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "tools.json"
DOCUMENT = ROOT / "docs" / "INVENTORY.md"
DECISIONS = {"pilot", "evaluate", "alternate", "dependency", "reference", "research"}
STATUSES = {"candidate", "native-verified", "mcp-verified", "agent-reviewed"}
FIELDS = ("id", "name", "family", "decision", "upstream", "reuse", "build", "test", "status")


def validate(catalog):
    if catalog["schema_version"] != 1:
        raise ValueError("Unsupported inventory schema")
    if not catalog["entries"] or catalog["entries"][0]["id"] != catalog["first_entry"]:
        raise ValueError("The first entry must be the first pilot")

    seen = set()
    for entry in catalog["entries"]:
        for field in FIELDS:
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise ValueError(f"Missing {field}: {entry.get('id', '<unknown>')}")
        key = entry["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key) or key in seen:
            raise ValueError(f"Invalid or duplicate entry ID: {key}")
        seen.add(key)
        if entry["decision"] not in DECISIONS or entry["status"] not in STATUSES:
            raise ValueError(f"Invalid decision or status: {key}")
        sources = entry.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValueError(f"No upstream sources: {key}")
        for source in sources:
            parsed = urlsplit(source)
            if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
                raise ValueError(f"Invalid public source in {key}: {source}")


def render(catalog):
    entries = catalog["entries"]
    lines = [
        f"# {catalog['project']} integration inventory",
        "",
        f"Edition {catalog['edition']} · {len(entries)} entries.",
        "",
        "Generated from [the source registry](../registry/tools.json).",
        "The catalog includes deployment targets, connectors, dependencies,",
        "reference tools and workloads. Each entry describes a proposed test.",
        "See the [master record](../MASTER_TEST_RECORD.md) for observed results.",
        "",
        "Decisions: pilot (first case), evaluate (near-term candidate), alternate",
        "(substitute), dependency (used inside another tool), reference (human",
        "or benchmark reference), research (later experiment).",
        "",
        "## Contents",
        "",
    ]
    for entry in entries:
        # Explicit IDs keep links stable when an upstream project changes name.
        lines.append(f"- [{entry['name']}](#{entry['id']}) — {entry['family']}")
    for entry in entries:
        sources = ", ".join(
            f"[{'Upstream source ' + str(index)}]({url})"
            for index, url in enumerate(entry["sources"], 1)
        )
        lines.extend([
            "",
            f'<a id="{entry["id"]}"></a>',
            f"## {entry['name']}",
            "",
            f"**Family** — {entry['family']}. **Decision** — {entry['decision']}. "
            f"**Status** — {entry['status']}.",
            "",
            f"- **Upstream interface** — {entry['upstream']}",
            f"- **Reuse** — {entry['reuse']}",
            f"- **Build** — {entry['build']}",
            f"- **Acceptance test** — {entry['test']}",
            f"- **Sources** — {sources}",
        ])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the Markdown inventory")
    args = parser.parse_args()

    catalog = json.loads(REGISTRY.read_text(encoding="utf-8"))
    validate(catalog)
    rendered = render(catalog)
    if args.write:
        DOCUMENT.write_text(rendered, encoding="utf-8", newline="\n")
    elif not DOCUMENT.is_file() or DOCUMENT.read_text(encoding="utf-8") != rendered:
        parser.error("The document is stale. Run python tools/validate_inventory.py --write")
    print(f"{catalog['project']}: {len(catalog['entries'])} inventory entries verified")


if __name__ == "__main__":
    main()
