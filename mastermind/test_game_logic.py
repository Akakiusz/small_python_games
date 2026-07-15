"""
Tests for the Mastermind logic.

Run with:  python -m unittest test_game_logic
"""

import unittest

from game_logic import Game, make_secret, score_guess


class TestScoreGuess(unittest.TestCase):

    def test_perfect_match(self):
        code = ["red", "blue", "green", "yellow"]
        self.assertEqual(score_guess(code, code), (4, 0))

    def test_all_right_colors_wrong_places(self):
        secret = ["red", "blue", "green", "yellow"]
        guess = ["blue", "red", "yellow", "green"]
        self.assertEqual(score_guess(secret, guess), (0, 4))

    def test_nothing_matches(self):
        secret = ["red", "blue", "green", "yellow"]
        guess = ["orange", "orange", "orange", "orange"]
        self.assertEqual(score_guess(secret, guess), (0, 0))

    def test_duplicates_in_secret(self):
        # Two reds and two blues, all in the wrong spots.
        secret = ["red", "red", "blue", "blue"]
        guess = ["blue", "blue", "red", "red"]
        self.assertEqual(score_guess(secret, guess), (0, 4))

    def test_duplicates_partially_placed(self):
        secret = ["red", "red", "blue", "blue"]
        guess = ["red", "blue", "red", "blue"]
        self.assertEqual(score_guess(secret, guess), (2, 2))

    def test_guess_repeats_a_color_secret_has_once(self):
        # Only one red exists, so only one peg can be credited.
        secret = ["red", "blue", "green", "yellow"]
        guess = ["red", "red", "red", "red"]
        self.assertEqual(score_guess(secret, guess), (1, 0))

    def test_blacks_and_whites_never_exceed_length(self):
        secret = ["red", "red", "red", "blue"]
        guess = ["red", "red", "blue", "red"]
        black, white = score_guess(secret, guess)
        self.assertLessEqual(black + white, 4)

    def test_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            score_guess(["red", "blue"], ["red", "blue", "green"])


class TestMakeSecret(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(make_secret()), 4)

    def test_colors_are_valid(self):
        from game_logic import COLORS
        for color in make_secret():
            self.assertIn(color, COLORS)

    def test_no_duplicates_when_disabled(self):
        code = make_secret(allow_duplicates=False)
        self.assertEqual(len(code), len(set(code)))


class TestGame(unittest.TestCase):

    def test_winning_finishes_the_game(self):
        game = Game()
        black, _ = game.submit(game.secret)
        self.assertEqual(black, 4)
        self.assertTrue(game.finished)
        self.assertTrue(game.won)

    def test_running_out_of_attempts(self):
        game = Game(max_attempts=2)
        wrong = ["red", "red", "red", "red"]
        # Make sure the guess isn't accidentally the secret.
        game.secret = ["blue", "blue", "blue", "blue"]
        game.submit(wrong)
        self.assertFalse(game.finished)
        game.submit(wrong)
        self.assertTrue(game.finished)
        self.assertFalse(game.won)

    def test_cannot_play_after_finish(self):
        game = Game()
        game.submit(game.secret)
        with self.assertRaises(ValueError):
            game.submit(game.secret)

    def test_history_records_each_guess(self):
        game = Game()
        game.secret = ["red", "blue", "green", "yellow"]
        game.submit(["red", "red", "red", "red"])
        self.assertEqual(len(game.history), 1)
        guess, black, white = game.history[0]
        self.assertEqual(guess, ["red", "red", "red", "red"])
        self.assertEqual((black, white), (1, 0))

    def test_attempts_left_counts_down(self):
        game = Game(max_attempts=10)
        game.secret = ["red", "blue", "green", "yellow"]
        self.assertEqual(game.attempts_left, 10)
        game.submit(["orange", "orange", "orange", "orange"])
        self.assertEqual(game.attempts_left, 9)

    def test_wrong_length_guess_raises(self):
        game = Game()
        with self.assertRaises(ValueError):
            game.submit(["red", "blue"])

    def test_unknown_color_raises(self):
        game = Game()
        with self.assertRaises(ValueError):
            game.submit(["pink", "blue", "green", "yellow"])


if __name__ == "__main__":
    unittest.main()