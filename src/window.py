from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height, title="Maze Solver"):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title(title)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False

    def redraw():
        self.root.update_idletasks() 
        self.root.update() 
        

    def wait_for_close():
        pass

    def close():
        pass