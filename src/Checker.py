import pygame
from pygame.constants import SRCALPHA

class Checker(pygame.Surface):

    def __init__(self, width, height, color, radius):
        super().__init__((width, height), flags=SRCALPHA)
        self.fill(pygame.Color(0, 0, 0, 0))
        pygame.draw.circle(self, color, (self.get_rect().centerx, self.get_rect().centery), radius)