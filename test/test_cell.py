import unittest
import io
from unittest.mock import patch
import sys
import os

# Add the src directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from board import Cell, Mark

class TestCell(unittest.TestCase):
    def test_initialization(self):
        cell = Cell((0, 0), (2, 2))
        self.assertEqual(cell.topLeft, (0, 0))
        self.assertEqual(cell.botRight, (2, 2))
        self.assertEqual(cell.mark, Mark.empty)

    def test_corner_coordinates(self):
        cell = Cell((0, 0), (2, 2))
        self.assertEqual(cell.topRight, (2, 0))
        self.assertEqual(cell.botLeft, (0, 2))

    # def test_print_corners(self):
    #     cell = Cell((0, 0), (2, 2))
    #     expected_output = f"""
    #     Top left: (0, 0), Top right: (2, 0)\n
    #     Bot left: (0, 2), Bot right: (2, 2)"""
    #     with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    #         cell.printCorners()
    #         self.assertEqual(fake_stdout.getvalue().strip(), expected_output)

    def test_is_marked(self):
        cell_empty = Cell((0, 0), (2, 2))
        cell_marked = Cell((0, 0), (2, 2), Mark.X)  # Replace 'Mark.someValue' with an actual mark value

        self.assertFalse(cell_empty.isMarked())
        self.assertTrue(cell_marked.isMarked())

if __name__ == '__main__':
    unittest.main()
