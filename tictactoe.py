# Simple game of tic tac toe 
import numpy as np
import random
import time 
import tkinter as tk
import tkinter.messagebox as msgbox

class TicTacToe :
    def __init__ (self):
        self.board = np.array([[' ' for _ in range(3)] for _ in range(3)])
        self.current_winner = None
    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')
    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']  
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return len(self.available_moves())
    def make_move(self, square, letter):
        if self.board[square[0]][square[1]] == ' ':
            self.board[square[0]][square[1]] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        row_ind, col_ind = square
        if all([self.board[row_ind][c] == letter for c in range(3)]):
            return True
        if all([self.board[r][col_ind] == letter for r in range(3)]):
            return True
        if row_ind == col_ind and all([self.board[i][i] == letter for i in range(3)]):
            return True
        if row_ind + col_ind == 2 and all([self.board[i][2-i] == letter for i in range(3)]):
            return True
        return False
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'
        time.sleep(0.8)
    if print_game:
        print('It\'s a tie!')

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'Enter your move (row,col) for {self.letter}: ')
            try:
                row, col = map(int, square.split(','))
                if (row, col) in game.available_moves():
                    valid_square = True
                    val = (row, col)
                else:
                    print('This square is already occupied. Try again.')
            except:
                print('Invalid input. Please enter row and column as two numbers separated by a comma.')
        return val
class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)