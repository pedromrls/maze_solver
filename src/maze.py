import time
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for col_id in range(self._num_cols):
            column = []
            for row_id in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)

        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell = self._cells[i][j]
        x1_pos = self._x1 + i * self._cell_size_x
        x2_pos = x1_pos + self._cell_size_x
        y1_pos = self._y1 + j * self._cell_size_y
        y2_pos = y1_pos + self._cell_size_y
        cell.draw(x1_pos, y1_pos, x2_pos, y2_pos)
        self._animate()

    def _break_entrance_and_exit(self):
        pass

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    
