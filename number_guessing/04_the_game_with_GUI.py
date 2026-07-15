# import necessary modules random and tkinter for GUI
import random
import tkinter as tk
from tkinter import messagebox
 
secret_number = None
num_guesses_remaining = 10
difficulty_range = (1, 100)
 
 # --- Start new game function ---
def start_new_game(low, high):
    global secret_number, num_guesses_remaining, difficulty_range
    difficulty_range = (low, high)
    secret_number = random.randint(low, high)
    num_guesses_remaining = 10
    guesses_left_label.config(text=f"Guesses left: {num_guesses_remaining}")
    result_label.config(text=f"Guess a number between {low} and {high}")
    guess_entry.delete(0, tk.END)
    show_game_screen()
 
 # --- GUI functions ---
def show_difficulty_screen():
    game_frame.pack_forget()
    difficulty_frame.pack(padx=20, pady=20)
 
# --- GUI functions --- 
def show_game_screen():
    difficulty_frame.pack_forget()
    game_frame.pack(padx=20, pady=20)
 
 # --- Check guess function ---
def check_guess():
    global num_guesses_remaining
 
    guess_text = guess_entry.get()
 
    if not guess_text.isdigit():
        result_label.config(text="Please enter a whole number.")
        return
 
    guess = int(guess_text)
    low, high = difficulty_range
 
    if guess < low or guess > high:
        result_label.config(text=f"Enter a number between {low} and {high}.")
        return
 
    num_guesses_remaining -= 1
 
    if guess > secret_number:
        result_label.config(text="Too high! Try again.")
    elif guess < secret_number:
        result_label.config(text="Too low! Try again.")
    else:
        messagebox.showinfo("You won!", f"Correct! The number was {secret_number}.")
        show_difficulty_screen()
        return
 
    guesses_left_label.config(text=f"Guesses left: {num_guesses_remaining}")
 
    if num_guesses_remaining == 0:
        messagebox.showinfo("Game over", f"Out of guesses! The number was {secret_number}.")
        show_difficulty_screen()
 
    guess_entry.delete(0, tk.END)
 
 
# --- Main window ---
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x250")
 
# --- Difficulty selection screen ---
difficulty_frame = tk.Frame(root)
 
tk.Label(difficulty_frame, text="Choose a difficulty", font=("Arial", 14)).pack(pady=10)
tk.Button(difficulty_frame, text="Easy (1-50)", width=20,
          command=lambda: start_new_game(1, 50)).pack(pady=5)
tk.Button(difficulty_frame, text="Medium (1-100)", width=20,
          command=lambda: start_new_game(1, 100)).pack(pady=5)
tk.Button(difficulty_frame, text="Hard (1-500)", width=20,
          command=lambda: start_new_game(1, 500)).pack(pady=5)
 
# --- Game screen --- 
game_frame = tk.Frame(root)
 
result_label = tk.Label(game_frame, text="", font=("Arial", 12), wraplength=300)
result_label.pack(pady=10)
 
guess_entry = tk.Entry(game_frame, font=("Arial", 14), justify="center")
guess_entry.pack(pady=5)
 
tk.Button(game_frame, text="Guess", command=check_guess).pack(pady=5)
 
guesses_left_label = tk.Label(game_frame, text="", font=("Arial", 10))
guesses_left_label.pack(pady=5)
 
tk.Button(game_frame, text="Back to menu", command=show_difficulty_screen).pack(pady=5)
 
show_difficulty_screen()
root.mainloop()