from graphics import *
from cell import Cell


def main():
    # Create a window
    win = Window(800, 600)

    # Test 1: Default cell (all walls)
    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100)

    # Test 2: Cell with no right wall
    cell2 = Cell(
        win,  # has_right_wall=False
    )
    cell2.draw(150, 50, 200, 100)

    # Test 3: Cell with only top and bottom walls
    cell3 = Cell(win, has_left_wall=False, has_right_wall=False)
    cell3.draw(250, 50, 300, 100)

    # Test 4: Default cell draw_move
    cell4 = Cell(win)
    cell4.draw(50, 150, 100, 200)
    cell5 = Cell(win)
    cell5.draw(100, 150, 150, 200)
    cell4.draw_move_1(cell5)

    # Test 5: Default cell draw_move backtrack
    cell6 = Cell(win)
    cell6.draw(50, 250, 100, 300)
    cell7 = Cell(win)
    cell7.draw(100, 250, 150, 300)
    cell7.draw_move_1(cell6, True)

    # Test 6: Adding another line
    cell1.draw_move_1(cell4)

    # Test 7: Default cell draw_move Lane's
    # cell2 = Cell(win, # has_right_wall=False
    #              )
    # cell2.draw(150, 50, 200, 100)
    cell8 = Cell(win)
    cell8.draw(150, 150, 200, 200)
    cell9 = Cell(win)
    cell9.draw(200, 150, 250, 200)
    cell8.draw_move_2(cell9)

    # Test 8: Default cell draw_move backtrack Lane's
    cell10 = Cell(win)
    cell10.draw(150, 250, 200, 300)
    cell11 = Cell(win)
    cell11.draw(200, 250, 250, 300)
    cell11.draw_move_2(cell10, True)

    # Test 9: Adding another line Lane's
    cell2.draw_move_2(cell8)

    win.wait_for_close()


if __name__ == "__main__":
    main()
