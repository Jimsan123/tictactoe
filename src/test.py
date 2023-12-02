import unittest
import pygame
import sys

# sys.path.append("../src")

from board import Board, Mark
from game import Game
from openai import OpenAI

from gpt_interface import Gpt

instance: Gpt = Gpt()

board_state: str = """
  0 1 2 3 4
0|X| | | | |
1| | | | | |
2| | | | | |
3| | | | | |
4| | | | | |
"""

board_size: int = 5
in_row_to_win: int = 3


result = instance.apiCall(board_state=board_state, board_size=board_size,
                          num_in_row_to_win=in_row_to_win, playerMark=Mark.X, gptMark=Mark.O)

print("Gpt response: ", result,)