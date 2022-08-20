"""A Game of Tic Tak Toe"""


def print_board(board: dict):
    """Print the board to cli"""
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def check_result(tic_tak_toe: dict) -> bool:
    """Checking dictionary again win matches, if pattern found will True """
    matches = [(1, 2, 3),
               (4, 5, 6),
               (7, 8, 9),
               (1, 4, 7),
               (2, 5, 8),
               (3, 6, 9),
               (1, 5, 9),
               (3, 5, 7),
               ]
    for i, j, k in matches:
        if (tic_tak_toe[i] == tic_tak_toe[j] == tic_tak_toe[k]) and tic_tak_toe[i] != " ":
            return True
    return False


def start_a_game():
    """Trigger for starting a game"""
    tic_tak_toe = {k: " " for k in range(1, 10)}
    user_1 = input("Input first user: ")
    user_2 = input("Input Second user: ")

    user = user_1
    while True:
        try:
            move = int(input(f"Dear {user} input your move: "))  #
            if tic_tak_toe[move] == " ":
                tic_tak_toe[move] = user
            else:
                print("Place is already filled please try again..")
                continue
        except (ValueError, KeyError):
            print("invalid input, please retry")
            continue

        print_board(tic_tak_toe)
        if check_result(tic_tak_toe):
            print(f"Congratulations {user}, you Won !!!")
            break
        elif all(value != " " for value in tic_tak_toe.values()):
            print("Restart the game, this game went draw")
            break
        user = user_1 if user is user_2 else user_2  # switching turns of user


if __name__ == '__main__':
    start_a_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
