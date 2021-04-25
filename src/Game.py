import pygame
from random import randrange
import Move

class Game_class:   
    class Player:            
        def __init__(self, x, y, health=100, facingAngle=0):
            self.x = x
            self.y = y
            self.health = health
            self.facingAngle = facingAngle
            self.Move = Move
                                    
        def move(self, dir):
            global x
            global y
            
            self.dir = dir            
            if self.dir == "up":
                self.x = self.Move.Up(player, x, y)
            elif self.dir == "left":
                self.Move.Left(player)
            elif self.dir == "right":
                self.Move.Right()
            
        def checkCollision(self, x, y):
            return
        
        def checkHealth(self):
            return
        
    def __init__(self, x=0, y=0, playerHealth=100, facingAngle=0):
        self.x = x
        self.y = y
        self.playerHealth = playerHealth
        self.facingAngle = facingAngle
        self.player = Game_class.Player(x, y, playerHealth, facingAngle)


x = 0
y = 0

health = 100

WIDTH = 900
HEIGHT = 1200

screen = pygame.display
display = pygame.display.set_mode((WIDTH, HEIGHT))
screen.set_caption("Genius Maths Farts Game")

facingAngle = randrange(0, 365)

game = Game_class(x, y, health, facingAngle)
player = game.player

del WIDTH, HEIGHT