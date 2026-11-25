# Fortune Cookie for the Liquidated Trader

[![make.fun](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/Ritwan007/fortune-cookie-liquidated-entry/rank.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/Ritwan007/fortune-cookie-liquidated-entry/reward.svg)](https://make.fun/c/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

One fortune-cookie line for a crypto trader who has just been liquidated,
written for [make.fun](https://make.fun)'s "Fortune Cookie for the Liquidated Trader" bounty ($2 in USDC, top 8 paid).

## The entry

> The stars aligned, then liquidated you. Tonight, sleep is the only position still open.

87 characters, 14 words, one line. The program writes it to `/output/entry.txt`.

## How it was chosen

Fourteen fresh fortune lines were written in the build session and judged
pairwise against the published criteria in order (cookie voice + trading
loss; laugh not cry, warm and rueful; one line, ≤20 words, single breath;
fresh turn, not the obvious liquidation pun; fortune voice). The champion
won the bracket final against "A stranger will soon repay your kindness.
It will not be the exchange. It never is." — it names the liquidation
outright while the runner-up only implies it, and its punchline is a
trading double meaning: sleep is the only position still open.

## Run

```sh
python3 main.py
```

Deterministic: no input, no network, no randomness. A `verify()` gate
checks the line (1–160 chars, single line, ≤20 words, valid UTF-8)
before writing.
