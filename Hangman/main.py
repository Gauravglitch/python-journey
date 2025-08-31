# Hangman in Python

import random
from Hangman.words import words   # importing words list from another file

# dictionary that shows hangman drawings based on wrong guesses
dict = {0:("   ",
           "   ",
           "   "),
        1:("  O  ",
           "     ",
           "     "),
        2:("  O  ",
           "  |  ",
           "     "),
        3:("  O  ",
           " /|  ",
           "     "),
        4:("  O  ",
           " /|\\",
           "     "),
        5:("  O  ",
           " /|\\",
           " /   "),
        6:("  O  ",
           " /|\\",
           " / \\")
        }

# function to show the hangman drawing
def display_man(wrong_guesses):
   print("**********")
   for line in dict[wrong_guesses]:   # print each line of drawing
        print(line)
   print("**********")
   pass

# function to show the current hint (with underscores and guessed letters)
def display_hint(hint):
   print(" ".join(hint))
   pass

# function to show the correct answer when game ends
def display_answer(answer):
   print(" ".join(answer))
   pass

def main():
   # pick a random word for the game
   answer = random.choice(words)
   # create a hint with underscores
   hint = ["_"] * len(answer)
   wrong_guesses = 0
   guessed_letters = set()   # to store already guessed letters
   is_running = True         # game loop control

   while is_running:
         display_man(wrong_guesses)   # show hangman
         display_hint(hint)           # show word progress
         guess = input("Guess a letter: ").lower()   # get user input

         # check if input is valid (must be 1 alphabet letter)
         if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

         # check if letter was already guessed
         if guess in guessed_letters:
             print(f"You already guessed '{guess}'. Try again.")
             continue
         
         guessed_letters.add(guess)   # add new guess to set
   
         # if the guessed letter is in the word
         if guess in answer:
            for i in range(len(answer)):
               if answer[i] == guess:
                     hint[i] = guess   # replace underscore with correct letter
         else:
            wrong_guesses += 1   # if guess wrong, add to wrong guesses

         # if no underscores left, player wins
         if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You've guessed the word!")
            is_running = False
         # if wrong guesses reach max, player loses
         elif wrong_guesses >= len(dict) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Game Over! You've run out of guesses.")

# start the game if the file is run directly
if __name__ == "__main__":
    main()
