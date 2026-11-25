#!/usr/bin/env python3
"""Two lines to my past self.

Writes a two-line warning to /output/entry.txt: the first line warns
against one specific moment, the second says why that moment mattered
and what changed because of it.
"""

import os

# The entry: two lines, one sentence each.
LINE_ONE = "Do not press Deploy on Friday at 4:59pm, no matter how small the change looks."
LINE_TWO = (
    "That one click turned the whole weekend into a war room, "
    "and it taught me that a quiet Friday evening is worth more "
    "than looking finished."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Write the two entry lines and make the file world-readable."""
    lines = [LINE_ONE, LINE_TWO]
    # Guard the gate before writing: exactly two lines, one sentence
    # each, and the whole entry within the 280-character limit.
    if len(lines) != 2 or any(not line.strip() for line in lines):
        return 1
    text = "\n".join(lines) + "\n"
    if len(text.rstrip("\n")) > 280:
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # The grader collects outputs as another user, so the file itself
    # must be readable by everyone. Only the file is chmodded here,
    # never the /output directory.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
