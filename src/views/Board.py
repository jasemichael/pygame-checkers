import pygame

class Board(pygame.Surface):

    def __init__(self, width, height, color):
        super().__init__((width, height))
        self.fill((200, 200, 200)) # background color
        self.color = color
        self.tile_positions = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        tile_width = width*0.125
        tile_height = height*0.125
        left = 0
        top = -tile_height
        for row in range(8):
            top += tile_height
            left = 0
            for column in range(8):
            # render/save tile
                tile = self.create_tile((row+column)%2)
                tile_pos = tile.get_rect()
                tile_pos.x = left
                tile_pos.y = top
                self.blit(tile, tile_pos)
                self.tile_positions[row].append(tile_pos)
                left += tile_width
               

    def create_tile(self, primary):
        tile = pygame.Surface((self.get_width()*0.125, self.get_height()*0.125)) # 1/8 of board width/height
        if primary:
            tile.fill(self.color)
        else:
            tile.fill((0, 0, 0))
        return tile

    def get_tile_positions(self):
        return self.tile_positions