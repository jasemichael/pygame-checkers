import pygame
from views.Checker import Checker

class KingChecker(Checker):

    def __init__(self, width, height, color, radius, is_selected):
        super().__init__(width, height, color, radius, is_selected)
        #draw crown
        start_x = self.get_rect().centerx - width/4
        start_y = self.get_rect().centery - width/8
        crown_verts = [
            (start_x, start_y),
            (start_x, start_y - height*.375),
            (start_x + width*.125, start_y - height*.25),
            (start_x + width*.25, start_y - height*.375),
            (start_x + width*.375, start_y - height*.25),
            (start_x + width*.5, start_y - height*.375),
            (start_x + width*.5, start_y),
            (start_x, start_y)
        ]
        pygame.draw.polygon(self, (230, 230, 0), crown_verts)
        