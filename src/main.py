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
        self.angle = PI/4
        self.y_velocity = 0
        self.x_velocity = 0
        self.max_vel = 5

    def update(self):
        keys = pygame.key.get_pressed()
        self.move(keys)
        self.rotate(keys)

    def move(self, keys):
        # vertical movement
        if keys[K_w]:
            self.y_velocity += 0.35
        elif keys[K_s]:
            self.y_velocity -= 0.35
        else:
            self.y_velocity *= 0.75
        # limit y velocity
        if self.y_velocity > self.max_vel:
            self.y_velocity = self.max_vel
        elif self.y_velocity < -self.max_vel:
            self.y_velocity = -self.max_vel
        # horizontal movement
        if keys[K_a]:
            self.x_velocity += 0.35
        elif keys[K_d]:
            self.x_velocity -= 0.35
        else:
            self.x_velocity *= 0.75
        # limit x velocity
        if self.x_velocity > self.max_vel:
            self.x_velocity = self.max_vel
        elif self.x_velocity < -self.max_vel:
            self.x_velocity = -self.max_vel
        self.y -= self.y_velocity
        self.x -= self.x_velocity

    def rotate(self, keys):
        if keys[K_LEFT]:
            self.angle -= 0.1
        elif keys[K_RIGHT]:
            self.angle += 0.1

# global stuff here
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
PI = math.pi
player = Player()
        
def draw():
    # fill window with the darkness
    WINDOW.fill((0,0,0))
    pygame.draw.line(WINDOW, (255,0,0), (int(player.x-10*math.sin(player.angle + PI/2)), int(player.y-10*math.sin(player.angle))), (int(player.x+10*math.sin(player.angle + PI/2)), int(player.y+10*math.sin(player.angle))))
    pygame.display.flip() 

def main():
    
    clock = pygame.time.Clock()
    play = True

    # main game loop
    while play:
        clock.tick(60)
        pygame.display.set_caption(str(int(clock.get_fps()))) # keep track of fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player.update()
        draw()

main()
