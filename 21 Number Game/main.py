# 21 Number Game
import random

last_num = 0 #game starts before "1"
nums = [] #will store the full sequence


while True:
    #Players' turns
    move = int(input("How many numbers will you say? (1-3): "))

    for i in range(1,move+1):
        next_num = last_num + 1
        last_num = next_num
        nums.append(next_num)

        if next_num == 21:
            print("You said:", nums[-move:]) #show only the last numbers said
            print("Numbers so far:", nums) #show all numbers said
            print("You reached 21! You lose!")
            exit()

    print("You said:", nums[-move:]) #show only the last numbers said
    print("Numbers so far:", nums) #show all numbers said

    #Computer's turn
    comp_move = random.randint(1, 3)

    for i in range(1,comp_move+1):
        next_num = last_num + 1
        last_num = next_num 
        nums.append(next_num)

        if next_num == 21:
            print("Computer says:", nums[-comp_move:]) #show only the last numbers said
            print("Numbers so far:", nums) #show all numbers said
            print("Computer reached 21! You win!")
            exit()

    print("Computer says:", nums[-comp_move:]) #show only the last numbers said
    print("Numbers so far:", nums) #show all numbers said


