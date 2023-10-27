import pygame

ZONES = 3


def main():
    # Init Pygame
    pygame.init()

    mainScreen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Tic Tac Toe")
    draw_tic_tac_toe_board(mainScreen, ZONES)

    # Main game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         pos = pygame.mouse.get_pos()
            #         print(f"Click at {pos}")

            pygame.display.update()

    pygame.quit()


# Function to draw a Tic-Tac-Toe board of a given size
def draw_tic_tac_toe_board(screen, size):
    whiteColor = (255, 255, 255)
    blackColor = (0, 0, 0)
    board_size = min(screen.get_width(), screen.get_height())
    cell_size = board_size // size

    # TODO: in this func, use the screen size calc to get the dimensions of the boxes
    # This is then going to be used to identify in what boxes the user klicks in

    # Clear the screen
    screen.fill(blackColor)

    # Draw horizontal lines
    for row in range(1, size):
        y = row * cell_size
        pygame.draw.line(screen, whiteColor, (0, y), (board_size - 0, y), 2)

    # Draw vertical lines
    for col in range(1, size):
        x = col * cell_size
        pygame.draw.line(screen, whiteColor, (x, 0), (x, board_size - 0), 2)


if __name__ == "__main__":
    main()
