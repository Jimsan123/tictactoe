import pygame
from enum import Enum

class Mark(Enum):
    undefined = 0
    O = 1
    X = 2

class Cell():
    def __init__(self, topLeft: tuple[int, int], botRight: tuple[int, int], mark: Mark = Mark.undefined) -> None:
        self.topLeft: tuple[int, int] = topLeft
        self.botRight: tuple[int, int] = botRight
        self.mark: Mark = mark

    def isMarked(self) -> bool:
        return self.mark != Mark.undefined

class Board():
    def __init__(self, screen_size: tuple[int, int], num_cells: int) -> None:
        self.num_cells: int = num_cells
        self.board_size: tuple[int, int] = screen_size
        self.cell_size: int = min(self.board_size) // num_cells

        # This creates list of all cells
        # Format example:
        # [[((0, 0),   (300, 300)), ((300, 0),   (600, 300)), ((600, 0),   (900, 300))],
        # [( (0, 300), (300, 600)), ((300, 300), (600, 600)), ((600, 300), (900, 600))],
        # [( (0, 600), (300, 900)), ((300, 600), (600, 900)), ((600, 600), (900, 900))]]
        # Starts horizontally with the x row
        self.cells: list[list[Cell]] = \
            [[Cell((i * self.cell_size, j * self.cell_size), ((i+1) * self.cell_size, (j+1) * self.cell_size))
            for i in range(num_cells)] for j in range(num_cells)]



    def markCell(self, xCoordinate: int, yCoordinate: int, mark: Mark) -> None:
        # Find the cell to mark
        for rows in self.cells:
            for cell in rows:
                if (xCoordinate >= cell.topLeft[0] and xCoordinate < cell.botRight[0] and # [0] will is the X pos
                    yCoordinate >= cell.topLeft[1] and yCoordinate < cell.botRight[1]): # [1] will is the Y pos
                    cell.mark = mark
                    print("found")
                    return



    # Function to draw a Tic-Tac-Toe board of a given size
    def draw_board(self, screen: pygame.Surface) -> None:
        whiteColor = (255, 255, 255)
        blackColor = (0, 0, 0)


        # Clear the screen
        screen.fill(blackColor)

        # Draw horizontal lines
        for row in range(1, self.num_cells):
            y = row * self.cell_size
            pygame.draw.line(screen, whiteColor, (0, y), (min(self.board_size) - 0, y), 2)

        # Draw vertical lines
        for col in range(1, self.num_cells):
            x = col * self.cell_size
            pygame.draw.line(screen, whiteColor, (x, 0), (x, min(self.board_size) - 0), 2)

        # # Test to see self.cells
        # for horizontallCells in self.cells:
        #     for cell in horizontallCells:
        #         pygame.draw.rect(screen, (255, 0, 0), cell, 5)

