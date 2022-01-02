import pygame
from pygame.locals import *
from Menu import Menu

def main():
    pygame.init()
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pygame Checkers')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
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
                if menu.get_ai_button_pos().collidepoint(mouse_pos):
                    menu.play_ai_game()
                elif menu.get_host_button_pos().collidepoint(mouse_pos):
                    menu.host_game()
                elif menu.get_joiner_button_pos().collidepoint(mouse_pos):
                    menu.join_game()
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()