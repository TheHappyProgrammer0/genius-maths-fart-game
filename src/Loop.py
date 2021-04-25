import socket
import pygame
import Member
from Game import game
from World import World
from Init import (
    WIDTH, HEIGHT, x, y, health
)

def Loop(in_game):
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    in_game = False
                    pygame.quit()
                
                elif event.key == pygame.K_UP:
                    player.Move("up")
                    
                elif event.key == pygame.K_LEFT:
                    player.Move("left")
                    
                elif event.key == pygame.K_RIGHT:
                    player.Move("right")
                

if __name__ == "__main__":  
    player = game.Player(x, y, health)
    w = World(0, 0)
    w.Generate(0, 0)
    
    Loop(True)
