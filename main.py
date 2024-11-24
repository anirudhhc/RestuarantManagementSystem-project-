import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    result = ""
    
    if user_choice == computer_choice:
        result = f"Draw! Both chose {computer_choice}."
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = f"You win! {user_choice} beats {computer_choice}."
    else:
        result = f"You lose! {computer_choice} beats {user_choice}."
    
    messagebox.showinfo("Result", result)

# Create the main window
window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

# Add a label for instructions
label = tk.Label(window, text="Click a button to choose Rock, Paper, or Scissors:", font=("Arial", 12))
label.pack(pady=20)

# Add buttons for user choices
rock_button = tk.Button(window, text="Rock", font=("Arial", 12), command=lambda: determine_winner("rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", font=("Arial", 12), command=lambda: determine_winner("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", font=("Arial", 12), command=lambda: determine_winner("scissors"))
scissors_button.pack(pady=10)

# Run the application
window.mainloop()
