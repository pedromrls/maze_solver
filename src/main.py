from graphics import *


def main():
    # Create a window
    win = Window(800, 600)

    # Test 1: Default cell (all walls)
    cell1 = Cell(50, 50, 100, 100, win)
    cell1.draw()

    # Test 2: Cell with no right wall
    cell2 = Cell(150, 50, 200, 100, win, has_right_wall=False)
    cell2.draw()

    # Test 3: Cell with only top and bottom walls
    cell3 = Cell(250, 50, 300, 100, win, has_left_wall=False, has_right_wall=False)
    cell3.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()
