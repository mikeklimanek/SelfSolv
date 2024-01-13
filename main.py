from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("My Window")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False


