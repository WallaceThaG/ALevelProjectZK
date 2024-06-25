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
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.angle = PI/2
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
            self.x_velocity -= 0.3*math.cos(player.angle)
            self.y_velocity -= 0.3*math.sin(player.angle)
        elif keys[K_s]:
            self.x_velocity += 0.3*math.cos(player.angle)
            self.y_velocity += 0.3*math.sin(player.angle)
        # deceleration
        elif not(keys[K_a] or keys[K_d]):
            self.x_velocity *= 0.95
            self.y_velocity *= 0.95
        # horizontal movement
        if keys[K_a]:
            self.x_velocity -= 0.3*math.sin(player.angle)
            self.y_velocity += 0.3*math.cos(player.angle)
        elif keys[K_d]:
            self.x_velocity += 0.3*math.sin(player.angle)
            self.y_velocity -= 0.3*math.cos(player.angle)
        # deceleration
        elif not(keys[K_w] or keys[K_s]):
            self.x_velocity *= 0.95
            self.y_velocity *= 0.95
        
        # limit velocity
        self.x_velocity *= 0.96
        self.y_velocity *= 0.96
        # update coordinates
        self.y -= self.y_velocity
        self.x -= self.x_velocity

    def rotate(self, keys):
        # decrease player angle when left key is pressed
        # increase when right key is pressed
        if keys[K_LEFT]:
            self.angle -= 0.1
            # the player's angle must always be between 0 and 2*pi radians
            if self.angle < 0:
                self.angle += 2*PI
        elif keys[K_RIGHT]:
            self.angle += 0.1
            if self.angle > 2*PI:
                self.angle -= 2*PI

    def draw(self):
        line_start = (int(self.x), int(self.y))
        line_end = (int(self.x+15*math.cos(self.angle)), int(self.y+15*math.sin(self.angle)))
        pygame.draw.line(WINDOW, (255,0,0), line_start, line_end, 3)
        pygame.draw.circle(WINDOW, (255,0,0), (int(self.x), int(self.y)), 5)

def draw():
    # fill window with the darkness
    WINDOW.fill((0,0,0))
    draw_map()
    cast_rays()
    player.draw()
    pygame.display.flip()

def draw_map():
    for i in range(16):
        for j in range(16):
            if map_1[i][j] == "#":
                # draw cells
                pygame.draw.rect(WINDOW, (0,0,255), pygame.Rect(j*CELL_LENGTH, i*CELL_LENGTH, CELL_LENGTH, CELL_LENGTH))

def cast_rays():
    line_start = (int(player.x), int(player.y))
    line_end = (int(player.x+512*math.cos(player.angle)), int(player.y+512*math.sin(player.angle)))
    pygame.draw.line(WINDOW, (255, 255, 255), line_start, line_end)

# global stuff here
WIDTH = 1024
HEIGHT = 768
CELL_LENGTH = HEIGHT/16
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
PI = math.pi
player = Player()
# maps are 16x16 squares with square cells
map_1 = [  "################",
           "#     #        #",
           "#     #        #",
           "#   ########   #",
           "#              #",
           "#              #",
           "#              #",
           "#######    #####",
           "#     #        #",
           "#     #        #",
           "#     #        #",
           "#     #        #",
           "#              #",
           "#              #",
           "#              #",
           "################",  ]

def main():

    global player

    pygame.init()
    
    clock = pygame.time.Clock()
    running = True

    # main game loop
    while running:
        clock.tick(60) # targeting 60 fps
        pygame.display.set_caption(str(int(clock.get_fps()))) # keep track of fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        # update attributes and draw to the screen
        player.update()
        draw()

main()
