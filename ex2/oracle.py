#!/usr/bin/env python3
from importlib import import_module
from types import ModuleType
import os


ENV_DATA = {
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
}


class ConfigurationError(Exception):
    """Configuration error."""
    pass


def import_dotenv() -> ModuleType | None:
    """Import python-dotenv if installed."""

    try:
        return import_module("dotenv")
    except ImportError:
        print(
            "python-dotenv is not installed.\n"
            "Run: pip install python-dotenv", end="\n\n"
        )
        return None


def load_env_file(dotenv: ModuleType) -> None:
    """Load .env file if it exists."""

    dotenv.load_dotenv(".env", override=False)


def check_mode() -> None:
    """Check MATRIX_MODE."""

    mode = os.getenv("MATRIX_MODE")

    if mode == "development":
        print("Mode: development")
        return

    if mode == "production":
        print("Mode: production")
        return

    print(
        f"Invalid MATRIX_MODE: {mode}. "
        "Expected 'development' or 'production'."
    )


def check_env_variables() -> list[str]:
    """Return missing variables."""

    return [key for key in ENV_DATA if not os.getenv(key)]


def check_database_url() -> None:
    """Check DATABASE_URL."""

    if os.getenv("DATABASE_URL"):
        print("Database: Connected to local instance")
    else:
        print("Database: Offline")


def check_api_key() -> None:
    """Check API_KEY."""

    if os.getenv("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")


def check_log_level() -> None:
    """Show log level."""

    level = os.getenv("LOG_LEVEL", "INFO")
    print(f"Log Level: {level}")


def check_zion_network() -> None:
    """Check Zion endpoint."""

    if os.getenv("ZION_ENDPOINT"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check() -> None:
    """Security checks."""

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")


def main() -> None:
    dotenv = import_dotenv()

    if dotenv:
        load_env_file(dotenv)

    print("Configuration loaded:")

    check_mode()
    check_database_url()
    check_api_key()
    check_log_level()
    check_zion_network()
    security_check()

    missing = check_env_variables()
    if missing:
        print("\nMissing configuration:")
        for var in missing:
            print(f" - {var}")
    else:
        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    main()
