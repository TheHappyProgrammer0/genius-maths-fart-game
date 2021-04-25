from Init import player

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
