#Hangman in Python

import random

words =("apple","banana","grape","orange","strawberry","watermelon")

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
def display_man(wrong_guesses):
   print("**********")
   for line in dict[wrong_guesses]:
        print(line)
   print("**********")
   pass

def display_hint(hint):
   print(" ".join(hint))
   pass

def display_answer(answer):
   print(" ".join(answer))
   pass

def main():
   answer = random.choice(words)
   hint = ["_"] * len(answer)
   wrong_guesses = 0
   guessed_letters = set()
   is_running = True

   while is_running:
         display_man(wrong_guesses)
         display_hint(hint)
         guess = input("Guess a letter: ").lower()
         if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

         if guess in guessed_letters:
             print(f"You already guessed '{guess}'. Try again.")
             continue
         
         guessed_letters.add(guess)
   
         if guess in answer:
            for i in range(len(answer)):
               if answer[i] == guess:
                     hint[i] = guess
         else:
            wrong_guesses += 1

         if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You've guessed the word!")
            is_running = False
         elif wrong_guesses >= len(dict) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Game Over! You've run out of guesses.")

if __name__ == "__main__":
    main()