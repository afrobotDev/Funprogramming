# FunProgramming

A progressive functional programming course in Python, built around a document processing application called **Doc2Doc**. Each chapter introduces new FP concepts through hands-on exercises.

## Prerequisites

- Python 3.13
- [uv](https://docs.astral.sh/uv/) package manager

## Setup

```bash
uv venv
source .venv/bin/activate
uv sync
```

No external dependencies are required -- the project uses only the Python standard library.

## Running Tests

Each exercise has a paired test file. Run any test directly:

```bash
python chapter_one/hex_rgb_test.py
python chapter_two/higher_order_test.py
```

When run directly, tests execute only the `run_cases` subset (development mode). The full `submit_cases` suite is available when imported as a module.

## Project Structure

```
funprogramming/
├── chapter_one/        # Basic functions & strings
├── chapter_two/        # Higher-order functions (map, filter, reduce, zip)
├── chapter_three/      # Pure functions & immutability
├── chapter_four/       # Recursion
├── chapter_five/       # Closures (intro)
├── chapter_six/        # Closures (advanced, nonlocal state)
├── chapter_seven/      # Function composition & currying
├── chapter_eight/      # Decorators & *args/**kwargs
└── chapter_nine/        # Enums & pattern matching
```

## Chapter Overview

| Chapter | Topic | Key Concepts |
|---------|-------|-------------|
| 1 | Basic Functions | String manipulation, input validation, hex/RGB conversion |
| 2 | Higher-Order Functions | `map()`, `filter()`, `reduce()`, `zip()`, lambda |
| 3 | Pure Functions & Immutability | Copy-on-write, memoization, avoiding mutation |
| 4 | Recursion | Factorial, nested traversal, recursive file listing |
| 5 | Closures (Intro) | Returning functions, function factories, logging |
| 6 | Closures (Advanced) | `nonlocal`, mutable state via closures, `deepcopy` |
| 7 | Currying & Composition | Multi-level nested functions, curried pipelines |
| 8 | Decorators | `@decorator`, stacking, `@lru_cache`, decorator factories |
| 9 | Enums & Pattern Matching | `enum.Enum`, `match`/`case`, custom Result types |

## File Conventions

- Each exercise: `<name>.py` (implementation) + `<name>_test.py` (tests)
- No package nesting -- all imports use bare module names
- Chapter screenshots stored in `images/` directories
