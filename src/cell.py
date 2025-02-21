from graphics import Line, Point


class Cell:
    def __init__(
        self,
        win=None,
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
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
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
        else:
            left_wall = Line(__top_left, __bottom_left)
            self._win.draw_line(left_wall, fill_color="white")
        if self.has_right_wall:
            right_wall = Line(__top_right, __bottom_right)
            self._win.draw_line(right_wall)
        else:
            right_wall = Line(__top_right, __bottom_right)
            self._win.draw_line(right_wall, fill_color="white")
        if self.has_top_wall:
            top_wall = Line(__top_left, __top_right)
            self._win.draw_line(top_wall)
        else:
            top_wall = Line(__top_left, __top_right)
            self._win.draw_line(top_wall, fill_color="white")
        if self.has_bottom_wall:
            bottom_wall = Line(__bottom_left, __bottom_right)
            self._win.draw_line(bottom_wall)
        else:
            bottom_wall = Line(__bottom_left, __bottom_right)
            self._win.draw_line(bottom_wall, fill_color="white")

    def draw_move(self, to_cell, fill_color, width, undo=False):
        if undo:
            fill_color = "gray"

        center_point_c1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        center_point_c2 = Point(
            (to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2
        )
        self._win.draw_line(Line(center_point_c1, center_point_c2), fill_color=fill_color, width=width)
