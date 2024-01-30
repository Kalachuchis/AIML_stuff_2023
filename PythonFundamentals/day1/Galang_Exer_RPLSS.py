import random

characters = ["rock", "paper", "scissors", "lizard", "spock"]
rpsls = {
    characters[0]: {"beats": {characters[2], characters[3]}},
    characters[1]: {"beats": {characters[0], characters[4]}},
    characters[2]: {"beats": {characters[1], characters[3]}},
    characters[3]: {"beats": {characters[4], characters[1]}},
    characters[4]: {"beats": {characters[0], characters[2]}},
}
player_points = 0
computer_points = 0


def game(choice, computer_choice):
    return computer_choice in rpsls[choice]["beats"]


while True:

    print("Enter rock, paper, scissors, lizard, spock to play")
    print("type exit to quit")
    print("type help for instructions")

    player_choice = input("Enter your move: ")

    if player_choice.lower() == "exit":
        print("Game over")
        print("FINAL SCORE")
        print(f"Player: {player_points}")
        print(f"Computer: {computer_points}")
        break
    elif player_choice.lower() == "help":
        # TODO: print instructions
        continue
    elif player_choice.lower() in characters:
        print("Computer is making a move...")
        computer_choice = characters[random.randint(0, 4)]
        print(f"Computer chooses {computer_choice}")
        
        if (player_choice.lower() == computer_choice):
            print("It's a tie")
        elif game(player_choice.lower(), computer_choice):
            print("You won!")
            print(f"{player_choice.lower()} beats {computer_choice}")
            player_points += 1
        else:
            print("You lost")
            print(f"{computer_choice} beats {player_choice.lower()}")
            computer_points += 1

        continue
    else:
        print("wrong input")
