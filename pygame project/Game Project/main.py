import pygame
import os
import random

import tiles
import mouse 


class Game:

    def __init__(self):
        self.size = self.width, self.height = (864, 576)  
        self.trueSize = (288, 192)
        

        self.win = pygame.display.set_mode((self.width, self.height))

        self.dungeonTileset = pygame.image.load(os.path.join("assets","Dungeon_Tileset.png"))
        self.map = []
        self.temp = []

    def run(self):
        run = True

        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = mouse.toGrid(mouse.scale(pygame.mouse.get_pos(), self.size, self.trueSize), (16,16))

                    self.temp.append(pos)
            
            self.draw()

        pygame.quit()

    def draw(self):

        sur = pygame.Surface(self.trueSize)

        for x in range(10):
            for y in range(10):
                tiles.Tileset.draw(tiles.Dungeon, sur, (x*16,y*16), (x,y))

        for pos in self.temp:
            #sur.fill((255,0,0), (pos, (1,1)))
            tiles.Tileset.draw(tiles.Dungeon, sur, pos, (1,1))
            

        self.win.blit(pygame.transform.scale(sur, self.size), (0, 0))

        for x in range(10):
            for y in range(10):
                tiles.Tileset.draw(tiles.Dungeon, self.win, (x*16,y*16), (x,y))

        pygame.display.update()

    def drawGrid(self, size = 16):
        for x in range(1, self.width // size+1):
            pygame.draw.line(self.win, [255]*3, (x*size, 0), (x*size, self.height), 1)
        for y in range(1, self.height // size+1):
            pygame.draw.line(self.win, [255]*3, (0, y*size), (self.width, y*size), 1)
        
g = Game()
g.run()
