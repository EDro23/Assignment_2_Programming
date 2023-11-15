#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:10:26 2023

@author: kaileyslaney
"""

board = ["+---", "+", "---+","---+",
         "+---", "+", "---+","---+",
         "+---", "+", "---+","---+",
         "+---", "+", "---+","---+"]

current_player = 'X'

winner = None

in_progress = True


# Print the game board

def display_board(board):
    print(board[0] + board[1] + board[2] + board[3])
    print("|   |   |   |")
    print(board[4] + board[5] + board[6] + board[7])
    print("|   |   |   |")
    print(board[8] + board[9] + board[10] + board[11])
    print("|   |   |   |")
    print(board[12] + board[13] + board[14] + board[15])
display_board(board)

# Take player input

# Check for a win or tie

