board = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]


def print_board(brd):
    n = len(brd)
    for row in range(n):
        if row % 3 == 0 and row != 0:
            print("-----------------------------")
        for col in range(n):
            if col % 3 == 0 and col != 0:
                print("|", end="")
            print(f" {brd[row][col]} ", end="")
        print()


def empty_finder(brd):
    n = len(brd)

    # find an emotry possition
    for row in range(n):
        for col in range(n):
            if brd[row][col] == 0:
                return row, col

    return None


def valid(brd, num, row, col):
    n = len(brd)
    # check rows
    for i in range(n):
        if brd[row][i] == num and i != col:
            return False

    # check colums
    for i in range(n):
        if brd[i][col] == num and i != row:
            return False

    # chech box
    x = row // 3
    y = col // 3

    for i in range(x*3, x*3 + 3):
        for j in range(y*3, y*3 + 3):
            if brd[i][j] == num and i != row and j != col:
                return False

    # If all passes return true
    return True


def solver(brd):

    # if no empty possition return True
    empty = empty_finder(brd)

    if not empty:
        return True
    else:
        row, col = empty

    # try numbers 1 to 9 for every empty box
    for num in range(1, 10):
        if valid(brd, num, row, col):
            brd[row][col] = num

            if solver(brd):
                return True

        brd[row][col] = 0

    return False


def main():
    
    print_board(board)
    solver(board)
    print("\nanswer:\n")
    print_board(board)


if __name__ == "__main__":
    main()
