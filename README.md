# Vier Gewinnt (Connect Four)

Welcome to Vier Gewinnt!

This is a simple console-based implementation of the "Vier Gewinnt" (Connect Four) game.

## How to Play

Run the `vier_gewinnt.py` program and follow the instructions on the console to play the game.

## AI Configuration

The AI uses the Minimax algorithm to calculate moves. The search depth can be adjusted in the `ai` function in `vier_gewinnt.py`.

## Functions

- `evaluate_window(window, player)`: Evaluates the score of a window for a specific player.
- `score_position(arr, player)`: Evaluates the entire board for a specific player.
- `get_next_empty_row(arr, col)`: Returns the next empty row in a column.
- `drop_piece(arr, row, col, player)`: Drops a piece into the board.
- `is_winner(arr)`: Checks if a player has won.
- `is_winning_move(arr, move, player)`: Checks if a move results in a win.
- `minimax(arr, depth, maximizing_player, alpha, beta, player)`: Implements the Minimax algorithm.
- `log_progress(arr)`: Writes the game progress to the `log.txt` file.
- `ai(arr, player)`: AI function that calculates and executes the best move for the AI player.

## Log File

The game progress is logged in the `log.txt` file. This file contains the current game state in the form of a game board.

## Screenshot

Here is a screenshot of the game in action:

(path/to/22.png)

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```sh
   git clone https://github.com/Thenighthunte/Vier-Gewinnt-Test-1

   .git
   cd Vier-Gewinnt-Test-1
