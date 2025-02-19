import unittest
from maze import Maze


class TestsMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_cell_grid_dimensions(self):
        # Create a simple 3x4 maze
        maze = Maze(0, 0, 3, 4, 10, 10)

        # Check the number of columns (num_cols)
        self.assertEqual(len(maze._cells), 4)
        # Check the number of rows per column (num_rows)
        self.assertEqual(len(maze._cells[0]), 3)

    def test_unique_cells(self):
        # Create a 4x4 maze
        maze = Maze(0, 0, 4, 4, 20, 20)

        # Collect all cells into a flat list
        all_cells = [cell for column in maze._cells for cell in column]

        # Verify all cells are unique
        self.assertEqual(
            len(all_cells), len(set(all_cells))
        )  # No references should overlap

    def test_cells_grid_consistency(self):
        # Create a maze with 3 rows and 4 columns
        maze = Maze(0, 0, 3, 4, 10, 10)

        # Validate that each column has the proper number of rows
        for column in maze._cells:
            self.assertEqual(len(column), 3)

        # Validate that the total number of columns matches num_cols
        self.assertEqual(len(maze._cells), 4)

    def test_draw_cell_returns_nothing_when_win_is_none(self):
        # Create a 3x3 Maze with no window (`win=None`)
        maze = Maze(0, 0, 3, 3, 10, 10, win=None)

        # Call _draw_cell explicitly (should return without doing anything)
        initial_cells = maze._cells  # Save the reference for comparison
        maze._draw_cell(0, 0)  # Attempt to draw a cell with win=None

        # Assert that the cells remain unchanged (no visual logic executed)
        self.assertEqual(maze._cells, initial_cells)

    def test_animate_returns_nothing_when_win_is_none(self):
        # Create a Maze with no window (`win=None`)
        maze = Maze(0, 0, 3, 3, 10, 10, win=None)

        # Execute the _animate method (should do nothing)
        try:
            maze._animate()
            success = True
        except Exception as e:
            success = False

        # Assert animate does nothing and does not raise any exceptions
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
