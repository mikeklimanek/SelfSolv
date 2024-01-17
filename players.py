from tkinter import *
from graphics import *
from window import *
from main import *

class Player:
    def __init__(self, x, y, radius=10, color="red"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw_player(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=self.color)
