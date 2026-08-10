#!/usr/bin/env python3
import sys
from importlib import import_module
from types import ModuleType
from typing import Any

DEPENDENCIES = {
    "pandas": ("pandas", "Data manipulation ready"),
    "numpy": ("numpy", "Numerical computation ready"),
    "matplotlib": ("matplotlib.pyplot", "Visualization ready"),
}


def check_dependencies() -> tuple[dict[str, ModuleType], list[str]]:
    """Check whether dependencies are installed.

    Returns:
        tuple[dict[str, ModuleType], list[str]]:
            Imported modules and missing dependencies.
    """
    modules: dict[str, ModuleType] = {}
    missing: list[str] = []

    print("LOADING STATUS: Loading programs...", end="\n\n")
    print("Checking dependencies:")

    for name, (module_name, desc) in DEPENDENCIES.items():
        try:
            mod = import_module(module_name)
            modules[name] = mod
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {desc}")
        except ImportError:
            missing.append(name)
            print(f"[ERROR] {name} - Not installed")

    return modules, missing


def missing_dependencies(missing: list[str]) -> bool:
    if missing:
        print("\nMissing dependencies:")
        for miss in missing:
            print(f" - {miss}")
        print("\nPlease install dependencies using pip or poetry")
        print(" pip install -r requirements.txt")
        print(" or")
        print(" poetry install")
        return False

    print("\nSystem ready.")
    return True


def generate_matrix_data(
    pd_module: ModuleType,
    np_module: ModuleType,
) -> Any:
    """Generate a DataFrame with random numbers."""
    print("\nAnalyzing Matrix data...")
    arr = np_module.random.randn(1000, 3)
    return pd_module.DataFrame(arr, columns=["A", "B", "C"])


def generate_visual_data(
    df: Any,
    plt_module: ModuleType,
    dest: str,
) -> None:
    """Generate analysis image."""
    print("Generating visualization...")
    plt_module.figure(figsize=(10, 5))
    plt_module.plot(df["A"])
    plt_module.title("Column A")
    plt_module.savefig(dest)
    print("Analysis complete")
    print("Results saved to:", dest)
    plt_module.close()


def main() -> None:
    modules, missing = check_dependencies()

    if not missing_dependencies(missing):
        sys.exit(1)

    pd = modules["pandas"]
    np = modules["numpy"]
    plt = modules["matplotlib"]

    try:
        df = generate_matrix_data(pd, np)
    except Exception as e:
        print("Error generating data:", e)
        sys.exit(2)

    print("Processing 1000 data points...")
    print("\nDataFrame:")
    print(df.head())

    print("\nStatistics:")
    print(df.describe(), end="\n\n")

    try:
        generate_visual_data(df, plt, "matrix_analysis.png")
    except Exception as e:
        print("Error generating visualization:", e)
        sys.exit(3)


if __name__ == "__main__":
    main()
