import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    # 1. Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    # 2. Update
    

    # 3. Draw
    pygame.draw.rect()

    # 4. Display
    pygame.display.flip()

pygame.quit()