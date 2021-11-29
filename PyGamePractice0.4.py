# PyGame Practice, Ryan Kelley, 11/29/21 9:14am, v0.4

from _typeshed import ReadableBuffer
import pygame, sys
from pygame.locals import *

# start PyGame
pygame.init()

#Create game window
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Hello, World")

# Set Color Values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup Fonts
basicFont = pygame.font.SysFont(None, 48)

# Setup Text 
text = basicFont.render('Hello, world', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery