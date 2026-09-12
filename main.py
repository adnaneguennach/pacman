import pygame
import pygame.gfxdraw
import math 

# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True



# player = pygame.Rect(100, 100, 50, 50)

# while running:

#     # Events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Update
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         # if moves outside the windows box then we dont move so we tighten our movements to follow a certain rule, either is a wall or the end of the screen 
#         player = player.move(-1, 0)

#     if keys[pygame.K_RIGHT]:
#         player = player.move(1, 0)
#     if keys[pygame.K_UP]:
#         player = player.move(0, -1)
#     if keys[pygame.K_DOWN]:
#         player = player.move(0, 1)
#     # Draw
#     screen.fill((0, 0, 0))
#     cx, cy = 500, 500
#     radius = 20

#     points = [(cx, cy)]

#     for angle in range(20, 321):
#         rad = math.radians(angle)
#         x = cx + radius * math.cos(rad)
#         y = cy + radius * math.sin(rad)
#         points.append((x, y))

#     pygame.draw.polygon(screen, (255, 0, 0), points)

#     # Display
#     pygame.display.flip()

# pygame.quit()



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# player = pygame.Rect()

while running:

    cx, cy = 200, 200
    radius = 20

    points = [(cx, cy)]
    for angle in range(20, 326):
        ra = math.radians(angle)
        x = cx + radius * math.cos(ra)
        y = cy + radius * math.sin(ra)
        points.append((x, y))

    

    pygame.draw.polygon(screen, (255, 255, 0), points)

    pygame.display.flip()
