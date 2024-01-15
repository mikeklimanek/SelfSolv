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
 win = Window(800, 600)
 center_window(win)
 maze = Maze(0, 0, 5, 5, 100, 100, win)
 maze._break_entrance_and_exit()
 win.wait_for_close()

if __name__ == "__main__":
 main()
