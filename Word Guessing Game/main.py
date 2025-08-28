import random

words_list = ["python", "java", "kotlin", "javascript", "ruby", "swift", "go", "rust", "typescript", "scala"]

guesses = ""
trys = 12

target_word = random.choice(words_list)

print("Welcome to the Word Guessing Game!")
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! You have {trys} attempts to guess the word.")
print("The word has", len(target_word), "letters.")
print('_' * len(target_word))
print("Let's begin!")
guessed_char = input("Guess a character: ").lower()

