from main import *

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