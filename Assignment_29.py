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

def draw_board(size):
    for i in range(size):
        print(" ---" * size)
        print("|   " * (size+1))
    print(" ---" * size)

def player_turn(x):
    if x%2 == 0:
        turn = 1
        mark = "x"
    else:
        turn = 2
        mark = "o"
    return turn, mark

def finding_winner(boardCheckup,mark):
    winner = 0
    diagonal_check_l = []
    diagonal_check_r = []
    for j in range(0,len(boardCheckup)):
        row_check = []
        col_check = []
        for m in range(0,len(boardCheckup)):
            row_check.append(boardCheckup[j][m])
            col_check.append(boardCheckup[m][j])
        diagonal_check_l.append(boardCheckup[j][j])
        diagonal_check_r.append(boardCheckup[len(boardCheckup)-1-j][len(boardCheckup)-1-j])
        # row check
        if len(set(row_check)) == 1 and 0 not in set(row_check):
            winner = who_won(row_check,boardCheckup)
        # column check
        elif len(set(col_check)) == 1 and 0 not in set(col_check):
            winner = who_won(col_check,boardCheckup)
    # diagonal check
    if len(set(diagonal_check_l)) == 1 and 0 not in set(diagonal_check_l):
        winner = who_won(diagonal_check_l,boardCheckup)
    elif len(set(diagonal_check_r)) == 1 and 0 not in set(diagonal_check_r):
        winner = who_won(diagonal_check_r,boardCheckup)
    return winner

def who_won(checkup,board):
    winner = 0
    if "".join(checkup) == "x" * len(board):
        print("Player number 1 won!")
        winner = 1
    elif "".join(checkup) == "o" * len(board):
        print("Player number 2 won!")
        winner = 2
    return winner


if __name__ == "__main__":
    winCount = [0,0]
    decision = "y"
    while decision == "y":
        boardSize = int(input("What size of board would you want? "))
        drawBoard = [[0 for x in range(boardSize)] for y in range(boardSize)]
        draw_board(boardSize)
        for x in range(0, boardSize ** 2):
            playerTurn, mark = player_turn(x)
            values = user_input(playerTurn, drawBoard)
            drawBoard[int(values[0])][int(values[1])] = mark
            winner = finding_winner(drawBoard, mark)
            for y in range(boardSize):
                print(drawBoard[y])
            if winner == 1:
                winCount[0] += 1
                break
            elif winner == 2:
                winCount[2] += 1
                break
        if winner == 0:
            print("Nobody won...")
        print("The score is: Player no.1 won %s times, Player no.2 won %s times"%(winCount[0],winCount[1]))
        decision = input("Play again?(y/n): ")