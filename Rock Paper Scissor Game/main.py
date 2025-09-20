#Rock Paper Scissors Game

import random

print("Welcome to Rock, Paper, Scissors! The rules are simple:")
print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")

choices = ["rock", "paper", "scissors"]
user_win_count = 0
computer_win_count = 0
total_rounds = 3
while total_rounds >0:
    print(f"\nRounds left: {total_rounds}")
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    
    if user_choice == 'quit':
        print("Thanks for playing! Goodbye.")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    total_rounds -= 1

    if user_choice == computer_choice:
        print("It's a tie!")
        total_rounds += 1  # Tie does not count as a round
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_win_count += 1
    else:
        print("Computer wins this round!")
        computer_win_count += 1

if user_win_count > computer_win_count:
    print("Congratulations! You won the game!")
else:
    print("Computer won the game! Better luck next time.")