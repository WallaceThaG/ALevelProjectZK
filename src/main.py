'''
ZHANDOS' PROGRAMMING PROJECT

Snake casing for variables and functions.
Pascal casing for class names (e.g. ClassName)
ALL-CAPS indicates a constant.
'''

# start by importing some useful things

import os
import sys
import math
import pygame
from pygame.locals import *

class Player:
    # constructor method for the player
    def __init__(self):
        # for now just initialise player position to the centre of the screen
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.angle = math.pi # important reminder here
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.y_velocity += 0.25
        elif keys[K_s]:
            self.y_velocity -= 0.25
        else:
            self.y_velocity *= 0.9
            
        if keys[K_a]:
            self.x_velocity += 0.25
        elif keys[K_d]:
            self.x_velocity -= 0.25
        else:
            self.x_velocity *= 0.9
        self.y -= self.y_velocity
        self.x -= self.x_velocity

# global stuff here
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player()
        
def draw():
    # fill window with the darkness
    WINDOW.fill((0,0,0))
    pygame.draw.rect(WINDOW, (255,0,0), [player.x-5, player.y-5, 10, 10])
    pygame.display.flip() 

def main():
    
    clock = pygame.time.Clock()
    play = True

    # main game loop
    while play:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player.update()
        draw()

main()