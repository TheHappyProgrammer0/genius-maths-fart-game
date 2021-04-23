import pygame
import socket

x = 0
y = 0

WIDTH = 900
HEIGHT = 1000

class Init:
    
    global display
    global in_game
    global x
    global y
    
    def Display(self):
        display = pygame.display.set_mode((WIDTH, HEIGHT))
        
    def Vars(self, x, y):
        x = 0
        y = 0
        in_game = True

init = Init()
