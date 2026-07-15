#!/usr/bin/env python3
import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def print_matrix_status() -> None:
    status = (
        "Welcome to the construct" if is_virtual_env()
        else "You are still plugged in"
    )
    print("\nMATRIX STATUS:", status, "\n")


def print_python_info() -> None:
    print("Current Python:", sys.executable)


def print_global_environment_warning() -> None:
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows\n")
    print("Then run this program again\n")


def print_virtual_environment_info(virtual_env: str) -> None:
    prompt = os.environ.get("VIRTUAL_ENV_PROMPT")
    print("Virtual Environment:", prompt)
    print("Environment Path:", virtual_env, "\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")


def print_site_packages_path() -> None:
    paths = site.getsitepackages()
    for p in paths:
        if "site-packages" in p:
            print("Package installation path:\n", p)
            return


def construct() -> None:
    print_matrix_status()
    print_python_info()

    virtual_env = os.environ.get("VIRTUAL_ENV")

    if not virtual_env:
        print_global_environment_warning()
    else:
        print_virtual_environment_info(virtual_env)
        print_site_packages_path()


if __name__ == "__main__":
    construct()
