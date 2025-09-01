# 21 Number Game
import random

last_number = 0 #game starts before "1"

while True:
    #Players' turns
    move = int(input("How many numbers will you say? (1-3): "))

    #update last_number
    last_number += move

    print("You said:", last_number)

    if last_number >= 21:
        print("You reached 21! You lose!")
        break

    #Computer's turn
    comp_move = random.randint(1, 3)
    last_number += comp_move
    print("Computer says:", last_number)

    if last_number >= 21:
        print("Computer reached 21! You win!")
        break


