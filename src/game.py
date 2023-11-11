import pygame
from board import Board, Mark



class Game():
    def __init__(self, mainScreen: pygame.Surface, board: Board) -> None:
        self.board = board
        self.current_player: Mark = Mark.X
        self.screen: pygame.Surface = mainScreen

    def makeMove(self, xCoordinate: int, yCoordinate: int):
        self.board.markCell(self.screen, xCoordinate, yCoordinate, self.current_player)
        if self.current_player == Mark.X:
            self.current_player = Mark.O
        else:
            self.current_player = Mark.X

    def Start(self):
        self.board.draw_board(self.screen)

    def isGameOver():



        pass

