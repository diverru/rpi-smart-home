#!/usr/bin/env python3
import sys
import os
from pathlib import Path


def subst_env(s):
    result = []
    parts = s.split("$$")
    for index, part in enumerate(parts):
        if index % 2 == 0:
            result.append(part)
        else:
            value = os.getenv(part)
            if not value:
                raise RuntimeError(f"Value of env variable {part} is empty")
            result.append(value)
    return "".join(result)


def main():
    for source in sys.argv[1:]:
        source = Path(source)
        result = []
        for line in source.open("r"):
            if "$$" in line:
                line = subst_env(line)
                print(f"=> {line.strip()}")
            result.append(line)

        source.open("w").writelines(result)


if __name__ == "__main__":
    main()
