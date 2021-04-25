from Move import Move

class Game:   
    class Player:      
        def __init__(self, x, y, health=100, facingAngle=0):
            self.x = x
            self.y = y
            self.health = health
            self.facingAngle = facingAngle
            self.move2 = Move()
                        
        def move(self, dir):
            self.dir = dir            
            if self.dir == "up":
                self.move2.Up()
            elif self.dir == "left":
                self.move2.Left()
            elif self.dir == "right":
                self.move2.Right()
            
        def checkCollision(self, x, y):
            return
        
        def checkHealth(self):
            return
        
    def __init__(self, x=0, y=0, playerHealth=100, facingAngle=0):
        self.x = x
        self.y = y
        self.playerHealth = playerHealth
        self.facingAngle = facingAngle
        self.player = self.Player(x, y, playerHealth, facingAngle)
