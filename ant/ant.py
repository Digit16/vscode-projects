import pygame
import os
import random

from antclass import Ant


class Game:

    def __init__(self):
        self.size = (100, 100)     
        self.trueSize = (100, 100)  
        
        self.win = pygame.display.set_mode(self.size)
        self.sur = pygame.Surface(self.trueSize)

        self.antPos = [self.trueSize[i]//2 for i in range(2)]
        self.antDir = 0

        self.antMoves = []

        self.antMoves.append( ((0,0,0), -1) )
        self.antMoves.append(((255,255,255), 1))
        """
        self.antMoves.append(((255,0,255), -1))
        self.antMoves.append(((255,255,0), 1))
        self.antMoves.append(((0,255,255), -1))
        self.antMoves.append(((0,0,255), 1))
        """


        self.border = False


        self.dirChange = {
            0: (1, 0),
            1: (0, 1),
            2: (-1, 0),
            3: (0, -1)
        }

    def run(self):
        run = True

        clock = pygame.time.Clock()
        self.ants = []
        self.ants.append(Ant(self.sur, (self.antPos[0] + 1, self.antPos[1] + 0), self.antMoves, 0))
        self.ants.append(Ant(self.sur, (self.antPos[0] + -1, self.antPos[1] + 0), self.antMoves, 2))
        self.ants.append(Ant(self.sur, (self.antPos[0] + 0, self.antPos[1] + 1), self.antMoves, 1))
        self.ants.append(Ant(self.sur, (self.antPos[0] + 0, self.antPos[1] + -1), self.antMoves, 3))


        """
        """


        while run:
            clock.tick(600)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()
        pygame.quit()

    def draw(self):

        for ant in self.ants:
            ant.update()


        self.win.blit(pygame.transform.scale(self.sur, self.size), (0, 0))
        pygame.display.update()
        
g = Game()
g.run()
