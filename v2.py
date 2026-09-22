from mazegenerator import MazeGenerator
import inspect
import pygame

maze = MazeGenerator((30, 30), False)

maze_matrix = maze.maze



pygame.init()
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
s_w = screen.get_width()
s_h = screen.get_height()

lvl1_w = 30 * 20
lvl1_h = 30 * 20

offset_x = (s_w - lvl1_w) // 2
offset_y = (s_h - lvl1_h) // 2
# print(s_w, s_h)

pacgum_grid = []
for yy in range(30):
    row = []
    for xx in range(30):
        if not maze_matrix[yy][xx] in (15, 42):
            row.append(1)
        else:
            row.append(0)
    pacgum_grid.append(row)

while running:


    screen.fill('black')
    

    for yy in range(30):
        for xx in range(30):
            cell = maze_matrix[yy][xx]

            x = offset_x +(xx * 20)
            y = offset_y + (yy * 20)

            if cell & 1:
                pygame.draw.rect(screen, 'blue', (x, y, 20, 2))
            if cell & 2:
                pygame.draw.rect(screen, 'blue', (x + 20 - 2, y, 2, 20))
            if cell & 4:
                pygame.draw.rect(screen, 'blue', (x, y + 20 - 2, 20, 2))
            if cell & 8:
                pygame.draw.rect(screen, 'blue', (x, y, 2, 20))

            if pacgum_grid[yy][xx] == 1:
                center_x = x + 10
                center_y = y + 10
                pygame.draw.circle(screen, 'red', (center_x,center_y), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


# functions = inspect.getmembers(maze, inspect.ismethod)

# for name, fnc in functions:
#     print(name)