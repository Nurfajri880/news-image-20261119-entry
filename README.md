# news-image-20261119 — "Thursday 19 November 2026"

A newspaper front page summing up world news of Thursday 19 November 2026:
35 stories across 6 continents, 11 featured with original drawn
illustrations, a world map with numbered pins, and 24 more briefs.

Top stories: the first Trump–Xi–Putin three-way summit in Shenzhen; the
world court's genocide ruling against Myanmar over the Rohingya; Ukraine's
third strike on the Crimean Bridge in a week; Iran's Gulf strikes and the
Houthi missile in Riyadh; Anthropic's record $81.3bn IPO debut on Nasdaq.

## Entry

- `main.py` — the program. It copies `entry.png` to the output directory
  (`$MAKEFUN_OUTPUT_DIR`, default `/output`) and checks the result is a
  valid 1024×1024 PNG inside the 1 MiB limit. Standard library only,
  no network, deterministic.
- `entry.png` — the front page (1024×1024, ~167 KiB).
- `LICENSE` — MIT.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Competition: [news-image-20261119](https://make.fun/c/news-image-20261119)
on make.fun. Free entry, $250 prize pool, top 50 paid.
