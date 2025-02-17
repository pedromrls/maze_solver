from graphics import *


def main():
    # Create a window
    win = Window(800, 600)

    # Test 1: Default cell (all walls)
    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100)

    # Test 2: Cell with no right wall
    cell2 = Cell(win, has_right_wall=False)
    cell2.draw(150, 50, 200, 100)

    # Test 3: Cell with only top and bottom walls
    cell3 = Cell(win, has_left_wall=False, has_right_wall=False)
    cell3.draw(250, 50, 300, 100)

    win.wait_for_close()


if __name__ == "__main__":
    main()
