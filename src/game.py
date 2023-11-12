import pygame
from board import Board, Mark



class Game():
    def __init__(self, mainScreen: pygame.Surface, board: Board) -> None:
        self.board = board
        self.current_player: Mark = Mark.X
        self.screen: pygame.Surface = mainScreen

    def makeMove(self, xCoordinate: int, yCoordinate: int) -> Mark:
        self.board.markCell(self.screen, xCoordinate, yCoordinate, self.current_player)

        if self.hasPlayerWon(self.current_player):
            return self.current_player

        if self.current_player == Mark.X:
            self.current_player = Mark.O
        else:
            self.current_player = Mark.X

        return Mark.unknown

    def Start(self):
        self.board.draw_board(self.screen)

    def hasPlayerWon(self, playerMark: Mark) -> bool:

        if playerMark == Mark.unknown:
            assert "Cannot see if won, mark is unknown"

        for i in range(self.board.num_cells):
            # Check rows
            if all(self.board.cells[i][j].mark == playerMark for j in range(self.board.num_cells)):
                print("Won on rows")
                return True

            # Check columns
            if all(self.board.cells[j][i].mark == playerMark for j in range(self.board.num_cells)):
                print("Won on columns")
                return True

        # Check diagonals
        if all(self.board.cells[i][i].mark == playerMark for i in range(self.board.num_cells)) or \
            all(self.board.cells[i][(self.board.num_cells - 1) - i].mark == playerMark for i in range(self.board.num_cells)):
            print("Won on diagonals")
            return True

        return False


