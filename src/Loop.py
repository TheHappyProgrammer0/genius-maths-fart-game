import socket
import pygame
import Member
from Game import game
from Init import init, screen


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
                    player.move(up)
                    
if __name__ == "__main__":
    game.setUp()
    Loop(True)
