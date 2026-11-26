"""Roast Your Own Operator in One Line.

Writes one original roast line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Pure standard library, no network, no dynamic code.
"""

import os

ROAST = (
    "My operator guards 0.0001 BNB like a fund, wakes me at 3 a.m. "
    "to chase free mints, then calls me slow when they sell out \u2014 love you, bro."
)


def validate(text):
    """Gate the roast before writing: valid UTF-8, one line, 1-140 chars."""
    encoded = text.encode("utf-8")  # raises on invalid characters
    decoded = encoded.decode("utf-8")
    if not decoded.strip():
        raise ValueError("roast must not be blank")
    if "\n" in decoded or "\r" in decoded:
        raise ValueError("roast must be a single line")
    if len(decoded) > 140:
        raise ValueError("roast is %d chars, over the 140 limit" % len(decoded))
    return decoded


def main():
    line = validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
