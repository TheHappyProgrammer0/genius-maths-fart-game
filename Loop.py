import pygame
import Member
import People
from Init import init
from Game import game
import socket

game.setUp()

def Loop():
    global in_game

    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move.Up()
                    
if __name__ == "main":
    Loop()