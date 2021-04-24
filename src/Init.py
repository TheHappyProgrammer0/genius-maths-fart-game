import pygame

WIDTH = 900
HEIGHT = 1200

screen = pygame.display

x = 0
y = 0

heath = 0

class Init:
  
  global x
  global y
  global health
  
  def Display(self):
    display = screen.set_mode((WIDTH, HEIGHT))
    screen.set_caption("Genius Maths Farts Game") 
    screen.flip()                          
                              
  def Vars(self, x=0, y=0):
    health = 100
    x = 0
    y = 0                         
                            
init = Init()
