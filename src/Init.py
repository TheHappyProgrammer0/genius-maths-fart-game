import pygame
from random import randrange
from Game import Game

x = 0
y = 0

health = 100

WIDTH = 900
HEIGHT = 1200

screen = pygame.display
display = pygame.display.set_mode((WIDTH, HEIGHT))
screen.set_caption("Genius Maths Farts Game")

facingAngle = randrange(0, 365)      

game = Game(facingAngle, x, y, health)

del WIDTH, HEIGHT
