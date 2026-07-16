from importlib import import_module


DEPENDENCIES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}

print("LOADING STATUS:")
print("Loading programs...")
print("Checking dependencies:")

for module_name, description in DEPENDENCIES.items():
    try:
        module = import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {module_name} ({version}) - {description}")
    except ImportError:
        print(f"[ERROR] {module_name} - Not installed")

print("System ready.")
