import unittest
from unittest.mock import patch
import sys
import os

# Add the src directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from board import Mark, mark_to_string
class TestMarkToString(unittest.TestCase):

    def test_mark_to_string_empty(self):
        self.assertEqual(mark_to_string(Mark.empty), " ", "Should return a space for Mark.empty")

    def test_mark_to_string_O(self):
        self.assertEqual(mark_to_string(Mark.O), "O", "Should return 'O' for Mark.O")

    def test_mark_to_string_X(self):
        self.assertEqual(mark_to_string(Mark.X), "X", "Should return 'X' for Mark.X")

if __name__ == '__main__':
    unittest.main()
