import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        print(f"It's a tie! Both chose {user}")

    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print(f"You win! {user} beats {computer}")

    elif user in ['r', 'p', 's']:
        print(f"You lose! {computer} beats {user}")

    else:
        print("Invalid input! Please choose 'r', 'p', or 's'.")

# Run the game
play()