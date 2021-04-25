import pygame
from os.path import join

class Member:
    def __init__(self, picName=".png", folderName="Pictures"):
        self.picName = picName
        self.folderName = folderName
        
    def createPicture(self):
        picture = pygame.image.load(join(self.folderName, self.picName))
        
