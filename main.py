# maze.py
import tkinter as tk
from tkinter import BOTH, Canvas
import time
from window import Window

class Point:
 def __init__(self, x, y):
     self.x = x
     self.y = y

class Line:
 def __init__(self, start_point, end_point):
     self.start_point = start_point
     self.end_point = end_point

 def draw(self, canvas, fill_color):
     canvas.create_line(
         self.start_point.x, self.start_point.y,
         self.end_point.x, self.end_point.y,
         fill=fill_color, width=2
     )

class Cell:
 def __init__(self, _x1, _y1, _x2, _y2, _win=None):
     self.x1 = _x1
     self.y1 = _y1
     self.x2 = _x2
     self.y2 = _y2
     self._win = _win
     self.has_left_wall = True
     self.has_right_wall = True
     self.has_top_wall = True
     self.has_bottom_wall = True

 def draw(self):
     if self._win is not None:
         if self.has_left_wall:
             self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "black")
         if self.has_right_wall:
             self._win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
         if self.has_top_wall:
             self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")
         if self.has_bottom_wall:
             self._win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "black")

 def draw_move(self, to_cell, undo=False):
     start_x = self.x1 + ((self.x2 - self.x1) // 2)
     start_y = self.y1 + ((self.y2 - self.y1) // 2)
     end_x = to_cell.x1 + ((to_cell.x2 - to_cell.x1) // 2)
     end_y = to_cell.y1 + ((to_cell.y2 - to_cell.y1) // 2)
     color = "gray" if undo else "red"
     if self._win is not None:
         self._win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), color)

class Maze:
 def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
     self.x1 = x1
     self.y1 = y1
     self.num_rows = num_rows
     self.num_cols = num_cols
     self.cell_size_x = cell_size_x
     self.cell_size_y = cell_size_y
     self._win = win
     self._cells = [[None]*num_cols for _ in range(num_rows)]
     self._create_cells()

 def _create_cells(self):
     for i in range(self.num_rows):
         for j in range(self.num_cols):
             x1 = self.x1 + j * self.cell_size_x
             y1 = self.y1 + i * self.cell_size_y
             x2 = x1 + self.cell_size_x
             y2 = y1 + self.cell_size_y
             cell = Cell(x1, y1, x2, y2, self._win)
             self._cells[i][j] = cell
             self._draw_cell(cell, i, j)

 def _draw_cell(self, cell, i, j):
     cell.draw()
     if self._win is not None:
         self._animate()

 def _animate(self):
     if self._win is not None:
         self._win.redraw()
         time.sleep(0.05)

def main():
 win = Window(800, 600)
 maze = Maze(0, 0, 5, 5, 100, 100, win)
 win.wait_for_close()

if __name__ == "__main__":
 main()
