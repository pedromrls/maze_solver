import time
from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = (x1,)
        self.y1 = (y1,)
        self.num_rows = (num_rows,)
        self.num_cols = (num_cols,)
        self.cell_size_x = (cell_size_x,)
        self.cell_size_y = (cell_size_y,)
        self.win = (win,)
        self._create_cells()

    def _create_cells(self):
        self._cells = []

    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        time.sleep(0.05)
