# finding Tic Tac Toe winner

game = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]

winner_is_2 = [[2, 2, 0], [2, 1, 0],[2, 1, 1]]

winner_is_1 = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],[2, 1, 0],[2, 1, 1]]

no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 2]]

also_no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 0]]

def finding_winner():
    list = no_winner
    winner = 0
    for i in range(1,3):
        if list[0][0] == i and list[0][1] == i and list[0][2] == i:
            print("The winner is player no. %s"%(i))
        elif list[1][0] == i and list [1][1] == i and list[1][2] == i:
            print("The winner is player no. %s" % (i))
        elif list[2][0] == i and list[2][1] == i and list[2][2] == i:
            print("The winner is player no. %s" % (i))
        elif list[0][0] == i and list[1][0] == i and list[2][0] == i:
            print("The winner is player no. %s" % (i))
        elif list[0][1] == i and list[1][1] == i and list[2][1] == i:
            print("The winner is player no. %s" % (i))
        elif list[0][2] == i and list[1][2] == i and list[2][2] == i:
            print("The winner is player no. %s" % (i))
        elif list[0][0] == i and list[1][1] == i and list[2][2] == i:
            print("The winner is player no. %s" % (i))
        elif list[0][2] == i and list[1][1] == i and list[2][0] == i:
            print("The winner is player no. %s" % (i))
        else:
            winner +=1
    if winner == 2:
        print("Nobody won..")

finding_winner()