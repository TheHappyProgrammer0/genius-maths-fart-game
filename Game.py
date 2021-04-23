from Init import (
    init
)              
from Move import (
    move
)      

class Game:
    def setUp(self):
        init.Display()
        init.Vars(0, 0)
        
game = Game()  