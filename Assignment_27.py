# Drawing a Tic Tac Toe board

def user_input(player,drawBoard):
    spot = 0
    while spot == 0:
        user_choice = input("Player %s, type the position: "%(player)).split(",")
        if drawBoard[int(user_choice[0])][int(user_choice[1])] !=0:
            print("This position is already filled")
        else:
            spot = 1
    return user_choice

def board_size():
    board = int(input("What size of board would you want? "))
    return board

def player_turn(x):
    if x%2 == 0:
        turn = 1
        mark = "x"
    else:
        turn = 2
        mark = "o"
    return turn, mark

if __name__ == "__main__":
    boardSize = board_size()
    drawBoard = [[0 for x in range(boardSize)] for y in range(boardSize)]
    for x in range(0,boardSize**2):
        playerTurn, mark = player_turn(x)
        values = user_input(playerTurn,drawBoard)
        drawBoard[int(values[0])][int(values[1])] = mark
        print(drawBoard)