from importlib import import_module
import sys


DEPENDENCIES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}

print("LOADING STATUS:")
print("Loading programs...")
print("Checking dependencies:")

modules = {}
missing = []

for module_name, description in DEPENDENCIES.items():
    try:
        module = import_module(module_name)
        modules[module_name] = module
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {module_name} ({version}) - {description}")
    except ImportError:
        missing.append(module_name)
        print(f"[ERROR] {module_name} - Not installed")

if missing:
    print("\nMissing dependencies:")
    for miss in missing:
        print(f" - {miss}")
    sys.exit(1)

print("System ready.")

# testing code
pd = modules["pandas"]
np = modules["numpy"]
requests = modules["requests"]

arr = np.random.randn(5, 3)

df = pd.DataFrame(
    arr,
    columns=["A", "B", "C"]
)

print("\nDataFrame:")
print(df)

response = requests.get("https://api.github.com")
print("Status code:", response.status_code)
print("Response:")
print(response.json())

print("\npandas version:", pd.__version__)
print("numpy version:", np.__version__)
# testing code
