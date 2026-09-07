# Python Module 08: Virtual Environments & Modern Packaging

Welcome to **Python Module 08** of the 42 Tokyo Python curriculum. This module introduces professional Python environment management, package dependency specification, matrix inspection, and environment variable configuration.

## 🎯 Objectives

- Understand Python environments, global vs. isolated runtimes (`sys.prefix` vs `sys.base_prefix`).
- Create, activate, and manage isolated virtual environments (`python -m venv`).
- Manage project dependencies using modern specifications (`pyproject.toml`) and lock/requirements files (`requirements.txt`).
- Configure application secrets and environment variables using `.env` files and runtime loaders.

---

## 📁 Directory Structure & Exercises

| Exercise                        | Directory | File(s)                                                | Description                                                                                          |
| :------------------------------ | :-------- | :----------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| **ex0: Construct**              | `ex0/`    | `construct.py`                                         | Detects whether the current process is running inside an active virtual environment or global space. |
| **ex1: Loading & Dependencies** | `ex1/`    | `loading.py`<br>`requirements.txt`<br>`pyproject.toml` | Packaging configurations and loading third-party dependencies.                                       |
| **ex2: The Oracle**             | `ex2/`    | `oracle.py`<br>`.env.example`<br>`requirements.txt`    | Working with configuration, secrets, and environment variables safely.                               |

---

## 🚀 Setup & Execution

### 1. Creating a Virtual Environment

```bash
python -m venv .venv

# Activate on Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Activate on Linux / macOS:
source .venv/bin/activate
```

### 2. Running Exercises

```bash
# Check environment status
python ex0/construct.py

# Install dependencies and test ex1
pip install -r ex1/requirements.txt
python ex1/loading.py

# Setup environment variables and test ex2
copy ex2\.env.example ex2\.env   # On Windows
python ex2/oracle.py
```
