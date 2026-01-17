import random

choices = ["rock", "paper", "scissors"]

# Score counters
wins = 0
losses = 0
ties = 0

while True:
    user = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user == "quit":
        print("Final Score -> Wins:", wins, "Losses:", losses, "Ties:", ties)
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    
    if user == computer:
        ties += 1
        print("It's a tie!")
    elif user == "rock":
        wins += 1
    elif user == "paper":
        wins += 1
    elif user == "scissors":
        wins += 1
    else:
        losses += 1

    print("Current Score -> Wins:", wins, "Losses:", losses, "Ties:", ties)
