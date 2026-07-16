# Python Mini Games

**[▶ Play Mastermind in your browser](https://akakiusz.github.io/small_python_games/mastermind/)** — no install, works on any device.

A collection of small games I'm building while learning Python. Each one starts
simple and gets rebuilt as I pick up new concepts — from terminal loops to
graphical interfaces to tested, packaged applications.

Every game lives in its own folder with its own README.

## The games

### [Number Guessing Game](number_guessing/)

The one that started it all. The computer picks a number, you have a limited
number of guesses, and it tells you whether you're too high or too low.

Built four times over, each version adding something new: functions, difficulty
levels, input validation, guess history, and finally a `tkinter` interface.

**Concepts:** `random`, `while` loops, functions, `try`/`except`, lists, `tkinter`

---

### [Mastermind](mastermind/)

A code-breaking game. The computer hides a four-color code; you guess, and it
tells you how many pegs are the right color in the right spot, and how many are
the right color in the wrong spot. Ten attempts to crack it.

The rules are separated from the interface so the scoring can be unit tested —
counting duplicate colors correctly is the part that's easy to get wrong.

Two versions share the same rules: a Python one with a desktop interface, and a
JavaScript one that runs in the browser.

**[▶ Play it now](https://akakiusz.github.io/small_python_games/mastermind/)**

**Concepts:** module separation, unit testing (`unittest`), classes, `tkinter`, JavaScript

<!--
  When the Windows .exe is published to Releases, add the download link here.
  Copy the real URL from your own published release asset — don't guess the format.
-->

---

<!--
  TEMPLATE — copy this block when you add a game.

  ### [Game Name](folder_name/)

  One or two sentences on what the game is and what makes it interesting to play.

  A line about what was interesting to *build* — the problem you had to solve, or
  the thing you'd do differently now.

  **Concepts:** the techniques this one taught you

  ---
-->

## Running any of them

Each game folder has its own README with instructions, but the short version:

```bash
cd folder_name
python game_file.py
```

Everything here needs Python 3 and nothing else — no external packages. The
`tkinter` games use Python's built-in GUI library, which ships with the standard
Python installers on Windows and macOS. On some Linux distributions it's a
separate install (`sudo apt install python3-tk`).

## Repo layout

```
small_python_games/
├── docs/               # the browser versions, served by GitHub Pages
├── mastermind/         # Python game + logic module + tests
└── number_guessing/    # the four versions of the first game
```

## Why this repo exists

I'm working through a Diploma in Python Programming at CCT College Dublin, and
this is where the practice lands. The games are small on purpose — the point is
to rebuild the same idea a few different ways and watch the code get better.

## Author

Arkadiusz Jędrzejewski
[GitHub](https://github.com/Akakiusz) · [LinkedIn](https://www.linkedin.com/in/ark-jedrzejewsky)
