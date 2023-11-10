import pygame
from board import Board, Mark

class Game():
    def __init__(self, board: Board) -> None:
        self.board = board