from main import *
from graphics import *
from tkinter import *
from players import *

class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="light grey", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.player = Player(100, 100)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    def draw_text(self, x, y, text, font="Helvetica", size=20, color="red"):
        self.__canvas.create_text(x, y, text=text, font=(font, size), fill=color)

    def bind_keys(self):
        self.__root.bind('<KeyPress-w>', lambda event: self.move_player(0, -10))
        self.__root.bind('<KeyPress-a>', lambda event: self.move_player(-10, 0))
        self.__root.bind('<KeyPress-s>', lambda event: self.move_player(0, 10))
        self.__root.bind('<KeyPress-d>', lambda event: self.move_player(10, 0))

    def close(self):
        self.__running = False



