import sys
import pygame
sys.path.append("src")

from board import Board
from game import Game
from gpt_interface import Gpt

def main():
    # Init Pygame
    pygame.init()

    # Init stuff
    pygame.display.set_caption("Tic Tac Toe")
    main_screen = pygame.display.set_mode((900, 900))
    game = Game(main_screen, Board((900, 900), 5), 3)

    model: Gpt = Gpt()

    game.Start()



    # Main game loop
    running = True

    while running:

        # TODO: create a statemachine that swappes betwwen the model and the player :D


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.K_q:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if game.makeMove(pos[0], pos[1]):
                        print(game.board.get_board_state())
                        if game.hasPlayerWon(game.current_player):
                            print(f"Player {game.current_player} has won!")
                            running = False

                        game.swapPlayer()

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
