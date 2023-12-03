import unittest
import sys
import os
from unittest.mock import Mock, patch

import pygame

# Add the src directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from board import Cell, Mark, Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.screen_size = (900, 900)
        self.num_cells = 3
        self.board = Board(self.screen_size, self.num_cells)

    def test_mark_cell_success(self):
        mock_surface = Mock(spec=pygame.Surface)  # Create a mock with the specific spec
        # Set up any necessary attributes or methods on mock_surface
        result = self.board.markCellCoordinates(mock_surface, 150, 150, Mark.X)
        self.assertTrue(result)

    # def test_mark_cell_failure(self, mock_surface):
    #     mock_surface = Mock(spec=pygame.Surface)  # Create a mock with the specific spec

    #     self.board.markCell(mock_surface, 150, 150, Mark.X)  # Mark the cell first
    #     result = self.board.markCell(mock_surface, 150, 150, Mark.O)  # Try to mark again
    #     self.assertFalse(result)

    # def test_draw_cell_x(self):
    #     cell = self.board.cells[0][0]
    #     cell.mark = Mark.X
    #     self.board.drawCell(self.mock_screen, cell)
    #     self.mock_screen.draw.line.assert_called()  # Add more specific assertions based on your implementation

    # def test_draw_cell_o(self):
    #     cell = self.board.cells[0][0]
    #     cell.mark = Mark.O
    #     self.board.drawCell(self.mock_screen, cell)
    #     self.mock_screen.draw.circle.assert_called()  # Add more specific assertions based on your implementation

    # def test_draw_cell_empty(self):
    #     cell = self.board.cells[0][0]
    #     cell.mark = Mark.empty
    #     with self.assertRaises(AssertionError):
    #         self.board.drawCell(self.mock_screen, cell)

if __name__ == '__main__':
    unittest.main()