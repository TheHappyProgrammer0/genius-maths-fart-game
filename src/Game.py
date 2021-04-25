from Move import move

class Game:   
    class Player:
        def __init__(self, x, y, health=100):
            self.x = x
            self.y = y
            self.health = health
            self.facingAngle = facingAngle
            self.move = move
                        
        def Move(self, dir):
            self.dir = dir            
            if self.dir == "up":
                move.Up()
            elif self.dir == "left":
                move.Left()
            elif self.dir == "right":
                move.Right()
            
        def checkCollision(self, x, y):
            return
        
        def checkHealth(self):
            return
        
    def __init__(self, facingAngle=0, x=0, y=0, playerHealth=100):
        self.x = x
        self.y = y
        self.playerHealth = playerHealth
        self.player = Player(x, y, playerHealth)