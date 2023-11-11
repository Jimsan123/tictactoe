import unittest
import pygame
import sys

sys.path.append("../src")

from board import Board, Mark
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.main_surface = pygame.Surface((300, 300))
        self.board = Board((900, 900), 3)  # Create a 3x3 board
        self.game = Game(self.main_surface, self.board)

    def test_current_player_swapping(self):
        # Initially, the current player should be Mark.X
        self.assertEqual(self.game.current_player, Mark.X)

        # Make a move (e.g., at coordinates (0, 0))
        self.game.makeMove(0, 0)

        # After the first move, the current player should be Mark.O
        self.assertEqual(self.game.current_player, Mark.O)

        # Make another move (e.g., at coordinates (1, 1))
        self.game.makeMove(1, 1)

        # After the second move, the current player should be Mark.X again
        self.assertEqual(self.game.current_player, Mark.X)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
