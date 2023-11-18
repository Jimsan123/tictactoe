import pygame
import sys
sys.path.append("src")

from board import Board
from game import Game

def main():
    # Init Pygame
    pygame.init()

    # Init stuff
    pygame.display.set_caption("Tic Tac Toe")
    mainScreen = pygame.display.set_mode((900, 900))
    game = Game(mainScreen, Board((900, 900), 5), 3)
    game.Start()

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
                    # game.board.markCell(mainScreen, pos[0], pos[1], nextMark)

                    if game.makeMove(pos[0], pos[1]): # if the move is legal
                        if game.hasPlayerWon(game.current_player):
                            print(f"Player {game.current_player} has won!")
                            running = False

                        game.swapPlayer()

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
