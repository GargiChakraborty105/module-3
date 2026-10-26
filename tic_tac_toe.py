
board = [" " for i in range(9)]

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner():
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return True

    return False

player = "X"

print("Welcome to Tic-Tac-Toe!")
print("Choose a position from 1 to 9.")

while True:
    display_board()

    position = int(input("Player " + player + ", enter position: "))

    if position < 1 or position > 9:
        print("Invalid position! Choose 1 to 9.")
        continue

    if board[position - 1] != " ":
        print("That position is already taken!")
        continue

    board[position - 1] = player

    if check_winner():
        display_board()
        print("Player", player, "wins! 🎉")
        break

    if " " not in board:
        display_board()
        print("It's a draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
