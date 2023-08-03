from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board, sign_of_move, player):
    ok = False
    while not ok:
        move = input(f"{player} move: ")
        ok = len(move) == 1 and move >= "1" and move <= "9"  # check if input is valid?
        if not ok:
            print("Bad move - repeat your input!")  
            continue
        move = int(move) - 1  # cell's number from 0 to 8
        row = move // 3  # cell's row
        col = move % 3  # cell's column
        sign = board[row][col]  # check the selected square
        ok = sign not in ["O", "X"]
        if not ok:  # if it's occupied - to the input again
            print("Field already occupied - repeat your input!")
            continue
    board[row][col] = sign_of_move  # set '0' at the selected square


def make_list_of_free_fields(board):
    free = []  # the list is empty initially
    for row in range(3):  # iterate through rows
        for col in range(3):  # iterate through columns
            if board[row][col] not in ["O", "X"]:  # check if the cell is free?
                free.append((row, col))  # if it is - append new tuple to the list
    return free


def victory_for(board, sgn):
    if sgn == "X":
        who = "player 2"
    elif sgn == "O":
        who = "player 1"
    else:
        who = None
    cross1 = cross2 = True  # for diagonals
    for rc in range(3):
        if (
            board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn
        ):  # check row rc
            return who
        if (
            board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn
        ):  # check column rc
            return who
        if board[rc][rc] != sgn:  # check 1st diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # check 2nd diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = make_list_of_free_fields(board)  # make a list of free fields
    cnt = len(free)
    if cnt > 0:  # if the list is not empty, choose a place for 'X' and set it
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = "X"


def get_game_type():
    game_type = input(
        """
Press 1 to play with computer,
Press 2 to play with a friend.
"""
    )
    try:
        game = int(game_type)
        if game == 1:
            return 1
        elif game == 2:
            return 2
        else:
            print("Invalid Game Type")
            exit()
    except ValueError:
        print("Invalid Input.")
        exit()


def start_game():
    game_type = get_game_type()

    board = [
        [3 * j + i + 1 for i in range(3)] for j in range(3)
    ]  # make an empty board using List comprehension

    free = make_list_of_free_fields(board)

    player_1 = True  # For checking turn

    while len(free):
        display_board(board)
        if player_1:
            enter_move(board, "O", "player 1")
            victor = victory_for(board, "O")
        else:
            if game_type == 1:
                draw_move(board)
            else:
                enter_move(board, "X", "player 2")

            victor = victory_for(board, "X")
        if victor != None:
            break
        player_1 = not player_1  # switching the turn
        free = make_list_of_free_fields(board)

    display_board(board)

    if victor == "player 1":
        print("player 1 won!")
    elif victor == "player 2":
        print("player 2 won")
    else:
        print("Tie!")


start_game()
