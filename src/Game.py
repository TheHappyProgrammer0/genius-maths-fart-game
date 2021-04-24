from Init import (
    init, x, y 
)           
from Move import move 
from random import randrange

class Game:
    class Player:
        def __init__(self, x, y, health=100):
            self.x = x
            self.y = y
            self.health = health
            self.move = move
            
        def Move(self, dir):
            if self.dir == up:
                self.dir == move.Up()
            
        def checkCollision(self, x, y):
            return 0
        
        def checkHealth(self):
            return 0     
                
    def setUp(self):
        init.Display()
        init.Vars()
        
game = Game()  
