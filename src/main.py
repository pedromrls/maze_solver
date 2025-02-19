from graphics import *
from cell import Cell
from maze import Maze


def main():
    # Create a window
    win = Window(800, 600)
    maze = Maze(5, 5, 6, 8, 80, 60, win)
    maze._break_entrance_and_exit()
    win.wait_for_close()


if __name__ == "__main__":
    main()
