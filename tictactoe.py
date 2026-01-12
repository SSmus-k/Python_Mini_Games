import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def make_move(self, row, col, letter):
        if self.board[row][col] == ' ':
            self.board[row][col] = letter
            if self.winner(row, col, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, r, c, letter):
        if all(self.board[r][i] == letter for i in range(3)):
            return True
        if all(self.board[i][c] == letter for i in range(3)):
            return True
        if r == c and all(self.board[i][i] == letter for i in range(3)):
            return True
        if r + c == 2 and all(self.board[i][2 - i] == letter for i in range(3)):
            return True
        return False


class TicTacToeGUI:
    def __init__(self):
        self.game = TicTacToe()
        self.current_player = 'X'

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    self.root,
                    text=' ',
                    font=('Arial', 24),
                    width=5,
                    height=2,
                    command=lambda r=r, c=c: self.on_click(r, c)
                )
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

        self.root.mainloop()

    def on_click(self, row, col):
        if self.game.make_move(row, col, self.current_player):
            self.buttons[row][col]['text'] = self.current_player

            if self.game.current_winner:
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.root.destroy()
                return

            if all(self.game.board[r][c] != ' ' for r in range(3) for c in range(3)):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.root.destroy()
                return

            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    TicTacToeGUI()
