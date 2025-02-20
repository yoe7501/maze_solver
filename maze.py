import random
import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []  
        self._create_cells()
        self.seed = seed
        if seed != None:
            random.seed(seed)

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
        self._break_entrance_and_exit()

        self._break_walls_r(0,0)

    def _draw_cell(self, i, j):
  
        cell = self._cells[i][j]
        cell.draw()  
        self._animate()

    def _animate(self):
    
        self.win.redraw()
        time.sleep(0.05)  

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()

        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].draw()

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            # List of potential next cells (direction, new_i, new_j)
            neighbors = []

            # Check the cell to the left
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append(('left', i - 1, j))

            # Check the cell to the right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append(('right', i + 1, j))

            # Check the cell above
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append(('top', i, j - 1))

            # Check the cell below
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append(('bottom', i, j + 1))

            # If no unvisited neighbors, backtrack
            if not neighbors:
                self._draw_cell(i, j)
                return

            # Pick a random direction to move
            direction, new_i, new_j = random.choice(neighbors)
            next_cell = self._cells[new_i][new_j]

            # Break the wall between current_cell and next_cell
            if direction == 'left':
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == 'right':
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif direction == 'top':
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == 'bottom':
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False

            # Redraw cells after breaking the wall
            self._draw_cell(i, j)
            self._draw_cell(new_i, new_j)

            # Recursive call to continue the maze generation
            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
       
        self._reset_cells_visited() 
        return self._solve_r(0, 0)


    def _solve_r(self, i, j):
      
        self._animate()  # Visualize progress
        current_cell = self._cells[i][j]
        current_cell.visited = True

        # ✅ Check if the current cell is the goal
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # 🔽 Try moving down
        if j + 1 < self.num_rows and not current_cell.has_bottom_wall:
            next_cell = self._cells[i][j + 1]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                if self._solve_r(i, j + 1):
                    return True
                current_cell.draw_move(next_cell, undo=True)

        # 🔼 Try moving up
        if j - 1 >= 0 and not current_cell.has_top_wall:
            next_cell = self._cells[i][j - 1]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                if self._solve_r(i, j - 1):
                    return True
                current_cell.draw_move(next_cell, undo=True)

        # ▶️ Try moving right
        if i + 1 < self.num_cols and not current_cell.has_right_wall:
            next_cell = self._cells[i + 1][j]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                if self._solve_r(i + 1, j):
                    return True
                current_cell.draw_move(next_cell, undo=True)

        # ◀️ Try moving left
        if i - 1 >= 0 and not current_cell.has_left_wall:
            next_cell = self._cells[i - 1][j]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                if self._solve_r(i - 1, j):
                    return True
                current_cell.draw_move(next_cell, undo=True)

        # ❌ Dead end
        return False


