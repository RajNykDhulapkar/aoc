# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) written in Python.

## Setup

1. Install dependencies using [uv](https://github.com/astral-sh/uv):
```bash
uv sync
```

2. Create a `.env` file with your AOC session cookie:
```bash
AOC_SESSION=your_session_cookie_here
```

## Running Solutions

Each day's solution can be run individually:

```bash
python -m aoc.day01
```

### Input Options

Solutions accept input in two ways:
- **Automatic**: Fetches input from adventofcode.com using your session cookie
- **Stdin**: Pipe or redirect input directly
  ```bash
  cat input.txt | python -m aoc.day01
  ```

### Debug Mode

Enable debug output with the `--debug` flag:

```bash
python -m aoc.day01 --debug
```

## Project Structure

```
aoc2025/
├── aoc/
│   ├── utils.py       # Utility functions
│   ├── day01.py       # Day 1 solution
│   └── ...
├── .env               # Session cookie (not committed)
├── pyproject.toml     # Project dependencies
└── README.md
```

## Utilities

The `aoc/utils.py` module provides helper functions:

- **`read_input(day: int)`** - Reads input from stdin or fetches from AOC
- **`debug(*args, **kwargs)`** - Prints debug messages when `--debug` flag is enabled

### Using the debug utility

Instead of conditional debug prints:
```python
# Don't do this
if DEBUG:
    print("Debug message")
```

Simply use the `debug()` function:
```python
from aoc.utils import debug

debug("Debug message")
debug(f"Variable: {value}")
```

The debug function automatically checks if debug mode is enabled and only prints when the `--debug` flag is passed.
