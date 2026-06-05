# Function Software Measurement of Iconic Quantum Algorithms

This repository contains code and reference materials for measuring and experimenting with a set of iconic quantum algorithms. The focus is on small, reproducible implementations based off Qiskit documentation and examples.

## Repository contents

- `fsm/` - Python modules and notebooks implementing experiments and quantum algorithm examples.
	- `quantum_teleportation.py` - a Python implementation related to quantum teleportation experiments.
	- `teleportation/` - Jupyter notebook variants and experiment notebooks.
- `references/` - collected reference notebooks and supporting materials.
- `pyproject.toml` - project metadata and dependencies.

## Quick start

This project is designed to be used with `uv`. To set up and run the project:

1. Install `uv` (if not already installed). See the official docs for installation details: https://docs.astral.sh/uv/

2. Synchronize the project environment and install dependencies:

```powershell
uv sync
```

3. Run configured project commands (examples, tests, or experiment runners):

```powershell
uv run
```

On Windows, if you use the included virtual environment, activate it first (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```
