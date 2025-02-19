
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self,canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)