def print_board(board):
    print("  0   1   2   3   4")
    print("+" + "---+" *5)
    for row in board:
        print("|", " | ".join(row), "|")
        print("+" + "---+" * 5)  # Adjusted for five columns
    print("  5   6   7   8   9")
def check_winner(board, player):
    # Check horizontally
    for row in range(6):
        for col in range(3):  # Adjusted for five columns
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertically
    for col in range(5):  # Adjusted for five columns
        for row in range(3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonally (positive slope)
    for row in range(3):
        for col in range(3):  # Adjusted for five columns
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonally (negative slope)
    for row in range(3, 6):
        for col in range(3):  # Adjusted for five columns
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def initialize_board():
    return [[" " for _ in range(5)] for _ in range(6)]  # Adjusted for five columns

def main():
    print("Welcome to Vier Gewinnt!")

    while True:
        board = initialize_board()
        last_moves = []

        while True:
            print_board(board)
            player = "x" if is_board_full(board) or sum(row.count("x") for row in board) <= sum(row.count("o") for row in board) else "o"
            move = input(f"akt. Spieler: {player},   Spalte eingeben   oder Drück'r' um eine neue Spiele anzufangen : ")

            if move.lower() == 'r':
                break  # Start a new game

            if len(move) == 1 and move.isdigit() and 0 <= int(move) <= 4:  # Adjusted for five columns
                col = int(move)
                if any(board[i][col] == " " for i in range(3)):  # Check for empty spaces from the top
                    for i in range(2, -1, -1):
                        if board[i][col] == " ":
                            board[i][col] = player
                            last_moves.append((i, col, player))
                            break
                else:
                    print("Column is full. Try again.")
                    continue
            elif len(move) == 1 and move.isdigit() and 5 <= int(move) <= 9:  # Check for stones dropped from the top
                col = int(move)
                if any(board[i][col - 5] == " " for i in range(3, 6)):  # Check for empty spaces from the bottom
                    for i in range(3, 6):
                        if board[i][col - 5] == " ":
                            board[i][col - 5] = player
                            last_moves.append((i, col - 5, player))
                            break
                else:
                    print("Column is full. Try again.")
                    continue
            elif len(move) == 2 and move[:-1].isdigit() and 0 <= int(move[:-1]) <= 9 and (move[-1] == "x" or move[-1] == "o"):
                col = int(move[:-1])
                stone_type = move[-1]
                if any(board[i][col] == " " for i in range(3)):  # Check for empty spaces from the top
                    for i in range(2, -1, -1):
                        if board[i][col] == " ":
                            if last_moves and last_moves[-1][2] != player and last_moves[1][:2] == (i,* col):
                                # Bonus stone condition
                                board[i][col] = player.upper() + stone_type
                            else:
                                board[i][col] = player + stone_type
                            last_moves.append((i, col, player))
                            break
                else:
                    print("Column is full. Try again.")
                    continue
            elif len(move) == 2 and move[:-1].isdigit() and 5 <= int(move[:-1]) <= 9 and (move[-1] == "x" or move[-1] == "o"):
                col = int(move[:-1])
                stone_type = move[-1]
                if any(board[i][col - 5] == " " for i in range(3, 6)):  # Check for empty spaces from the bottom
                    for i in range(3, 6):
                        if board[i][col - 5] == " ":
                            if last_moves and last_moves[1][2] != player and last_moves[1][:2] == (i,* col - 5):
                                # Bonus stone condition
                                board[i][col - 5] = player.upper() + stone_type
                            else:
                                board[i][col - 5] = player + stone_type
                            last_moves.append((i, col - 5, player))
                            break
                else:
                    print("Column is full. Try again.")
                    continue
            else:
                print("Invalid move. Choose a valid row.")
                continue

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
def process_sequence(sequence, board, last_moves):
    for move in sequence:
        if move.lower() == 'r':
            return True  # Start a new game

        if len(move) == 1 and move.isdigit() and 0 <= int(move) <= 9:
            row = int(move)
            if any(board[row][col] == " " for col in range(5)):
                col = last_moves[-1][1]  # Get the last column played
                player = last_moves[-1][2]  # Get the last player
                stone_type = 'x' if player == 'o' else 'o'  # Switch stone type for the bonus stone

                if board[row][col] == " ":
                    if last_moves and last_moves[-1][2] != player and last_moves[-1][0] == row:
                        # Bonus stone condition
                        board[row][col] = player.upper() + stone_type
                    else:
                        board[row][col] = player + stone_type
                    last_moves.append((row, col, player))
                else:
                    print("Row is full. Try again.")
                    return False
            else:
                print("Invalid move. Choose a valid row.")
                return False
        elif len(move) == 2 and move[:-1].isdigit() and 0 <= int(move[:-1]) <= 9 and (move[-1] == "x" or move[-1] == "o"):
            row = int(move[:-1])
            col = last_moves[-1][1]  # Get the last column played
            player = last_moves[-1][2]  # Get the last player
            stone_type = move[-1]  # Use the specified stone type

            if board[row][col] == " ":
                if last_moves and last_moves[-1][2] != player and last_moves[-1][0] == row:
                    # Bonus stone condition
                    board[row][col] = player.upper() + stone_type
                else:
                    board[row][col] = player + stone_type
                last_moves.append((row, col, player))
            else:
                print("Row is full. Try again.")
                return False
        else:
            print("Invalid move. Choose a valid row.")
            return False

    return True


            

if __name__ == "__main__":
    main()
