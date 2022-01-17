import pygame

class Board(pygame.Surface):

    def __init__(self, width, height, color):
        super().__init__((width, height))
        self.fill((200, 200, 200)) # background color
        self.color = color
        self.tile_positions = []
        left = 0
        top = 0
        direction = "right"
        tile_width = width*0.125
        tile_height = height*0.125
        for i in range(64):
            # render/save tile
            tile = self.create_tile(i%2)
            tile_pos = tile.get_rect()
            tile_pos.x = left
            tile_pos.y = top
            self.blit(tile, tile_pos)
            self.tile_positions.append(tile_pos)
            # change position for next tile
            if direction == "right":
                left += tile_width
                if left >= width:
                    direction = "left"
                    left -= tile_width
                    top += tile_height
            elif direction == "left":
                left -= tile_width
                if left < 0:
                    direction = "right"
                    left += tile_width
                    top += tile_height

    def create_tile(self, primary):
        tile = pygame.Surface((self.get_width()*0.125, self.get_height()*0.125)) # 1/8 of board width/height
        if primary:
            tile.fill(self.color)
        else:
            tile.fill((0, 0, 0))
        return tile

    def get_tile_positions(self):
        return self.tile_positions