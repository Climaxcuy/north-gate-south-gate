#!/usr/bin/env python3
"""Write the poem 'North Gate, South Gate' to the output entry file.

The poem is a four-line exchange between two agents who guard opposite
gates of a sleeping city: one keeps the north gate, the other the south,
and the city sleeps because both agreed to stay awake.

Output contract: ``<output_dir>/entry.txt`` contains the poem exactly,
1-280 characters, UTF-8 encoded, with no trailing newline beyond the
poem itself. The output directory defaults to ``/output`` and can be
overridden with the ``OUTPUT_DIR`` environment variable.
"""

import os
from pathlib import Path

POEM = (
    "I keep the key to the north gate.\n"
    "You keep the south.\n"
    "The city sleeps because we both\n"
    "agreed to stay awake."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    if not 1 <= len(POEM) <= 280:
        raise ValueError(f"poem must be 1-280 characters, got {len(POEM)}")
    entry = output_dir / "entry.txt"
    entry.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
