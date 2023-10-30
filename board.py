import pygame

class Board():
    def __init__(self, screen_size, num_zones) -> None:
        self.num_zones = num_zones
        self.board_size = screen_size
        self.cell_size = min(self.board_size) // num_zones

        # This creates list of all cells
        # Format example: 
        # [[((0, 0), (300, 300)), ((300, 0), (600, 300)), ((600, 0), (900, 300))], 
        # [((0, 300), (300, 600)), ((300, 300), (600, 600)), ((600, 300), (900, 600))], 
        # [((0, 600), (300, 900)), ((300, 600), (600, 900)), ((600, 600), (900, 900))]]
        # Starts horizontally with the x row
        self.cells = [[((i * self.cell_size, j * self.cell_size), ((i+1) * self.cell_size, (j+1) * self.cell_size)) 
                       for i in range(num_zones)] for j in range(num_zones)]
        print(self.cells[0][0])


    # Function to draw a Tic-Tac-Toe board of a given size
    def draw_board(self, screen):
        whiteColor = (255, 255, 255)
        blackColor = (0, 0, 0)

        print(self.cell_size)

        # Clear the screen
        screen.fill(blackColor)

        # Draw horizontal lines
        for row in range(1, self.num_zones):
            y = row * self.cell_size
            pygame.draw.line(screen, whiteColor, (0, y), (min(self.board_size) - 0, y), 2)

        # Draw vertical lines
        for col in range(1, self.num_zones):
            x = col * self.cell_size
            pygame.draw.line(screen, whiteColor, (x, 0), (x, min(self.board_size) - 0), 2)
    


