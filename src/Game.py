from Init import (
    x, y 
)           
from Move import move2
from random import randrange

class Game:
    class Player:
        def __init__(self, x, y, health=100):
            self.x = x
            self.y = y
            self.health = health
                        
        def Move(self, dir):
            self.dir = dir            
            if self.dir == "up":
                move2.Up()
            elif self.dir == "left":
                move2.Left()
            elif self.dir == "right":
                move2.Right()
            
        def checkCollision(self, x, y):
            return
        
        def checkHealth(self):
            return
        
game = Game()  
player = game.Player(x, y)

#test
# test2