from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height, title="Maze Solver"):
        self.__root = Tk()
        self.__root.title(title)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color=fill_color)

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(
        self,
        win,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        __top_left = Point(x1, y1)
        __top_right = Point(x2, y1)
        __bottom_left = Point(x1, y2)
        __bottom_right = Point(x2, y2)
        if self.has_left_wall:
            left_wall = Line(__top_left, __bottom_left)
            self._win.draw_line(left_wall)

        if self.has_right_wall:
            right_wall = Line(__top_right, __bottom_right)
            self._win.draw_line(right_wall)

        if self.has_top_wall:
            top_wall = Line(__top_left, __top_right)
            self._win.draw_line(top_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(__bottom_left, __bottom_right)
            self._win.draw_line(bottom_wall)
