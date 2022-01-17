import pygame
from views.Board import Board
from views.Checker import Checker
from views.KingChecker import KingChecker

class GameView(pygame.Surface):

    def __init__(self, width, height, game):
        super().__init__((width, height))
        self.fill((255, 255, 255))
        # Time
        font = pygame.font.Font(None, 42)
        text = font.render(str(round(game.get_game_time(), 2)), 1, (10, 10, 10))
        text_pos = text.get_rect()
        text_pos.centerx = self.get_rect().centerx
        text_pos.y = height * .01
        self.blit(text, text_pos)
        # Current player position
        font = pygame.font.Font(None, 42)
        text = font.render(f"Player #{str(game.get_current_player())}'s turn", 1, (10, 10, 10))
        text_pos = text.get_rect()
        text_pos.centerx = self.get_rect().centerx
        text_pos.y = height * .05
        self.blit(text, text_pos)
        # Board position
        self.board = Board(width*.9, height*.9, (255, 0, 0))
        board_pos = self.board.get_rect()
        board_pos.centerx = self.get_rect().centerx
        board_pos.y = height * 0.09
        for row in range(len(game.get_board())):
            for column in range(len(game.get_board()[row])):
                tile = game.get_board()[row][column]
                if tile != False and tile != None:
                    player = tile["player"]
                    checker_is_selected = tile["is_selected"]
                    checker_is_king = tile["is_king"]
                    tile = self.board.get_tile_positions()[row][column]
                    color = (125, 23, 125) if player == 1 else (23, 125, 23)
                    if checker_is_king:
                        checker = KingChecker(
                            tile.width, 
                            tile.height, 
                            color,
                            tile.width/2-5,
                            checker_is_selected
                        )
                    else:
                        checker = Checker(
                            tile.width, 
                            tile.height,
                            color,
                            tile.width/2-5,
                            checker_is_selected
                        )
                    checker_pos = checker.get_rect()
                    checker_pos.centerx = tile.centerx
                    checker_pos.centery = tile.centery
                    self.board.blit(checker, checker_pos)
        self.update_tile_positions(board_pos)
        self.blit(self.board, board_pos)
        # Display winner
        if game.winner:
            self.fill((240, 240, 240))
            font = pygame.font.Font(None, 42)
            text = font.render(f"Player #{game.winner} is the winner!", 1, (10, 10, 10))
            text_pos = text.get_rect()
            text_pos.centerx = self.get_rect().centerx
            text_pos.centery = self.get_rect().centery
            self.blit(text, text_pos)

    def update_tile_positions(self, board_pos):
        tile_positions = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        for row in range(len(self.board.get_tile_positions())):
            for column in range(len(self.board.get_tile_positions()[row])):
                tile = self.board.get_tile_positions()[row][column]
                tile.x = tile.x + board_pos.x
                tile.y = tile.y + board_pos.y
                tile_positions[row].append(tile)
        return tile_positions

    def get_tile_positions(self):
        return self.board.get_tile_positions()