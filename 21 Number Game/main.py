print("Player 2 is Computer.")
start = str(input("Do you want to start the game? (y/n): "))
if start.lower() == 'n':
    print("Exiting the game.")
    exit()
elif start.lower() != 'y':
    print("Enter 'F' to take the first chance.")
    print("Enter 'S' to take the second chance.")
    choice = str(input("Your choice (F/S): "))
    if choice.lower() == 'f':
        