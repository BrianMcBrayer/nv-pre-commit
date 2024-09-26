from __future__ import annotations

import argparse
import re
from typing import Sequence

NGC_PAT_EXPRESSION = re.compile(r"(nvapi-[a-zA-Z0-9_-]{64})")
NGC_API_EXPRESSION = re.compile(r"[A-z0-9]{84}")

def warning(keys: Sequence[str]) -> Sequence:
    hidden_keys = []
    for key in keys:
        hidden_keys.append(key[:4].ljust(10, "*") + key[-3:])
    return hidden_keys


def detect_pat(text_body: str) -> Sequence:
    keys = NGC_PAT_EXPRESSION.findall(text_body)
    return keys


def detect_api_key(text_body: str) -> Sequence:
    keys = NGC_API_EXPRESSION.findall(text_body)
    return keys


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args(argv)

    private_key_files = []

    for filename in args.filenames:
        with open(filename, "rb") as f:
            content = f.read().decode()
            private_key_files.extend(warning(detect_pat(content)))
            private_key_files.extend(warning(detect_api_key(content)))

    if private_key_files:
        for private_key_file in private_key_files:
            print(f"Private key found: {private_key_file}")
        return 1
    else:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
