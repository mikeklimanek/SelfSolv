# maze.py
import tkinter as tk
from tkinter import BOTH, Canvas
import time
from window import *
from graphics import *

def main():
 win = Window(800, 600)
 maze = Maze(0, 0, 5, 5, 100, 100, win)
 win.wait_for_close()

if __name__ == "__main__":
 main()
