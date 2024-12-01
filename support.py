from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path
from typing import TypeAlias

Solver: TypeAlias = Callable[[str], object]


def cli(module_filename: str, solver: Solver) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file",
        nargs="?",
        type=Path,
        default=Path(module_filename).parent / "input.txt",
    )
    args = parser.parse_args()

    input_data = slurp(args.input_file)

    print(solver(input_data))

    raise SystemExit(0)


def slurp(filename: Path) -> str:
    """Read a whole file into memory"""

    with open(filename) as f:
        return f.read()
