# Conway's Game of Life
# ShockingRotom July 2021

# Draw with LMB
# Erase with RMB
# Fill with 'f'
# Clear with 'c'
# Randomize matrix with 'r'
# Create a glider with '1'
# Pause and unpause with SPACE

import pygame
import numpy as np
from extra import Algorithm

pygame.init()

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# IMPORTANT VARS
# while True:
    # user = int(input("Select the dimension of matrix between 1 and 700: "))
    # if 1 <= user <= 700:
        # COUNT = user
        # break

COUNT = 100
SIZE = int(800 / COUNT)

size = (SIZE * COUNT, SIZE * COUNT)
screen = pygame.display.set_mode(size, 0, 32)

screen.fill(WHITE)

pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

# Functions
# Creates a matrix of the board
def create_matrix(x):
    matrix = np.zeros((x, x))
    return matrix


# Creates glider
def glider1(matrix, SIZE):
    pos = pygame.mouse.get_pos()
    c = int(pos[1] / SIZE)
    r = int(pos[0] / SIZE)
    try:
        matrix[c-1][r-1] = 1
        matrix[c-1][r] = 1
        matrix[c][r] = 1
        matrix[c][r+1] = 1
        matrix[c+1][r-1] = 1
    except:
        pass

    return matrix


# Draws matrix
def draw_matrix(screen, x, SIZE, matrix):
    for c in range(x):
        for r in range(x):
            if matrix[c][r] == 0:
                colour = WHITE
            else:
                colour = BLACK
            pygame.draw.rect(screen, colour, (r * SIZE, c * SIZE, SIZE, SIZE))


# Draws highlight
def draw_highlight(screen, SIZE):
    c = int(pygame.mouse.get_pos()[0] / SIZE)
    r = int(pygame.mouse.get_pos()[1] / SIZE)
    pos = (c * SIZE, r * SIZE)
    select = pygame.Surface((SIZE, SIZE))
    # Makes square semi transparent
    select.set_alpha(128)
    select.fill(GREEN)
    screen.blit(select, pos)

matrix = create_matrix(COUNT)
draw_matrix(screen, COUNT, SIZE, matrix)
pygame.display.flip()

running = True
paused = True
drawing = False
erasing = False

print("")
print("WELCOME TO CONWAY'S GAME OF LIFE")
print("")
print("Draw with LMB")
print("Erase with RMB")
print("Fill with 'f'")
print("Clear with 'c'")
print("Randomize matrix with 'r'")
print("Create a glider with '1'")
print("Pause and unpause with SPACE")

while running:
    # User Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                paused = True

    while paused:
        # User Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    running = False
                elif event.key == pygame.K_r:
                    matrix = Algorithm.randomizer(COUNT, matrix)
                elif event.key == pygame.K_c:
                    matrix = create_matrix(COUNT)
                elif event.key == pygame.K_f:
                    pos = pygame.mouse.get_pos()
                    old = matrix[int(pos[1] / SIZE)][int(pos[0] / SIZE)]
                    if old == 0:
                        new = 1
                    else:
                        new = 0
                    Algorithm.flood_fill(int(pos[1] / SIZE), int(pos[0] / SIZE), old, new, matrix, COUNT)
                elif event.key == pygame.K_1:
                    matrix = glider1(matrix, SIZE)
                elif event.key == pygame.K_SPACE:
                    paused = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == 1:
                    drawing = True
                if pygame.mouse.get_pressed()[2] == 1:
                    erasing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed()[0] == 0:
                    drawing = False
                if pygame.mouse.get_pressed()[2] == 0:
                    erasing = False

        if drawing:
            matrix[int(pygame.mouse.get_pos()[1] / SIZE)][int(pygame.mouse.get_pos()[0] / SIZE)] = 1

        if erasing:
            matrix[int(pygame.mouse.get_pos()[1] / SIZE)][int(pygame.mouse.get_pos()[0] / SIZE)] = 0

        draw_matrix(screen, COUNT, SIZE, matrix)
        draw_highlight(screen, SIZE)

        pygame.display.flip()

    matrix = Algorithm.life(COUNT, matrix)

    draw_matrix(screen, COUNT, SIZE, matrix)

    pygame.display.flip()

    clock.tick(10)
