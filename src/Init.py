import pygame
from random import randrange

WIDTH = 900
HEIGHT = 1200

screen = pygame.display
display = pygame.display.set_mode((WIDTH, HEIGHT))
screen.set_caption("Genius Maths Farts Game")

x = 0
y = 0

health = 100

facingAngle = randrange(0, 365)      
