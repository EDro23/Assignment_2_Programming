#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:21:22 2023

@author: ethandrover

Tic Tac Toe program!

"""

def display_board(board):
    """
    Function to display the board

    Returns
    -------
    None.

    """
    for row in range(len(board)):
        print("+---+---+---+")
        print("|", end="")
        for column in range(len(board[row])):
            print(f" {board[row][column]} |", end="")
        print()
    print("+---+---+---+")

def if_winner(board):
    """
    Checks rows, columns, and diagonals if there is a winner.

    Returns
    -------
    Returns wether a player has won.

    """
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    """
    Checks if board is full.

    """
    for row in board:
        if " " in row:
            return False
    return True

def main():
    """
    Main function to run the tic tac toe game.

    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic Tac Toe")
    print()
    display_board(board)

    while True:
        print()
        row = int(input(f"{player}'s turn \nPick a row (1, 2, 3): ")) -1
        col = int(input("Pick a column (1, 2, 3): ")) -1
        print()

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = player
        display_board(board)

        winner = if_winner(board)
        if winner:
            print(f"{winner} wins!")
            print("\nGame over!")
            break
        elif is_board_full(board):
            print()
            print("It's a tie!")
            print("\nGame over!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()