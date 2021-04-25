from Game import player
from Init import (
    x, y
)

class Move:
    def Up(self):
        global y
        y += 1
        player.checkCollision(x, y)
        
    def Left(self):
        global x
        x -= 1
        player.checkCollision(x, y)
        
    def Right(self):
        global x
        x += 1
        player.checkCollision(x, y)
        
move2 = Move()
