board = [
    ["|1|", "|2|", "|3|"],
    ["|4|", "|5|", "|6|"],
    ["|7|", "|8|", "|9|"]
]

user = True  # True - X, False - O
turns = 0


def print_board(board):
    for row in board:
        for slot in row:
            print(slot + " ", end="")
        print()
        print("------------")


def check_input(user_input):
    # проверяем число ли это
    if not isnum(user_input): return False
    user_input = int(user_input)
    # проверяем входит ли в диапозон 1-9
    if not bounds(user_input): return False
    return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("Это не число из интервала 1-9.")
        return False
    else:
        return True


def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("Это не число из интервала 1-9.")
        return False
    else:
        return True


def coordinates(user_input):
    row = int(user_input / 3)
    col = int(user_input % 3)
    return (row, col)


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] == "X" or board[row][col] == "O":
        print("Эта ячейка уже занята.")
        return True
    else:
        return False


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "X"
    else:
        return "O"


def iswin(active_user, board):
    if check_row(active_user, board): return True
    if check_col(active_user, board): return True
    if check_diag(active_user, board): return True
    return False


def check_row(active_user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != active_user:
                complete_row = False
                break
        if complete_row: return True
    return False


def check_col(active_user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != active_user:
                complete_col = False
                break
        if complete_col: return True
    return False


def check_diag(active_user, board):
    if board[0][0] == active_user and board[1][1] == active_user and board[2][2] == active_user:
        return True
    elif board[0][2] == active_user and board[1][1] == active_user and board[2][0] == active_user:
        return True
    else:
        return False


while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Пожалуйста, введите число от 1 до 9.")
    if not check_input(user_input):
        print("Пожалуйста, попробуйте снова.")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Пожалуйста, попробуйте снова.")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} победил!")
        break

    turns += 1
    if turns == 9: print("Ничья!")
    user = not user

