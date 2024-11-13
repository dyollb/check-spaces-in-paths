import argparse
import sys
from typing import Sequence


def _has_space(file: str):
    if " " in file:
        print(
            f"Error: The file or folder '{file}' contains spaces in its name.",
            file=sys.stderr,
        )
        return 1
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    ret = 0
    for filename in args.filenames:
        ret |= _has_space(filename)
    return ret
