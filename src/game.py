import pygame
from board import Board, Mark


class Game():
    def __init__(self, mainScreen: pygame.Surface, board: Board, in_row_to_win: int) -> None:
        self.board = board
        self.current_player: Mark = Mark.X
        self.screen: pygame.Surface = mainScreen
        self.in_row_to_win: int = in_row_to_win

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

        if playerMark == Mark.empty:
            assert "Cannot see if won, mark is unknown"

        # Check rows and columns
        for i in range(self.board.num_cells):
            # Check rows
            winCount: int = 0
            for j in range(self.board.num_cells):
                if self.board.cells[i][j].mark == playerMark:
                    winCount += 1
                    if winCount == self.in_row_to_win:
                        print("Won on rows")
                        return True
                else:
                    winCount = 0

            # Check columns
            winCount: int = 0
            for j in range(self.board.num_cells):
                if self.board.cells[j][i].mark == playerMark:
                    winCount += 1
                    if winCount == self.in_row_to_win:
                        print("Win on columns")
                        return True
                else:
                    winCount = 0

        # Check diagonals

        # Function to check a single diagonal
        def check_diagonal(start_row, start_col, row_increment, col_increment):
            winCount = 0
            row, col = start_row, start_col
            while 0 <= row < self.board.num_cells and 0 <= col < self.board.num_cells:
                if self.board.cells[row][col].mark == playerMark:
                    winCount += 1
                    if winCount == self.in_row_to_win:
                        return True
                else:
                    winCount = 0  # reset count if sequence is broken
                row += row_increment
                col += col_increment
            return False

        # Check all diagonals from top left to bottom right
        for start_row in range(self.board.num_cells - self.in_row_to_win + 1):
            for start_col in range(self.board.num_cells - self.in_row_to_win + 1):
                if check_diagonal(start_row, start_col, 1, 1):
                    print("Won on a diagonal from top left to bottom right")
                    return True

        # Check all diagonals from top right to bottom left
        for start_row in range(self.board.num_cells - self.in_row_to_win + 1):
            for start_col in range(self.in_row_to_win - 1, self.board.num_cells):
                if check_diagonal(start_row, start_col, 1, -1):
                    print("Won on a diagonal from top right to bottom left")
                    return True


        return False
