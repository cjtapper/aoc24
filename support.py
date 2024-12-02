from __future__ import annotations

import argparse
import contextlib
import sys
from collections.abc import Callable
from pathlib import Path
from typing import TypeAlias

Solver: TypeAlias = Callable[[str], object]


def cli(module_filename: str, solver: Solver) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file",
        nargs="?",
        default=str(Path(module_filename).parent / "input.txt"),
    )
    args = parser.parse_args()

    input_data = slurp(args.input_file)

    print(solver(input_data))

    raise SystemExit(0)


def slurp(file: str) -> str:
    with contextlib.ExitStack() as stack:
        if file == "-":
            stream = sys.stdin
        else:
            stream = stack.enter_context(open(file))

        return stream.read()
