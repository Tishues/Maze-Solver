from graphics import Window, Line, Point

class Cell:
    def __init__(self, _win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = _win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        half_cell = abs(self._x1 - self._x2) // 2
        x_mid = half_cell + self._x1
        y_mid = half_cell + self._y1

        half_cell2 = abs(to_cell._x1 - to_cell._x2) // 2
        x_mid2 = half_cell2 + to_cell._x1
        y_mid2 = half_cell2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_mid, y_mid), Point(x_mid2, y_mid2))
        self._win.draw_line(line, fill_color)