"""Funniest Cat Voicemail Greeting — one-line entry.

The line below is a voicemail greeting recorded by a cat named Biscuit.
The joke is built from things only a cat would do: knocking a phone off
a table (the classic shelf-clearing habit), then calmly telling the
caller to leave a message anyway — as if the cat caused the problem and
is now unbothered by it. The punch lands fast: the cat is not sorry,
it just wants tuna as a bribe. "Tuna bribes accepted" gives Biscuit a
cheeky, unbothered attitude, and ending on a deadpan "Meow." sells it
as a real recorded greeting spoken aloud in a few seconds.
"""

import os

# Biscuit's greeting: specific cat behaviour (knocking things off),
# a clear voicemail shape ("leave a message after the beep"), and a
# greedy little payoff (tuna bribes) — all in the cat's own voice.
LINE = "Hi, it's Biscuit. I knocked your phone off the table, so leave a message after the beep. Tuna bribes accepted. Meow."


def validate(text):
    """Check the entry line meets the bounty rules."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1..120 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
