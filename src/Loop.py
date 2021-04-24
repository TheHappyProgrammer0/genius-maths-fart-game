import pygame
import Member
from Init import (
    init, screen
)
from Game import game
import socket

def Loop(in_game):
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if keys_pressed == pygame.K_UP:
                    move.Up()
                    
if __name__ == "__main__":
    game.setUp()
    keys_pressed = pygame.key.get_pressed()
    Loop(True)
