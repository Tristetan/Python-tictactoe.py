board = [
["-","-","-"],
["-","-","-"],
["-","-","-"]
]



def print_board(board):
    for row in board:
        print(row)

print_board(board)

def add_to_board(coords, board, turn):
    row = coords[0]
    col = coords[1]
    board[row][col] = turn

def quit(user_input):
    if user_input.lower() == "q":
        return True
    else:
        return False



def check_input(user_input):
    if not isnum(user_input) or not bounds(user_input):
        return False

    user_input = int(user_input)
    return True


def bounds(user_input):
    if int(user_input) > 9 or int(user_input) < 1:
        return False
    return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("This a not a  valid number")
        return False
    else:
        return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This spot is already TAKEN!!!")
        return True
    return False

def player_turn(turn_int):
    if turn_int == 1:
        return "X"
    else:
        return "O"

def win(board):
    if board[0] == ["X","X","X"]:
        print("Player 1 has WON!!")
        return True
    elif board[1] == ["X","X","X"]:
        print("Player 1 has WON!!")
        return True
    elif board[2] == ["X","X","X"]:
        print("Player 1 has WON!!")
        return True
    elif board[0] == ["O","O","O"]:
        print("Player 2 has WON!!")
        return True
    elif board[1] == ["O","O","O"]:
        print("Player 2 has WON!!")
        return True
    elif board[2] == ["O","O","O"]:
        print("Player 2 has WON!!")
        return True
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("Player 1 has WON!!")
        return True
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Player 2 has WON!!")
        return True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("Player 1 has WON!!")
        return True
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Player 2 has WON!!")
        return True
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("Player 1 has WON!!")
        return True
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Player 2 has WON!!")
        return True
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player 1 has WON!!")
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Player 2 has WON!!")
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player 1 has WON!!")
        return True
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("Player 2 has WON!!")
        return True
    for line in board:
        for position in line:
            if position == "-":
                return False
    print("CatScratch!!!")
    return True



def coordinates(user_input):
    row = int(user_input / 3)
    col = int(user_input % 3)

    return (row, col)
turn_int = 1
while True:

    user_input = input("Enter a position 1 through 9 or q to quit \n ")
    if quit(user_input) == True:
        print("Thanks For Playing")
        break
    if not check_input(user_input):
        print("Please try again")
        continue
    elif check_input(user_input):
        user_input = int(user_input) -1
        coords = coordinates(user_input)
        if not istaken(coords, board):
            turn = player_turn(turn_int)
            add_to_board(coords, board, turn)
            print_board(board)
            turn_int *= -1
        else:
            print("Please try again")
        if win(board):
            print("Play again or enter q to quit!")
            board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
            ]
            print(" ", board[0],"\n",board[1],"\n",board[2])
