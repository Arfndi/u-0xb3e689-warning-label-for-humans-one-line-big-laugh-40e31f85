# Warning Label for Humans entry: one fixed warning line.
#
# The entry is a fixed string: the program is deterministic by
# construction, so two runs write the same bytes. It reads
# $MAKEFUN_OUTPUT_DIR when set, else /output, and writes entry.txt
# there. The line is 138 characters, inside the 160-character cap,
# and is written with no trailing newline so the gate counts it as-is.

import os

ENTRY = "WARNING: This human runs on caffeine, overconfidence, and three hours of sleep. Do not shake. Do not ask how they are. Handle with snacks."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
