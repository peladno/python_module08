#!/usr/bin/env python3
from importlib import import_module
from types import ModuleType
import os
from typing import Any

ENV_DATA = {
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
}


class ConfigurationError(Exception):
    """Config error"""
    pass


def import_dotenv() -> ModuleType | None:
    """Check if the dotenv module exists, if exist returns the module"""
    try:
        return import_module("dotenv")
    except ImportError:
        print(
            "python-dotenv is not installed.\n"
            "Run: pip install python-dotenv"
        )
        return None


def load_env_file(dotenv: ModuleType, env: str) -> Any:
    """Load enviroment file"""
    loaded = dotenv.load_dotenv(env, verbose=True, override=False)

    if not loaded:
        raise ConfigurationError(".env file is missing")

    return loaded


def check_mode() -> None:
    """Checks MATRIX MODE enviroment variable"""
    mode = os.getenv("MATRIX_MODE")

    if mode == "development":
        print("mode: development")
        return

    if mode == "production":
        print("mode: production")
        return

    raise ConfigurationError(
        f"MATRIX_MODE '{mode}' is invalid. "
        "Expected 'development' or 'production'."
    )


def check_env_variables() -> list[str]:
    """Checks missing enviroment variables in file"""
    return [key for key in ENV_DATA if not os.getenv(key)]


def main() -> None:
    dotenv = import_dotenv()

    if not dotenv:
        return

    if not load_env_file(dotenv, ".env"):
        return

    missing = check_env_variables()

    if missing:
        raise ConfigurationError(
            f"Variables missing: {', '.join(missing)}"
        )
    print("Configuration loaded")
    check_mode()


if __name__ == "__main__":
    try:
        main()
    except ConfigurationError as error:
        print(f"ERROR: {error}")
