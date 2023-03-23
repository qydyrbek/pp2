import pygame 

pygame.init()

screen = pygame.display.set_mode((750,750))

clock = pygame.time.Clock()

c_x = 350
c_y = 350 
c_speed = 25

while True:
    screen.fill("white")
    pygame.draw.circle(screen, "red", (c_x,c_y), 25)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and c_x > 25 :
        c_x -= c_speed
    elif keys[pygame.K_RIGHT] and c_x < 725:
        c_x += c_speed

    if keys[pygame.K_UP] and c_y > 25 :
        c_y -= c_speed
    elif keys[pygame.K_DOWN] and c_y < 725:
        c_y += c_speed

    clock.tick(20)

    pygame.display.update()