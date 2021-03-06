import pygame
from random import (
    randrange, choice
)
from os.path import join
from Game import (
    x, y, facingAngle, display
)

class World:
    def __init__(self, x, y, facingAngle=9, pictureFolder="src", grassblock_name="grass_texture.jpeg", dirtblock_name="dirt_texture.jpeg"):
        self.x = x
        self.y = y
        self.facingAngle = randrange(0, 360)
        self.north = 0
        self.east = 90
        self.south = 180
        self.west = 360
        self.pictureFolder = pictureFolder
        self.grassblock_name = grassblock_name
        self.dirtblock_name = dirtblock_name
        self.grassblock = pygame.image.load(# join(self.pictureFolder, self.grassblock_name)
                                            "/home/pi/git/genius-maths-fart-game/src/pictures/grass_texture.jpeg"
        )
        self.dirtblock = pygame.image.load(
            # join(self.pictureFolder, self.dirtblock_name)
            "/home/pi/git/genius-maths-fart-game/src/pictures/dirt_texture.jpeg"
        )
        self.textureChoice = [self.grassblock, self.dirtblock]
        
    def Generate(self, x, y):
        display.blit(choice(self.textureChoice), (self.x, self.y))
        pygame.display.update()     