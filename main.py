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

    # Config
    display_size = (900, 900)
    board_size = 5
    in_row_to_win = 4

    # Init stuff
    pygame.display.set_caption("Tic Tac Toe")
    main_screen = pygame.display.set_mode(display_size)
    game = Game(main_screen, Board(display_size, board_size), in_row_to_win)

    model: Gpt = Gpt()
    current_player: CurrentPlayerState = CurrentPlayerState.player

    game.Start()

    print("Welcome to the game of TicTacToe!!")
    print("A screen will popup, click within any square/cell to make a move")
    print("After choosing a move, the selected model will make a move")
    print("First to the set amount in row wins")
    print("Have fun!!! :)")

    # Main game loop
    running = True

    while running:
        if current_player == CurrentPlayerState.bot:
            print("Bots turn")
            model_move = model.apiCall(game.board.get_board_state(), game.board.num_cells,
                                       game.in_row_to_win, Mark.X, Mark.O)
            # model_move = (0, 0)
            print("Response from model: ", model_move)

            if model_move != None and game.makeMoveValues(model_move[0], model_move[1]):
                print(game.board.get_board_state())
                if game.hasPlayerWon(game.current_player):
                    print(f"Player {game.current_player} has won!")
                    running = False
                # Swap player
                game.swapPlayer()
                current_player = CurrentPlayerState.player
            else:
                print("Invalid move from bot")


        elif current_player == CurrentPlayerState.player:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()

                        if game.makeMoveCoords(pos[0], pos[1]):
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
