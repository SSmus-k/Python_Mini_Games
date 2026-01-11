import tkinter as tk
from snakegame import SnakeGame

def start_game():
    root.destroy()
    game = SnakeGame()
    game.run()

root = tk.Tk()
root.title("Snake Game")

btn = tk.Button(root, text="Start Game", font=("Arial", 16), command=start_game)
btn.pack(padx=40, pady=40)

root.mainloop()
