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

class Player:
    # constructor method for the player
    def __init__(self):
        # for now just initialise player position to the centre of the screen
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.angle = math.pi

    def update(self, keys):
        if keys[pygame.K_w]:
            player.y -= 10
        
'''
def grid():
    line_dist = 40
    # using DIV here to get the number of vertical and horizontal lines
    x_lines = WIDTH//line_dist
    y_lines = HEIGHT//line_dist
    x = 0
    y = 0
    # following for loops draw lines to the screen using some parameters
    # namely the colour of the line and two points between which the line is drawn
    for line in range(x_lines):
        x += line_dist
        pygame.draw.line(WINDOW, (255,255,255), (x, 0), (x, HEIGHT))
    for line in range(y_lines):
        y += line_dist
        pygame.draw.line(WINDOW, (255,255,255), (0, y), (WIDTH, y))
'''            

# global stuff here
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player()
        
def draw():
    # fill window with the darkness
    WINDOW.fill((0,0,0))
    '''grid()'''
    pygame.draw.rect(WINDOW, (255,0,0), [player.x-5, player.y-5, 10, 10])
    pygame.display.update() 

def main():
    pygame.init()
    play = True

    # main game loop
    while play:
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            player.update(pressed_keys)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw()

main()