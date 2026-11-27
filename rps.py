import random

rps = ["rock", "paper", "scissors"]
comp = random.choice(rps)


def check_self(player):
    if player == rps[0]:
        print("You chose rock, computer chose", comp)
    elif player == rps[1]:
        print("You chose paper, computer chose", comp)
    elif player == rps[2]:
        print("You chose scissors, computer chose", comp)


def determine_win(player):
    if comp == player:
        print("Both players selected", player + ". It's a tie!")
    elif comp == rps[0] and player == rps[2]:
        print("Scissors can't cut rock. Computer wins!")
    elif comp == rps[0] and player == rps[1]:
        print("Paper covers rock! You win!")
    elif comp == rps[1] and player == rps[0]:
        print("Rock can't beat paper! Computer wins!")
    elif comp == rps[1] and player == rps[2]:
        print("Scissors cuts paper! You win!")
    elif comp == rps[2] and player == rps[0]:
        print("Rock crushes scissors! You win!")
    elif comp == rps[2] and player == rps[1]:
        print("Scissors cuts paper! Computer wins!")


def new_game():
    while True:
        game_decision = input("Do you want to play another game? [Yes/No]: ")
        if game_decision == "Yes":
            return True
        elif game_decision == "No":
            return False
        else:
            print("Invalid input. Please type Yes or No.")


while True:
    self_choice = input("Enter a choice (rock, paper, scissors): ")
    if self_choice in rps:
        check_self(self_choice)
        determine_win(self_choice)
        if not new_game():
            break
        comp = random.choice(rps)
    else:
        print("Invalid choice. Please try again.")
