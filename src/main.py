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

def grid(WINDOW):
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
            
        
def draw(WINDOW):
    # fill window with the darkness
    WINDOW.fill((0,0,0))
    grid(WINDOW)
    pygame.display.update() 

def main():
    # Globalise constants
    global WIDTH, HEIGHT
    WIDTH = 800
    HEIGHT = 600
    # 4:3 aspect ratio for the vibes
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    play = True

    # main game loop
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # function for drawing grid lines
        draw(WINDOW)

main()
