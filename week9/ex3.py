import pygame
import math
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
            pygame.draw.rect(window, draw_color, (mouse_pos[0], mouse_pos[1], 50, 20), draw_size)
        elif shape == "circle":
            pygame.draw.circle(window, draw_color, mouse_pos, 25, draw_size)
        elif shape == "square":
            pygame.draw.rect(window, draw_color, (mouse_pos[0], mouse_pos[1], 50, 50), draw_size)
        elif shape == "rtriangle":
            pygame.draw.polygon(window, draw_color, ((mouse_pos[0], mouse_pos[1]), (mouse_pos[0], mouse_pos[1]+50), (mouse_pos[0]+50, mouse_pos[1])))
        elif shape == "rhombus":
            size = 50
            x,y = pygame.mouse.get_pos()
            top_left = (x - size, y)
            top_right = (x, y - size)
            bottom_left = (x, y + size)
            bottom_right = (x + size, y)
            pygame.draw.polygon(window, draw_color, [top_left, top_right, bottom_right, bottom_left])
        elif shape == "etriangle":
            side_length = 50
            center_x, center_y = pygame.mouse.get_pos()
            vertex1 = (center_x, center_y - side_length)
            vertex2 = (center_x - side_length * math.sin(math.pi / 3), center_y + side_length * math.cos(math.pi / 3))
            vertex3 = (center_x + side_length * math.sin(math.pi / 3), center_y + side_length * math.cos(math.pi / 3))
            pygame.draw.polygon(window, draw_color, [vertex1, vertex2, vertex3])            
        elif shape == "eraser":
            pygame.draw.rect(window, BLACK, (mouse_pos[0], mouse_pos[1], 40, 40), draw_size)


# Initialize the shape variable to None
shape = None

# Set the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # Check for key presses
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

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
                shape = "square"
            elif event.key == K_4:
                shape = "rtriangle"
            elif event.key == K_5:
                shape = "etriangle"
            elif event.key == K_6:
                shape = "rhombus"
            elif event.key == K_7:
                shape = "eraser"
            

            # Check for size selection
            if event.key == K_8:
                draw_size = 1
            elif event.key == K_9:
                draw_size = 10
            elif event.key == K_0:
                draw_size = 15

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
