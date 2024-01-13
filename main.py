import tkinter as tk
from tkinter import BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("My Window")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

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
   def __init__(self, _x1, _y1, _x2, _y2, _win):
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
       if self.has_left_wall:
           self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "black")
       if self.has_right_wall:
           self._win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
       if self.has_top_wall:
           self._win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")
       if self.has_bottom_wall:
           self._win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "black")

def main():
    win = Window(800, 600)

    cell1 = Cell(0, 0, 200, 200, win)
    cell1.draw()

    cell2 = Cell(200, 0, 400, 200, win)
    cell2.has_left_wall = False
    cell2.draw()

    win.wait_for_close()



if __name__ == "__main__":
    main()


