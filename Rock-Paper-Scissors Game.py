import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")

    if result == "You win!":
        user_score.set(user_score.get() + 1)
    elif result == "You lose!":
        computer_score.set(computer_score.get() + 1)

root = tk.Tk()
root.title("Rock Paper Scissors")

user_score = tk.IntVar()
computer_score = tk.IntVar()

def reset_scores():
    user_score.set(0)
    computer_score.set(0)

tk.Label(root, text="Your Score:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, textvariable=user_score).grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Computer's Score:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, textvariable=computer_score).grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Rock", width=15, command=lambda: play_game('rock')).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Paper", width=15, command=lambda: play_game('paper')).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Scissors", width=15, command=lambda: play_game('scissors')).grid(row=2, column=2, padx=10, pady=10)

tk.Button(root, text="Reset Scores", command=reset_scores).grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Quit", command=root.quit).grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
