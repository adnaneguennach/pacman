import sys
from mazegenerator import MazeGenerator   
import json
import pygame


def load_config(path):
    clean_str  = ""
    try:
        with open(path, "r") as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line.startswith("#"):
                    continue
                clean_str += line
        lines = json.loads(clean_str)
        return lines
    except FileNotFoundError:   
        print(f"Error: Could not find configuration file '{path}'.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: The configuration file is not valid JSON.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

TILE_SIZE = 20
def main() -> None:
    config_file = sys.argv[1]
    game_config = load_config(config_file)

    pygame.init()
    lvl1_width = game_config["levels"][0]["width"]
    lvl1_height = game_config["levels"][0]["height"]

    #kanjbdo list dyal l maze 
    maze_gen = MazeGenerator(size = (lvl1_width, lvl1_height), perfect = False)
    m_grid = maze_gen.maze

    m_pixel_w = lvl1_width * TILE_SIZE 
    m_pixel_h = lvl1_height * TILE_SIZE




    running = True
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    offset_x = (screen_width - m_pixel_w) /2 
    offset_y = (screen_height - m_pixel_h)  /2 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.fill('black')
        for y in range(lvl1_height):
            for x in range(lvl1_width):
                cell = m_grid[y][x]
                px = offset_x + (x * TILE_SIZE)
                py = offset_y + (y * TILE_SIZE)

                if cell & 1: #north
                    pygame.draw.rect(screen, 'blue', (px, py, TILE_SIZE, 2))
                if cell & 2: # east
                    pygame.draw.rect(screen, 'blue', (px + TILE_SIZE - 2, py, 2, TILE_SIZE))
                if cell & 4: # south
                    pygame.draw.rect(screen, 'blue', (px, py + TILE_SIZE - 2, TILE_SIZE, 2))
                if cell & 8: # west
                    pygame.draw.rect(screen, 'blue', (px, py, 2, TILE_SIZE))


        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()








# maze_gen = MazeGenerator(size=(15, 15), perfect=False)
# my_grid = maze_gen.maze

# pygame.init()
# screen = pygame.display.set_mode((720,720))
# clock = pygame.time.Clock()
# running = True

# while running:
#     screen.fill('black')
#     pygame.display.flip()
#     # maze.generate()
# pygame.quit()

