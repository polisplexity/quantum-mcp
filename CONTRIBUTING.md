# Contributing

Write public documentation, issues and code comments in English.

1. Select one scoped job or experiment and inspect the original interface, source,
   version and license. Reuse the supported MCP, API or CLI where possible.
2. Update the registry with what is reused, the proposed code delta and a test
   that would falsify the capability claim. Regenerate the inventory with
   `python tools/validate_inventory.py --write`.
3. Reproduce the reference natively, then run the same task through actual MCP.
   Record positive, failure, retry and recovery behavior where applicable.
4. Repeat the applicable agent task in fresh Codex and Hermes workspaces.
   Compare artifacts, structured claims and the final narrative separately.
5. Submit reviewed evidence and update the master record. A recipe should state
   the licensed fixture, source versions, native commands, required allocation,
   actual measurement scope and known limits.

Public code and documents follow [the MIT license](LICENSE). Third-party
software, fixtures, outputs and provider accounts retain their own terms.
Keep credentials, local profiles, private data and bulk generated files outside
version control. Publish only permitted, reviewed inputs and artifacts.
