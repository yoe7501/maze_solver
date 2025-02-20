import unittest
from window import Window
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_break_wall(self):
        win = Window(800,600)
        maze = Maze(5,5,6,8,100,100,win)
        self.assertEqual(maze._cells[0][0].has_top_wall, False)
if __name__ == "__main__":
    unittest.main()