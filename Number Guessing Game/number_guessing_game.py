import random

print("!!! NUMBER GUESSING GAME !!!")

lower_limit = int(input('Enter the lower limit: '))
upper_limit = int(input('Enter the upper limit: '))

target_num = random.randint(lower_limit, upper_limit)
guess_count = 0
guess_limit = 7

print("You have total of 7 guesses.")

while guess_count < guess_limit:
    try:
        guess_num = int(input('Enter your guess: '))
        guess_count +=1
        
        if guess_num < lower_limit or guess_num > upper_limit:
            print(f"Please guess under the range of {lower_limit} and {upper_limit}")
        elif guess_num < target_num:
            print('Too Low')
        elif guess_num > target_num:
            print('Too High')
        else:
            print(f'Congratulations! The number was {target_num} and it took you {guess_count} guesses.')
            break
        print(f"You have {guess_limit - guess_count} guesses left.")
    except ValueError:
        print("Invalid input! Please enter a number.")
else:
    print(f"Out of guesses. The number was {target_num}")


