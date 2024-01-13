# tests.py
import unittest
from main import Maze

class Tests(unittest.TestCase):
 def test_maze_create_cells(self):
     num_cols = 12
     num_rows = 10
     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
     self.assertEqual(
         len(m1._cells),
         num_rows,
     )
     self.assertEqual(
         len(m1._cells[0]),
         num_cols,
     )

 def test_maze_create_cells_with_diff_dimensions(self):
     num_cols = 8
     num_rows = 6
     m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
     self.assertEqual(
         len(m2._cells),
         num_rows,
     )
     self.assertEqual(
         len(m2._cells[0]),
         num_cols,
     )

 def test_maze_create_cells_with_no_window(self):
     num_cols = 10
     num_rows = 10
     m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
     self.assertEqual(
         len(m3._cells),
         num_rows,
     )
     self.assertEqual(
         len(m3._cells[0]),
         num_cols,
     )

if __name__ == "__main__":
 unittest.main()