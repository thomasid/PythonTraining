# Game of rock paper scissors
decision = "yes"
while decision.lower() == "yes":
    first_player = input("Player one: rock, paper, scissors? ")
    second_player = input("Player two: rock, paper, scissors? ")
    if first_player.lower() == second_player.lower():
        print("It's a draw")
    elif first_player.lower()== "paper" and second_player.lower() == "rock":
        print("Player 1 wins!")
    elif first_player.lower()== "scissors" and second_player.lower() == "paper":
        print("Player 1 wins!")
    elif first_player.lower() == "rock" and second_player.lower() == "scissors":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
    decision = input("Would you like to keep playing (yes/no)? ")
print("End of the game")