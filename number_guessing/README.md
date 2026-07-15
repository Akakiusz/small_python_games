# Python Mini Games

A collection of small Python games I am building and improving while learning. The project centers on one game — a number guessing game — that evolves step by step across several files, with each version adding a new concept or feature on top of the last.

## Game evolution

### 01 — The basic game (`01_the_game.ipynb`)
The starting point: the program picks a random number between 1 and 10, and the player has 5 guesses to find it, with "too high" / "too low" hints along the way.

**Concepts used:** `random` module, `while` loops, conditionals, f-strings

### 02 — Refactored with a welcome message (`02_the_game.ipynb`)
The range is extended to 1–100 with 10 guesses, and a `print_welcome_message()` function is introduced to explain the rules before the game starts.

**Concepts used:** functions, code organization

### 03 — Difficulty levels, validation, and guess history (`03_the_game_with_levels.ipynb`)
A bigger step up: adds a difficulty selection step (Easy 1–50, Medium 1–100, Hard 1–500), validates that the player's input is actually a number, blocks repeated guesses, and shows the running list of guesses so far after each round.

**Concepts used:** functions with parameters and return values, input validation (`try`/`except`), lists


### 04 — Graphical version (`04_the_game_with_GUI.py`)
The same game logic, now with a graphical interface built using Python's built-in `tkinter` library instead of the terminal. Players pick a difficulty and enter guesses through buttons and a text field, with live feedback shown directly in the window.

**Concepts used:** `tkinter` (Frame, Label, Entry, Button), event-driven programming, global state



**How to run:**
```bash
python 04_the_game_with_GUI.py
```

