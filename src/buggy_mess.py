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
        self.angle = math.pi # important reminder here
        self.position = pygame.math.Vector2(WIDTH/2,HEIGHT/2)
        self.velocity = pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,0)
        self.friction = -0.15

    def update(self,dt):
        self.move(dt)

    def move(self,dt):
        keys = pygame.key.get_pressed()
        # vertical movement
        self.acceleration.y = 0
        if keys[K_w]:
            self.acceleration.y += 0.2
        elif keys[K_s]:
            self.acceleration.y += 0.2
        self.acceleration.y -= self.velocity.y * self.friction
        self.velocity.y -= self.acceleration.y * dt
        self.position.y += self.velocity.y * dt + (0.5 * self.acceleration.y) * (dt * dt)
        # horizontal movement
        if keys[K_a]:
            self.acceleration.x += 0.2
        elif keys[K_d]:
            self.acceleration.x -= 0.2
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x -= self.acceleration.x * dt
        self.position.x += self.velocity.x * dt + (0.5 * self.acceleration.x) * (dt * dt)


# global stuff here
WIDTH  = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TARGET_FPS = 60
player = Player()
        
def draw():
    # fill window with the darkness
    WINDOW.fill((0,0,0))
    pygame.draw.rect(WINDOW, (255,0,0), [int(player.position.x-5), int(player.position.y-5), 10, 10])
    #pygame.draw.line(WINDOW, (255,0,0), ()) i want to draw the player as an arrow so their direction is clear
    pygame.display.flip() 

def main():
    
    clock = pygame.time.Clock()
    running = True

    # main game loop
    while running:
        dt = clock.tick(60)*0.001*TARGET_FPS
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        player.update(dt)
        draw()

main()
