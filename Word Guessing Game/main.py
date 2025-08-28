# Importing the random module to select a random word from the list
import random

# List of words to choose from
words_list = ["python", "java", "kotlin", "javascript", "ruby", "swift", "go", "rust", "typescript", "scala"]

# Initializing variables
guesses = ""
turns = 12

# Selecting a random word from the list
target_word = random.choice(words_list)

# Game introduction
print("Welcome to the Word Guessing Game!")
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! You have {turns} attempts to guess the word.")
print("The word has", len(target_word), "letters.")
print('_ ' * len(target_word))
print("Let's begin!")

# Main game loop
while turns > 0:
    failed = 0
    # Displaying the current state of the guessed word
    for char in target_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    # Checking if the user has guessed all letters
    if failed == 0:
        print("\nCongratulations! You've guessed the word:", target_word)
        break
    # Taking user input for a letter guess
    guess = input("\nGuess a letter: ").lower()
    # Validating the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue
    if guess in guesses:
        print("You have already guessed that letter. Try another one.")
        continue
    # Adding the guessed letter to the list of guesses
    guesses += guess
    # Checking if the guessed letter is in the target word
    if guess not in target_word:
        turns -= 1
        print(f"Wrong guess. You have {turns} attempts left.")
        if turns == 0:
            print("Sorry, you've run out of attempts. The word was:", target_word)