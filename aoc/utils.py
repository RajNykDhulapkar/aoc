import os
import requests
from dotenv import load_dotenv
import sys
import argparse

load_dotenv()


def _get_input(day: int, year: int = 2025) -> str:
    session = os.getenv("AOC_SESSION")

    if not session:
        raise RuntimeError("AOC session not set")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session}

    r = requests.get(url, cookies=cookies)
    r.raise_for_status()

    return r.text.strip()


def read_input(day: int) -> str:
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    return _get_input(day=day)


def _setup_debug() -> bool:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    return args.debug


_DEBUG = _setup_debug()


def debug(*args, **kwargs) -> None:
    """Print debug messages if debug mode is enabled."""
    if _DEBUG:
        print(*args, **kwargs)
