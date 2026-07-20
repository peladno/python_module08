#!/usr/bin/env python3
from importlib import import_module
import dotenv
import os
import sys

ENV_DATA = {
    'MATRIX_MODE',
    'DATABASE_URL',
    'API_KEY',
    'LOG_LEVEL',
    'ZION_ENDPOINT'
}


class ConfigurationError(Exception):
    pass


def check_import() -> None:
    try:    
        module = import_module("dotenv")
    except ImportError as e:
        print(e)


def check_mode() -> bool:
    mode = os.getenv("MATRIX_MODE")
    if not mode:
        return False
    if mode == "development":
        print("mode: development")
        return True
    if mode == "production":
        print("mode: production")
        return True
    return False


def env_exist() -> bool:
    load = dotenv.load_dotenv(".env", verbose=True, override=True)
    if not load:
        raise ConfigurationError("env file doesn't exist")
    return True


def check_env() -> list[str]:
    missing = [k for k in ENV_DATA if not os.getenv(k)]
    return missing


def check_db() -> None:
    pass

    
def check_api_key() -> None:
    pass


def log() -> None:
    pass


def check_endpoint() -> None:
    pass


def main() -> int:
    try:
        env_exist()
    except ConfigurationError as e:
        print("ERROR:", e, file=sys.stderr)
        return 1

    missing = check_env()
    if missing:
        print(f"ERROR: Variables missing: {', '.join(missing)}")

    check_mode()
    return 0


if __name__ == "__main__":
    sys.exit(main())
