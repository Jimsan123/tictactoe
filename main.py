import pygame
from board import Board, Mark

def main():
    # Init Pygame
    pygame.init()

    # Init stuff
    game_board = Board((900, 900), 3)

    mainScreen = pygame.display.set_mode(game_board.board_size)
    pygame.display.set_caption("Tic Tac Toe")
    game_board.draw_board(mainScreen)

    # Main game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.K_q:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    print(f"Click at {pos}")
                    game_board.markCell(pos[0], pos[1], Mark.X)

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
