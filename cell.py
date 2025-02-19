from point import Line, Point

class Cell:
    def __init__(self, x1, x2, y1, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1  
        self._x2 = x2  
        self._y1 = y1  
        self._y2 = y2 
        self._win = win  

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line, "blue")
       
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line, "blue")

        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line, "blue")

        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line, "blue")

    def draw_move(self, to_cell, undo=False):
        # Center of the current cell
        start_x = (self._x1 + self._x2) / 2
        start_y = (self._y1 + self._y2) / 2
        p1 = Point(start_x, start_y)

        # Center of the target cell
        end_x = (to_cell._x1 + to_cell._x2) / 2
        end_y = (to_cell._y1 + to_cell._y2) / 2
        p2 = Point(end_x, end_y)

        # Color selection based on 'undo' flag
        color = "gray" if undo else "red"
        line = Line(p1, p2)
        self._win.draw_line(line, color)
