from graphics import *
from cell import Cell


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

    # Test 4: Default cell draw_move
    cell4 = Cell(win)
    cell4.draw(50, 150, 100, 200)
    cell5 = Cell(win)
    cell5.draw(100, 150, 150, 200)
    cell4.draw_move(cell5)

    # Test 5: Default cell draw_move backtrack
    cell6 = Cell(win)
    cell6.draw(50, 250, 100, 300)
    cell7 = Cell(win)
    cell7.draw(100, 250, 150, 300)
    cell7.draw_move(cell6, True)

    # Test 5: Adding another line
    cell1.draw_move(cell4)

    win.wait_for_close()


if __name__ == "__main__":
    main()
