import sys
from importlib import import_module
from types import ModuleType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd  # type: ignore


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
        return False

    print("\nSystem ready.")
    return True


def generate_matrix_data(
    pd_module: ModuleType,
    np_module: ModuleType,
) -> pd.DataFrame:
    """Generate a DataFrame with random numbers."""

    print("\nAnalyzing Matrix data...")
    arr = np_module.random.randn(1000, 3)
    return pd_module.DataFrame(
        arr,
        columns=["A", "B", "C"],
    )


def generate_visual_data(
    df: pd.DataFrame,
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

    df = generate_matrix_data(
        modules["pandas"],
        modules["numpy"],
    )
    print("Processing 1000 data points...")
    print("\nDataFrame:")
    print(df.head())

    print("\nStatistics:")
    print(df.describe(), end="\n\n")

    generate_visual_data(
        df,
        modules["matplotlib"],
        "matrix_analysis.png",
    )


if __name__ == "__main__":
    main()
