import socket
import pygame
import Member
from World import World
from Game import player
from Init import (
    x, y, health
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
    w = World(0, 0)
    w.Generate(0, 0)
    
    del (
        x, y, health, game
    )
        
    Loop(True)
