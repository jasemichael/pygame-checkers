import pygame
from views.Menu import Menu
from views.Board import Board
from views.KingChecker import KingChecker
from pygame.locals import *

class Controller:

    def __init__(self):
        pygame.init()
        self.load_config()
        self.window = pygame.display.set_mode((self.get_window_width(), self.get_window_height()))
        pygame.display.set_caption('Pygame Checkers')
        self.background = pygame.Surface(self.window.get_size())
        self.background_color = (240, 240, 240)
        self.screen = "menu"

    def render(self, surface, position):
        self.background.fill(self.background_color)
        self.background.blit(surface, position)
        self.window.blit(self.background, (0, 0))
        pygame.display.flip()

    def run(self):
        # Run event loop
        menu = Menu(self.get_window_width(), self.get_window_height())
        menu_pos = menu.get_rect()
        menu_pos.centerx = self.background.get_rect().centerx
        self.render(menu, menu_pos)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.screen == "menu": # Menu button selection
                        if menu.get_ai_button_pos().collidepoint(mouse_pos):
                            board = Board(self.get_window_width()*.95, self.get_window_height()*.95, (255, 0, 0))
                            board_pos = board.get_rect()
                            board_pos.centerx = self.background.get_rect().centerx
                            board_pos.centery = self.background.get_rect().centery
                            for tile in board.get_tile_positions():
                                kingChecker = KingChecker(
                                    tile.width, 
                                    tile.height, 
                                    (125, 23, 125),
                                    tile.width/2-5
                                )
                                checker_pos = kingChecker.get_rect()
                                checker_pos.centerx = tile.centerx
                                checker_pos.centery = tile.centery
                                board.blit(kingChecker, checker_pos)
                            self.render(board, board_pos)
                            self.screen = "game"
                        elif menu.get_host_button_pos().collidepoint(mouse_pos):
                            self.background.fill(self.background_color)
                            self.screen = "game"
                        elif menu.get_joiner_button_pos().collidepoint(mouse_pos):
                            self.background.fill(self.background_color)
                            self.screen = "game"
            self.window.blit(self.background, (0, 0))
            pygame.display.flip()

    def load_config(self):
        # Load user config from json file
        self.set_window_width(800)
        self.set_window_height(800)

    def get_window_width(self):
        return self.window_width

    def set_window_width(self, window_width):
        self.window_width = window_width

    def get_window_height(self):
        return self.window_height

    def set_window_height(self, window_height):
        self.window_height = window_height

    def set_config(self):
        pass