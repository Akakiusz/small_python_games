# Implementation of the game logic for Mastermind.
import random

# Constants for the game configuration
COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
CODE_LENGTH = 4
MAX_ATTEMPTS = 10
ALLOW_DUPLICATES = True


def make_secret(colors=COLORS, length=CODE_LENGTH, allow_duplicates=ALLOW_DUPLICATES):
    # Generate a random secret code of the given length from the available colors.
    if allow_duplicates:
        return [random.choice(colors) for _ in range(length)]
    return random.sample(colors, length)


def score_guess(secret, guess):
   # Score a guess against the secret code, returning (black, white) counts.
    if len(secret) != len(guess):
        raise ValueError("Guess must be the same length as the secret")

    black = sum(s == g for s, g in zip(secret, guess))

    # Count color overlap ignoring position, then remove the exact matches.
    overlap = 0
    for color in set(secret):
        overlap += min(secret.count(color), guess.count(color))
    white = overlap - black

    return black, white


def is_win(black, length=CODE_LENGTH):
    # Check if the number of black pegs indicates a win (all pegs correct).
    return black == length


class Game:
    # Represents a single game of Mastermind.

    def __init__(self, colors=COLORS, length=CODE_LENGTH, max_attempts=MAX_ATTEMPTS,
                 allow_duplicates=ALLOW_DUPLICATES):
        self.colors = colors
        self.length = length
        self.max_attempts = max_attempts
        self.secret = make_secret(colors, length, allow_duplicates)
        self.history = []   # list of (guess, black, white)
        self.finished = False
        self.won = False

    @property
    def attempts_used(self):
        return len(self.history)

    @property
    def attempts_left(self):
        return self.max_attempts - self.attempts_used

    def submit(self, guess):
       # Submit a guess and return the score (black, white). Raises ValueError for invalid guesses or if the game is over.
        if self.finished:
            raise ValueError("Game is already over")
        if len(guess) != self.length:
            raise ValueError("Guess must have {} pegs".format(self.length))
        for color in guess:
            if color not in self.colors:
                raise ValueError("Unknown color: {}".format(color))

        black, white = score_guess(self.secret, guess)
        self.history.append((list(guess), black, white))

        if is_win(black, self.length):
            self.finished = True
            self.won = True
        elif self.attempts_used >= self.max_attempts:
            self.finished = True

        return black, white