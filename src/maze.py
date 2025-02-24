import time, random
from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None, path_width=2, path_color="turquoise"
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.path_width = path_width
        self.path_color = path_color
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.solve()

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

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        i = self._num_cols - 1
        j = self._num_rows - 1
        self._cells[i][j].has_bottom_wall = False
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current._visited = True
        cols, rows = len(self._cells), len(self._cells[0])
        while True:
            to_visit = []
            adjacent_cells = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
            for ni, nj in adjacent_cells:
                if 0 <= ni < cols and 0 <= nj < rows:
                    if not self._cells[ni][nj]._visited:
                        to_visit.append((ni, nj))
            if not to_visit:
                self._draw_cell(i, j)
                return
            else:
                ni, nj = random.choice(to_visit)
                chosen = self._cells[ni][nj]
                if ni == i - 1 and nj == j:
                    chosen.has_right_wall = False
                    current.has_left_wall = False
                if ni == i + 1 and nj == j:
                    chosen.has_left_wall = False
                    current.has_right_wall = False
                if ni == i and nj == j - 1:
                    chosen.has_bottom_wall = False
                    current.has_top_wall = False
                if ni == i and nj == j + 1:
                    chosen.has_top_wall = False
                    current.has_bottom_wall = False

                self._draw_cell(ni, nj)
                self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell._visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current._visited = True
        end = self._cells[self._num_cols - 1][self._num_rows - 1]
        if current == end:
            return True
        directions = [
            (-1, 0, "has_left_wall"),
            (1, 0, "has_right_wall"),
            (0, -1, "has_top_wall"),
            (0, 1, "has_bottom_wall"),
        ]
        for di, dj, wall_attr in directions:
            ni, nj = i + di, j + dj

            # checks that the index are valid
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                neighbor = self._cells[ni][nj]

                # dynamically checks the attributes
                if not getattr(current, wall_attr) and not neighbor._visited:
                    current.draw_move(neighbor, fill_color=self.path_color, width=self.path_width)
                    if self._solve_r(ni, nj):
                        return True
                    else:
                        current.draw_move(neighbor, fill_color=self.path_color, width=self.path_width, undo=True)
        return False
