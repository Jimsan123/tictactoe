import pygame
from board import Board, Mark



class Game():
    def __init__(self, mainScreen: pygame.Surface, board: Board) -> None:
        self.board = board
        self.current_player: Mark = Mark.X
        self.screen: pygame.Surface = mainScreen

    # Return
    def makeMove(self, xCoordinate: int, yCoordinate: int) -> bool:
        return self.board.markCell(self.screen, xCoordinate, yCoordinate, self.current_player)

    def swapPlayer(self) -> None:
        if self.current_player == Mark.X:
            self.current_player = Mark.O
        else:
            self.current_player = Mark.X

    def Start(self):
        self.board.draw_board(self.screen)

    def hasPlayerWon(self, playerMark: Mark) -> bool:

        if playerMark == Mark.unknown:
            assert "Cannot see if won, mark is unknown"

        for i in range(self.board.num_cells):
            # Check rows
            print("here i: ", i)
            winCount: int = 0
            for j in range(self.board.num_cells):
                print("here j: ", j)
                if self.board.cells[i][j].mark == playerMark:
                    print("winCount: ", winCount)
                    winCount += 1
                    if winCount == 5:
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


