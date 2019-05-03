# drawing a board

def board_size():
    size = int(input("What size board would you like(2,3,4,...)? "))
    return size

def draw_board(size):
    for i in range(size):
        print(" ---" * size)
        print("|   " * (size+1))
    print(" ---" * size)


if __name__ == "__main__":
    boardSize = board_size()
    draw_board(boardSize)


