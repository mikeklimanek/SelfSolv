import tkinter as tk
from tkinter import BOTH, Canvas
import time
from graphics import *
from window import *
from players import *

def main():
    num_rows = 20
    num_cols = 20
    margin = 70
    screen_x = 1600
    screen_y = 1200
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    win.draw_text(90, 55, "Start", color="red")
    win.draw_text(screen_x - 90, screen_y - 55, "End", color="red")

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)


    win.bind_keys()

    print("Maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze can not be solved")
    else:
        print("Maze solved")

    win.wait_for_close()

if __name__ == "__main__":
 main()
