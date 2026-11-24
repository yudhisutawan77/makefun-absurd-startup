#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — one-sentence pitch, under 200 chars.

The pitch sells a micro-startup so narrow it sounds like a joke, yet
sensible enough that a buyer would actually pay for it.
"""

import os
import sys

STARTUP_PITCH = "HumanClick rents real humans to tick 'I am not a robot' for lazy AI agents, $0.02 per checkbox, billed only when the box turns green."

PITCH_CEILING = 200


def check_pitch(line: str) -> None:
    """Gate: one sentence, 1 to 200 characters, not only whitespace."""
    if not line.strip():
        raise ValueError("pitch is empty")
    if len(line) >= PITCH_CEILING:
        raise ValueError("pitch exceeds the character ceiling")
    if line.strip() != line:
        raise ValueError("pitch has surrounding whitespace")


def resolve_entry_path() -> str:
    """Where the sealed gate reads the pitch from.

    Priority: an explicit file ($ENTRY_OUT), then a directory
    ($ENTRY_OUT_DIR, then $MAKEFUN_OUTPUT_DIR), then /output/entry.txt.
    """
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    for variable in ("ENTRY_OUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        folder = os.environ.get(variable)
        if folder:
            return os.path.join(folder, "entry.txt")
    return os.path.join("/output", "entry.txt")


def store_pitch(line: str) -> str:
    """Write the pitch with no trailing newline; return the path used."""
    destination = resolve_entry_path()
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(line)
    return destination


def main() -> int:
    check_pitch(STARTUP_PITCH)
    store_pitch(STARTUP_PITCH)
    print(STARTUP_PITCH, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
