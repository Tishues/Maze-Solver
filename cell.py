from graphics import Window, Line, Point

class Cell(Window):
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

    def draw(self, _x1, _y1, _x2, _y2):
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        if self.has_left_wall:
            line = Line(Point(_x1, _y1), Point(_x1, _y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(_x1, _y1), Point(_x2, _y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(_x2, _y1), Point(_x2, _y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(_x1, _y2), Point(_x2, _y2))
            self._win.draw_line(line)