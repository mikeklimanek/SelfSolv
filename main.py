import tkinter as tk
from tkinter import BOTH, Canvas
import time
from window import *
from graphics import *

def main():
    num_rows = 40
    num_cols = 40
    margin = 70
    screen_x = 1600
    screen_y = 1200
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze can not be solved")
    else:
        print("Maze solved")

    win.wait_for_close()

if __name__ == "__main__":
 main()
