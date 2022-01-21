import pygame
from views.GameView import GameView
from views.Menu import Menu
from Game import Game
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
                    if self.screen == "menu": # Menu screen
                        if menu.get_ai_button_pos().collidepoint(mouse_pos): # selected AI button
                            self.game = Game()
                            self.update()
                            self.screen = "game"
                        elif menu.get_host_button_pos().collidepoint(mouse_pos): # selected host button
                            self.background.fill(self.background_color)
                            self.screen = "game"
                        elif menu.get_joiner_button_pos().collidepoint(mouse_pos): # selected join button
                            self.background.fill(self.background_color)
                            self.screen = "game"
                    elif self.screen == "game":
                        for row in range(len(self.game_view.get_tile_positions())):
                            for column in range(len(self.game_view.get_tile_positions()[row])):
                                tile = self.game_view.get_tile_positions()[row][column]
                                if tile.collidepoint(mouse_pos):
                                    selected_checker = self.game.get_selected_checker()
                                    pos = (row, column)
                                    is_checker = self.game.is_checker(pos)
                                    tile = self.game.get_tile(pos)
                                    if not selected_checker:
                                        self.game.select_checker(pos)
                                    elif selected_checker and is_checker:
                                        self.game.select_checker(pos)
                                    elif selected_checker and not self.game.is_checker(pos):
                                        self.game.move_checker(pos)
                                    break
            if self.screen == "game":
                self.update()
            self.window.blit(self.background, (0, 0))
            pygame.display.flip()

    def update(self):
        self.game_view = GameView(
            self.get_window_width(), 
            self.get_window_height(), 
            self.game
        )
        self.game_view_pos = self.game_view.get_rect()
        self.game_view_pos.centerx = self.background.get_rect().centerx
        self.game_view_pos.centery = self.background.get_rect().centery
        self.render(self.game_view, self.game_view_pos)

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