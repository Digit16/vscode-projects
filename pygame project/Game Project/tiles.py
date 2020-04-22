import pygame
import os


class Tileset:
    def draw(self, surface, pos, tile):
        surface.blit(self.tileset, pos, (tile[0]*self.size[0],tile[1]*self.size[1],self.size[0],self.size[1]))

class Dungeon:
    tileset = pygame.image.load(os.path.join("assets","Dungeon_Tileset.png"))
    size = (16, 16)

    WALL_LEFT_1 = (0,0)
    WALL_LEFT_2 = (0,1)
    WALL_LEFT_3 = (0,2)
    WALL_LEFT_4 = (0,3)
    WALL_UP_1 = (1,0)
    WALL_UP_2 = (2,0)
    WALL_UP_3 = (3,0)
    WALL_UP_4 = (4,0)


