from graphics import *


def main():
    win = Window(800, 600, "Test Window")
    point_1 = Point(0, 0)
    point_2 = Point(800, 600)
    line = Line(point_1, point_2)
    line2 = Line(Point(800, 0), Point(0, 600))
    win.draw_line(line, "black")
    win.draw_line(line2, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
