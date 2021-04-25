# from Init import player

def Up(player, x, y):
    y += 1
    player.checkCollision(x, y)
    return y

def Left(player):
    global x
    x -= 1
    player.checkCollision(x, y)

def Right(player):
    global x
    x += 1
    player.checkCollision(x, y)
