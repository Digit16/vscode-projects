import pygame


class Ant:

    dirChange = {
        0: (1, 0),
        1: (0, 1),
        2: (-1, 0),
        3: (0, -1)
    }
    
    def __init__(self, surface, pos, moves,dir = 0):
        self.surface = surface
        self.pos = pos
        self.moves = moves
        self.dir = dir
        self.size = self.surface.get_size()


    def update(self):
        self.pos = [(self.pos[i] + self.size[i]) % self.size[i] for i in range(2)]

        pixelColor = self.surface.get_at(self.pos)
        nextColor = None

        for key, move in enumerate(self.moves):
            color, turn = move

            if pixelColor == color:
                self.dir = (self.dir + turn) % 4
                nextColor = self.moves[(key+1) % len(self.moves)][0]
                break

        self.surface.fill(nextColor, (self.pos, (1,1)))

        self.pos[0] += self.dirChange[self.dir][0]
        self.pos[1] += self.dirChange[self.dir][1]