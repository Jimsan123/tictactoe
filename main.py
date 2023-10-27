import pygame


def main():
    # Init Pygame
    pygame.init()

    mainScreen = pygame.display.set_mode((900, 700))  # Window size
    pygame.display.set_caption("Tic Tac Toe")
    drawBoardLines(mainScreen)

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


def drawBoardLines(screen):
    whiteColor = (255, 255, 255)
    lineWidth = 5
    # Line 1 Vertical
    startPos = (300, 100)
    endPos = (300, 600)
    pygame.draw.line(screen, whiteColor, startPos, endPos, lineWidth)
    # Line 2 Vertical
    startPos = (550, 100)
    endPos = (550, 600)
    pygame.draw.line(screen, whiteColor, startPos, endPos, lineWidth)
    # Line 1 Horizontal
    startPos = (150, 250)
    endPos = (700, 250)
    pygame.draw.line(screen, whiteColor, startPos, endPos, lineWidth)
    # Line 2 Horizontal
    startPos = (150, 450)
    endPos = (700, 450)
    pygame.draw.line(screen, whiteColor, startPos, endPos, lineWidth)


if __name__ == "__main__":
    main()
