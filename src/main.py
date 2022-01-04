import pygame
from pygame.locals import *
from Menu import Menu
from Board import Board
from Checker import Checker
from KingChecker import KingChecker

def main():
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    BACKGROUND_COLOR = (240, 240, 240)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pygame Checkers')
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    # Menu
    menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT)
    menu_pos = menu.get_rect()
    menu_pos.centerx = background.get_rect().centerx
    background.blit(menu, menu_pos)
    screen.blit(background, (0, 0))
    pygame.display.flip()

# Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if menu: # Menu button selection
                    if menu.get_ai_button_pos().collidepoint(mouse_pos):
                        background.fill(BACKGROUND_COLOR)
                        board = Board(SCREEN_WIDTH*.95, SCREEN_HEIGHT*.95, (255, 0, 0))
                        board_pos = board.get_rect()
                        board_pos.centerx = background.get_rect().centerx
                        board_pos.centery = background.get_rect().centery

                        '''Checking to see if the KingChecker draws correctly'''
                        # for tile in board.get_tile_positions():
                        #     checker = Checker(
                        #         tile.width, 
                        #         tile.height, 
                        #         (125, 23, 125),
                        #         tile.width/2-5
                        #     )
                        #     checker_pos = checker.get_rect()
                        #     checker_pos.centerx = tile.centerx
                        #     checker_pos.centery = tile.centery
                        #     board.blit(checker, checker_pos)
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

                        background.blit(board, board_pos)
                        menu = None
                    elif menu.get_host_button_pos().collidepoint(mouse_pos):
                        background.fill(BACKGROUND_COLOR)
                        menu = None
                    elif menu.get_joiner_button_pos().collidepoint(mouse_pos):
                        background.fill(BACKGROUND_COLOR)
                        menu = None
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()