from main import *

class Window(tk.Tk):
 def __init__(self, width, height):
     super().__init__()
     self.title("My Window")
     self.canvas = tk.Canvas(self, width=width, height=height)
     self.canvas.pack()
     self.running = False
     self.protocol("WM_DELETE_WINDOW", self.close)

 def redraw(self):
     self.update_idletasks()
     self.update()

 def wait_for_close(self):
     self.running = True
     while self.running:
         self.redraw()

 def close(self):
     self.running = False

 def draw_line(self, line, fill_color):
     line.draw(self.canvas, fill_color)