# Imports
import pygame, sys, random
from pygame.locals import *

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (51, 153, 255)
RED = (255, 51, 51)
GREEN = (51, 255, 51)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Thank You!", True, GREEN)

background = pygame.image.load("latar1.jpg")

# Background Music
music = pygame.mixer.music.load("bgmusic.mp3")
pygame.mixer.music.play(-1)

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(BLUE)
pygame.display.set_caption("METEOR AVOID")

pygame.display.update()