# Mastermind

**[▶ Play it in your browser](https://akakiusz.github.io/small_python_games/mastermind/)** — no install needed.

This folder holds the Python version, which runs as a desktop app with a
`tkinter` interface. The browser version lives in [`docs/mastermind/`](../docs/mastermind/)
and is written in JavaScript — same rules, different language.

## The game

The computer picks a secret code of four colored pegs. After each guess you get
feedback:

- **Black peg** — right color in the right position
- **White peg** — right color, wrong position

The pegs tell you *how many* are right, never *which ones*. That's the whole
game: comparing guesses until only one code can still fit. You have ten tries.

## Files

| File | What it does |
|---|---|
| `mastermind.py` | The GUI. Run this to play. |
| `game_logic.py` | The rules — no GUI code, so it can be tested on its own. |
| `test_game_logic.py` | Unit tests for the rules. |

The logic is kept separate from the interface so the scoring rules can be tested
without opening a window. Scoring duplicate colors correctly is the tricky part
of Mastermind — if the code has two reds and you guess four, only two should
count. The tests cover that case and a few others like it.

## Play

```bash
python mastermind.py
```

Needs Python 3. `tkinter` ships with the standard Python installers on Windows
and macOS. On some Linux distributions it's a separate package (e.g.
`sudo apt install python3-tk`).

## Run the tests

```bash
python -m unittest test_game_logic -v
```

## Configuration

The knobs live at the top of `game_logic.py`:

| Setting | Meaning |
|---|---|
| `COLORS` | Available peg colors |
| `CODE_LENGTH` | How many pegs in the code |
| `MAX_ATTEMPTS` | How many guesses you get |
| `ALLOW_DUPLICATES` | Whether the code can repeat a color |

## Build a Windows .exe

Built on Windows with [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name Mastermind mastermind.py
```

The executable lands in `dist/`.

Two things worth knowing: PyInstaller builds for the OS it runs on, so a Windows
`.exe` has to be built on Windows. And antivirus software sometimes flags
PyInstaller output as a false positive — a known quirk of the tool, not the code.
