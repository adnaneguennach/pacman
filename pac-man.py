import sys
from mazegenerator import MazeGenerator   
import json
import pygame
from enum import Enum

class GameState(Enum):
    MAIN_MENU = 1
    CREDITS = 2
    SETTINGS = 3
    HIGHSCORES = 4
    
    PLAYING = 5
    PAUSE = 6
    GAME_OVER = 7
    VICTORY = 8

freeze = False
invisible = False
speed = False

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

TILE_SIZE = 25

pacgum_grid = []
for y in range(lvl1_height):
    row = []
    for x in range(lvl1_width):
        if m_grid[y][x] == 15:
            row.append(0)
        else:
            row.append(1)
    pacgum_grid.append(row)

def main() -> None:
    config_file = sys.argv[1]
    game_config = load_config(config_file)

    pygame.init()
    current_state = GameState.MAIN_MENU

    lvl1_width = game_config["levels"][0]["width"]
    lvl1_height = game_config["levels"][0]["height"]

    #kanjbdo list dyal l maze 
    maze_gen = MazeGenerator(size = (lvl1_width, lvl1_height), perfect = False)
    m_grid = maze_gen.maze

    print(m_grid)

    m_pixel_w = lvl1_width * TILE_SIZE  # 800
    m_pixel_h = lvl1_height * TILE_SIZE # 800

    running = True
    pygame.font.init()
    menu_font = pygame.font.Font("ByteBounce.ttf", 48)
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    menu_bg = pygame.image.load("credits.jpg").convert()
    menu_bg = pygame.transform.scale(menu_bg, (screen_width, screen_height))
    offset_x = (screen_width - m_pixel_w) // 2 # (1920 - 800) = 1120 / 2 = 560

    offset_y = (screen_height - m_pixel_h)  // 2  # (1080 - 800) = 780 / 2 = 390
    print(screen_height, screen_width)

    menu_options = ["PLAY", "CREDITS", "SETTINGS", "QUIT"]
    settings_options = ["INVISIBLITY","SPEED", "FREEZE", "BACK"]
    selected_index = 0
    cd = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_ESCAPE:
                    # running = False
                if current_state == GameState.MAIN_MENU:
                    if event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % len(menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_index == 0:
                            current_state = GameState.PLAYING
                        elif selected_index == 1:
                            current_state = GameState.CREDITS
                        elif selected_index == 2:
                            current_state = GameState.SETTINGS
                        elif selected_index == 3:
                            running = False
                    # elif event.key == pygame.K_ESCAPE:
                        # current
                
                elif current_state == GameState.SETTINGS:
                    if event.key == pygame.K_UP:
                        print(cd)
                        cd = (cd - 1) % len(settings_options)
                    elif event.key == pygame.K_DOWN:
                        cd = (cd + 1) % len(settings_options)
                    
                    elif event.key == pygame.K_RETURN:
                        if cd == 0:
                            global invisible
                            invisible = not invisible
                        elif cd == 1:
                            global speed
                            speed = not speed
                        elif cd == 2:
                            global freeze
                            freeze = not freeze
                            print(freeze, "check freeze")
                        elif cd == 3:
                            current_state = GameState.MAIN_MENU
                        

                        
                elif current_state in [GameState.PLAYING,GameState.CREDITS,GameState.SETTINGS] :
                    if event.key == pygame.K_ESCAPE:
                        current_state = GameState.MAIN_MENU
        
        if current_state == GameState.MAIN_MENU:
            screen.blit(menu_bg, (0, 0))
            title_surface = menu_font.render("PAC-MAN 42", True, (0, 255, 255))
            screen.blit(title_surface, (screen_width // 2 - 100, screen_height // 2 - 100))
            
            for index, option in enumerate(menu_options):
                if index == selected_index:
                    color = (255, 255, 0)
                else:
                    color = (255, 255, 255)
                    
                text_surface = menu_font.render(option, True, color)
                
                x_pos = screen_width // 2 - 70
                y_pos = (screen_height // 2 - 20) + (index * 50)
                
                screen.blit(text_surface, (x_pos, y_pos))
            

        if current_state == GameState.PLAYING:    
            screen.fill('black')
            #add a hug fnc
            for y in range(lvl1_height):
                for x in range(lvl1_width):
                    cell = m_grid[y][x] # 9 
                    px = offset_x + (x * TILE_SIZE) # 560 + (0 * 20) # 50
                    py = offset_y + (y * TILE_SIZE) # 50

                    if cell & 1: #north #yes
                        pygame.draw.rect(screen, 'blue', (px, py, TILE_SIZE, 2)) # (start_x , start_y, chehal fiha mn px, width dyalha)
                    if cell & 2: # east
                        pygame.draw.rect(screen, 'blue', (px + TILE_SIZE - 5 , py, 5, TILE_SIZE)) 
                        # (18, )
                    if cell & 4: # south
                        pygame.draw.rect(screen, 'blue', (px, py + TILE_SIZE - 2, TILE_SIZE, 2))
                    if cell & 8: # west
                        pygame.draw.rect(screen, 'blue', (px, py, 2, TILE_SIZE))
                    
                    center_x = px + (TILE_SIZE // 2)
                    center_y = py + (TILE_SIZE // 2)
            

        if current_state == GameState.SETTINGS:
            screen.blit(menu_bg, (0,0))
            title_surface = menu_font.render("SETTINGS", True, 'blue')
            screen.blit(title_surface, (screen_width // 2 - 100, screen_height // 2 - 100))

            for index, option in enumerate(settings_options):
                if index == cd:
                    color = 'yellow'
                else:
                    color = 'white'

                text_sur = menu_font.render(option, True, color)
                x_pos = screen_width // 2 - 70
                y_pos = (screen_height // 2 - 20) + (index * 50)

                screen.blit(text_sur, (x_pos, y_pos))
            


        if current_state == GameState.CREDITS:
            screen.fill('black')
            title_surface = menu_font.render("42 PAC-MAN", True, (0, 255, 255))
            screen.blit(title_surface, (screen_width // 2 - 100, screen_height // 2 - 150))


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

