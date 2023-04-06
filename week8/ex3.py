import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Drawing Shapes")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

draw_color = BLACK
draw_size = 1

def draw_shape(mouse_pos, click, shape):
    if click[0] == 1:
        if shape == "rect":
            pygame.draw.rect(window, draw_color, (mouse_pos[0], mouse_pos[1], 50, 50), draw_size)
        elif shape == "circle":
            pygame.draw.circle(window, draw_color, mouse_pos, 25, draw_size)
        elif shape == "eraser":
            pygame.draw.rect(window, BLACK, (mouse_pos[0], mouse_pos[1], 20, 20), draw_size)


# Initialize the shape variable to None
shape = None

# Set the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Check for key presses
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Check for color selection
            if event.key == K_r:
                draw_color = RED
            elif event.key == K_g:
                draw_color = GREEN
            elif event.key == K_b:
                draw_color = BLUE
            elif event.key == K_y:
                draw_color = YELLOW
            elif event.key == K_w:
                draw_color = WHITE
            elif event.key == K_k:
                draw_color = BLACK

            # Check for shape selection
            if event.key == K_1:
                shape = "rect"
            elif event.key == K_2:
                shape = "circle"
            elif event.key == K_3:
                shape = "eraser"

            # Check for size selection
            if event.key == K_4:
                draw_size = 1
            elif event.key == K_5:
                draw_size = 5
            elif event.key == K_6:
                draw_size = 10

        # Check for mouse button presses
        if event.type == MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                draw_shape(pygame.mouse.get_pos(), click, shape)

        # Check for mouse motion
        if event.type == MOUSEMOTION:
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                draw_shape(pygame.mouse.get_pos(), click, shape)

    # Update the display
    pygame.display.update()
