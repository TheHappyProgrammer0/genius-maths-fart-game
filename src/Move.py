from Init import(
    x, y
)
import pygame

class Move:
    
    global x
    global y
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def Up(self):
        y += 1
                
    def Left(self):
        x -= 1
        
    def Right(self):
        x += 1
        
move = Move(x, y)