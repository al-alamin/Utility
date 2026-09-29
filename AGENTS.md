# AGENTS.md

Read the shared rules first: agents/AGENTS.md of https://github.com/DE-Knowledge-Base/agents.md (on Alamin's MacBooks at ~/agents.md), plus the applicable harness supplement. This file adds this repository's guidance.

## Purpose, current state and planned work

Reusable Python utilities and notebook import helpers for research projects.

Maintenance and runtime/deployment status are not established by this top-level audit, so `repo.yaml` uses `state: unknown`. Capabilities below describe documentation and tracked material, not newly tested application behavior.

Current documented capabilities:

- utils.py is documented as providing Pandas, TensorFlow, directory/file management and Stack Overflow XML-analysis helpers.
- basic_modules.py is documented as collecting common imports for Jupyter notebooks; both Python files are tracked.

No repository roadmap is established by the reviewed top-level documentation; `planned_capabilities` is empty.

## Working here

- Read the affected helper and its callers before changing reusable behavior.
- Preserve research-data boundaries when using filesystem/XML helpers; a utility description is not authorization to read arbitrary datasets.
