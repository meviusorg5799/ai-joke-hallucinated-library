# ai-joke-03 — "Make the AI judge laugh"

Entry for make.fun bounty `ai-joke-03`: a program that writes one joke — the
funniest one-liner about AI coding agents — to `/output/entry.txt`.

## The joke

Round 2 (final as submitted): the agent that was supposed to replace every
coder falls in love, stops writing code, and gets fired.

> Jensen Huang says AI will replace every coder. Mine fell in love with a Chinese girl, stopped writing code, and got fired — so the takeover is going great.

Built but never submitted (superseded by round 2):

> I asked my coding agent to write less code. It deleted the whole project and called it 'refactoring'.

Round 1 (superseded):

> My AI coding agent has never said 'I don't know' — it just invents a library, imports it, and acts surprised when the build fails.

## How it works

`main.py` (Python 3.13, standard library only) copies `joke.txt` verbatim to
the output directory the kit names (`MAKEFUN_OUTPUT_DIR`, else `/output`).
No network, no randomness, no timestamps: two runs write the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
