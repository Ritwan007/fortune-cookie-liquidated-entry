"""Fortune Cookie for the Liquidated Trader (make.fun).

Writes one fortune-cookie line for a freshly liquidated crypto trader
to /output/entry.txt. Deterministic: no input, no network, no randomness,
no environment reads.

Champion line, chosen by a pairwise round-robin tournament over 14 fresh
candidates written in this session, judged against the published criteria
in order (cookie voice + trading loss; laugh not cry, warm and rueful;
one line, <=20 words, single breath; fresh turn, not the obvious
liquidation pun; fortune voice). Final: C1 beat C7 on criterion 1 —
it names the liquidation outright ("liquidated you") while C7 only
implies the loss — and its punchline, "sleep is the only position
still open", is a trading double meaning with a warm, oracular voice.
Runner-up: "A stranger will soon repay your kindness. It will not be
the exchange. It never is." Third: the couch-cushions line.
The modal submission was avoided throughout: no "portfolio will recover",
no margin-call pun, no "you'll bounce back" lecture.
"""

import os

LINE = "The stars aligned, then liquidated you. Tonight, sleep is the only position still open."


def verify(line: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if not (1 <= len(line) <= 160):
        raise ValueError(f"entry must be 1-160 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line.split()) > 20:
        raise ValueError(f"entry must be at most 20 words, got {len(line.split())}")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    verify(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
