"""
Mastermind — a logic code-breaking game.

Run this file to play:  python mastermind.py

The rules live in game_logic.py; this file only draws the window and
passes clicks through to the Game object.

Author: Arkadiusz Jedrzejewski (github.com/Akakiusz)
"""

import tkinter as tk

from game_logic import COLORS, CODE_LENGTH, MAX_ATTEMPTS, Game

# Map the logical color names to something tkinter can paint.
SWATCHES = {
    "red": "#e5484d",
    "blue": "#4a7dff",
    "green": "#46c07a",
    "yellow": "#f5c542",
    "orange": "#f08c3c",
    "purple": "#a877e8",
}

BG = "#14151a"
PANEL = "#1c1e26"
INK = "#ecebe4"
MUTED = "#8b8d98"
ACCENT = "#e8c24b"


class MastermindApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind — Crack the Code")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.game = Game()
        self.pending = []      # colors picked but not submitted yet

        self._build_ui()

    # ---- interface construction ----

    def _build_ui(self):
        tk.Label(
            self.root, text="MASTERMIND", bg=BG, fg=ACCENT,
            font=("Helvetica", 20, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=(16, 2))

        tk.Label(
            self.root,
            text="Black = right color, right spot   ·   White = right color, wrong spot",
            bg=BG, fg=MUTED, font=("Helvetica", 10),
        ).grid(row=1, column=0, columnspan=2, pady=(0, 12))

        # Left: the board of past guesses
        board_panel = tk.Frame(self.root, bg=PANEL, padx=12, pady=12)
        board_panel.grid(row=2, column=0, padx=(16, 8), sticky="n")

        tk.Label(board_panel, text="Your guesses", bg=PANEL, fg=MUTED,
                 font=("Helvetica", 10)).pack(pady=(0, 8))

        self.board = tk.Frame(board_panel, bg=PANEL)
        self.board.pack()

        # Right: the controls
        panel = tk.Frame(self.root, bg=PANEL, padx=12, pady=12)
        panel.grid(row=2, column=1, padx=(8, 16), sticky="n")

        tk.Label(panel, text="Build your guess", bg=PANEL, fg=MUTED,
                 font=("Helvetica", 10)).pack(pady=(0, 8))

        palette = tk.Frame(panel, bg=PANEL)
        palette.pack(pady=(0, 10))
        for i, name in enumerate(COLORS):
            tk.Button(
                palette, bg=SWATCHES[name], activebackground=SWATCHES[name],
                width=3, height=1, bd=0, highlightthickness=0,
                command=lambda c=name: self.pick(c),
            ).grid(row=i // 3, column=i % 3, padx=3, pady=3)

        self.preview = tk.Frame(panel, bg=PANEL)
        self.preview.pack(pady=(0, 10))
        self.slots = []
        for _ in range(CODE_LENGTH):
            slot = tk.Label(self.preview, bg=BG, width=3, height=1)
            slot.pack(side="left", padx=3)
            self.slots.append(slot)

        tk.Button(panel, text="Submit guess", command=self.submit,
                  bg=ACCENT, fg=BG, bd=0, width=16,
                  font=("Helvetica", 11, "bold")).pack(pady=2)
        tk.Button(panel, text="Undo", command=self.undo,
                  bg=PANEL, fg=INK, width=16).pack(pady=2)
        tk.Button(panel, text="New game", command=self.reset,
                  bg=PANEL, fg=INK, width=16).pack(pady=2)

        self.status = tk.Label(panel, text="", bg=PANEL, fg=MUTED,
                               font=("Helvetica", 10))
        self.status.pack(pady=(10, 0))

        self._refresh_status()
        self._refresh_preview()

    # ---- interactions ----

    def pick(self, color):
        if self.game.finished:
            return
        if len(self.pending) < CODE_LENGTH:
            self.pending.append(color)
            self._refresh_preview()

    def undo(self):
        if self.game.finished or not self.pending:
            return
        self.pending.pop()
        self._refresh_preview()

    def submit(self):
        if self.game.finished:
            return
        if len(self.pending) < CODE_LENGTH:
            self.status.config(text="Pick {} colors first".format(CODE_LENGTH))
            return

        guess = list(self.pending)
        black, white = self.game.submit(guess)
        self._draw_row(guess, black, white)
        self.pending = []
        self._refresh_preview()

        if self.game.won:
            self.status.config(
                text="Cracked it in {}!".format(self.game.attempts_used), fg="#46c07a")
        elif self.game.finished:
            self.status.config(text="Out of guesses", fg="#e5484d")
            self._draw_secret()
        else:
            self._refresh_status()

    def reset(self):
        self.game = Game()
        self.pending = []
        for widget in self.board.winfo_children():
            widget.destroy()
        self.status.config(fg=MUTED)
        self._refresh_status()
        self._refresh_preview()

    # ---- drawing ----

    def _refresh_status(self):
        self.status.config(
            text="Attempt {} of {}".format(self.game.attempts_used + 1, MAX_ATTEMPTS))

    def _refresh_preview(self):
        for i, slot in enumerate(self.slots):
            if i < len(self.pending):
                slot.config(bg=SWATCHES[self.pending[i]])
            else:
                slot.config(bg=BG)

    def _draw_row(self, guess, black, white):
        row = tk.Frame(self.board, bg=PANEL)
        row.pack(anchor="w", pady=2)

        tk.Label(row, text="{:02d}".format(self.game.attempts_used),
                 bg=PANEL, fg=MUTED, font=("Courier", 9)).pack(side="left", padx=(0, 8))

        for color in guess:
            tk.Label(row, bg=SWATCHES[color], width=3, height=1).pack(side="left", padx=2)

        feedback = tk.Frame(row, bg=BG, padx=4, pady=2)
        feedback.pack(side="left", padx=(10, 0))
        for i in range(CODE_LENGTH):
            # A black peg on a dark background needs an outline to be visible,
            # so each peg state gets its own fill + border combination.
            if i < black:
                fill, border = "#000000", ACCENT
            elif i < black + white:
                fill, border = INK, INK
            else:
                fill, border = BG, "#3a3d47"
            tk.Label(
                feedback, bg=fill, width=1, height=1,
                highlightbackground=border, highlightthickness=1,
            ).pack(side="left", padx=2)

    def _draw_secret(self):
        row = tk.Frame(self.board, bg=PANEL)
        row.pack(anchor="w", pady=(8, 2))
        tk.Label(row, text="★", bg=PANEL, fg=ACCENT).pack(side="left", padx=(0, 8))
        for color in self.game.secret:
            tk.Label(row, bg=SWATCHES[color], width=3, height=1).pack(side="left", padx=2)


def main():
    root = tk.Tk()
    MastermindApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()