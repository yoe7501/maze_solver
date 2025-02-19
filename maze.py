import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []  
        self._create_cells()

    def _create_cells(self):
       
        for col in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, x2, y1, y2, self.win)
                column.append(cell)
            self._cells.append(column)

      
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
  
        cell = self._cells[i][j]
        cell.draw()  
        self._animate()

    def _animate(self):
    
        self.win.redraw()
        time.sleep(0.05)  
