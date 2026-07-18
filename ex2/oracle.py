#!/usr/bin/env python3
from dotenv import load_dotenv
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


def check_mode() -> None:
    mode = os.getenv("MATRIX_MODE")
    if not mode:
        return
    if mode == "development":
        print("mode: development")
    if mode == "production":
        print("mode: production")


def env_exist() -> bool:
    load = load_dotenv(".env", verbose=True, override=True)
    if not load:
        raise ConfigurationError("env file doesn't exist")
    return True


def check_env() -> list[str]:
    missing = [k for k in ENV_DATA if not os.getenv(k)]
    return missing


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
