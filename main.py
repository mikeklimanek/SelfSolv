import tkinter as tk
from tkinter import BOTH, Canvas
import time
from window import *
from graphics import *

def center_window(win):
   win.update_idletasks()
   width = win.winfo_width()
   height = win.winfo_height()
   x = win.winfo_screenwidth() // 2 - width // 2
   y = win.winfo_screenheight() // 2 - height // 2
   win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()

if __name__ == "__main__":
 main()
