import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0
        self.round_number = 0

        self.choice_label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.choice_label.pack(pady=10)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score - You: 0, Computer: 0")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)

    def play_game(self, user_choice):
        self.round_number += 1
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = self.determine_winner(user_choice, computer_choice)

        messagebox.showinfo("Result", f"Round {self.round_number}\nYou chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

        if 'win' in result:
            self.user_score += 1
        elif 'lose' in result:
            self.computer_score += 1

        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    def update_score_label(self):
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def play_again(self):
        response = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if response:
            # Reset the game for a new round
            self.round_number = 0
            self.update_score_label()
            self.result_label.config(text="")
        else:
            messagebox.showinfo("Thanks", "Thanks for playing! Goodbye!")
            self.root.destroy()

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
