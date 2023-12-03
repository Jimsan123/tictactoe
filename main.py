import sys
import pygame
from enum import Enum
sys.path.append("src")

from board import Board, Mark
from game import Game
from gpt_interface import Gpt

class CurrentPlayerState(Enum):
    none = 0
    player = 1
    bot = 2

def main():
    # Init Pygame
    pygame.init()

    # Init stuff
    pygame.display.set_caption("Tic Tac Toe")
    main_screen = pygame.display.set_mode((900, 900))
    game = Game(main_screen, Board((900, 900), 5), 3)

    model: Gpt = Gpt()
    current_player: CurrentPlayerState = CurrentPlayerState.player

    game.Start()



    # Main game loop
    running = True

    while running:
        if current_player == CurrentPlayerState.bot:
            print("bots turn")
            model_move = model.apiCall(game.board.get_board_state(), game.board.num_cells,
                                       game.in_row_to_win, Mark.X, Mark.O)
            print("response from model: ", model_move)

            if model_move != None and game.makeMovePixelValues(model_move[0], model_move[1]):
                print(game.board.get_board_state())
                if game.hasPlayerWon(game.current_player):
                    print(f"Player {game.current_player} has won!")
                    running = False
            else:
                print("Invalid move from bot")

            game.swapPlayer()
            current_player = CurrentPlayerState.player

        elif current_player == CurrentPlayerState.player:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()

                        print("player clicked: ", pos)


                        if game.makeMovePixelValues(pos[0], pos[1]):
                            print(game.board.get_board_state())
                            if game.hasPlayerWon(game.current_player):
                                print(f"Player {game.current_player} has won!")
                                running = False

                            game.swapPlayer()
                            current_player = CurrentPlayerState.bot

                pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
