from pygame import *
from characters import *
import time


pygame.init()

# tempo de ação do jogo
clock = pygame.time.Clock()
FPS = 60

# titulo do jogo
pygame.display.set_caption("Introbattle: Terraria project")

# tamanhos da janela do jogo
WIDTH, HEIGHT = 1024, 728
START = (0, 0)
MID = (WIDTH/2, HEIGHT/2)
SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)

# definindo imagens do jogo e ajustando seu tamanho
BACKGROUND = pygame.image.load(os.path.join('imgs', "fundo.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, SIZE)

BACKGROUND_INGAME = pygame.image.load(os.path.join('imgs', 'corruption_desert_day.png'))
BACKGROUND_INGAME = pygame.transform.scale(BACKGROUND_INGAME, SIZE)

START_BACKGROUND = pygame.image.load(os.path.join('imgs', 'start_screen.png'))

INTROBATTLE = pygame.image.load(os.path.join('imgs', 'introbattle.png'))
INTROBATTLE = pygame.transform.scale_by(INTROBATTLE, 2)
INTROBATTLE_RECT = INTROBATTLE.get_rect()
INTROBATTLE_RECT.center = (WIDTH/2, 100)

SELECTION_BANNER = pygame.image.load(os.path.join('imgs', 'red_banner.png'))
SELECTION_BANNER = pygame.transform.scale_by(SELECTION_BANNER, 6)
SELECTION_BANNER_RECT = SELECTION_BANNER.get_rect()

SETA = pygame.image.load(os.path.join('imgs', 'arrow_pointer.png'))
SETA = pygame.transform.rotate(SETA, 136)
SETA = pygame.transform.scale_by(SETA, 0.35)
SETA_RECT = SETA.get_rect()

MENU = pygame.image.load(os.path.join('imgs', 'menu.png'))
MENU_RECT = MENU.get_rect()


def draw_start_screen(screen: pygame.surface):
    font = pygame.font.Font(None, 40)
    text = font.render("Let's get start!", True, pygame.Color("YELLOW"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    
    screen.blit(START_BACKGROUND, START)
    screen.blit(INTROBATTLE, INTROBATTLE_RECT)
    screen.blit(text, text_rect)
    update_screen()
    
    time.sleep(1)


def draw_character_selection(screen: pygame.surface, character_list: list):
    selected_characters = list()
    x, y = 70, 260

    banner_positions = list()

    run = True
    while run:
        time.sleep(0.25)
        screen.blit(BACKGROUND, START)

        # imprime os banners ativos
        for banner in banner_positions:
            screen.blit(SELECTION_BANNER, banner)

        # imprime os personagens
        draw_character_list(screen, character_list)

        # imprime a seta
        screen.blit(SETA, (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            # movimento da seta
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and x+150 <= 800:
                    x += 150
                    
                elif event.key == pygame.K_LEFT and x-150 >= 70: 
                    x -= 150

                elif event.key == pygame.K_RETURN and len(selected_characters) >= 1:
                    return selected_characters

                elif event.key == pygame.K_z and len(selected_characters) < 3:
                    if x == 70:
                        if character_list[0] in selected_characters:
                            selected_characters.remove(character_list[0])
                            banner_positions.remove([100, 400])
                            
                        else:
                            selected_characters.append(character_list[0])
                            banner_positions.append([100, 400])
                        
                    elif x == 220:
                        if character_list[1] in selected_characters:
                            selected_characters.remove(character_list[1])
                            banner_positions.remove([250, 400])

                        else:
                            selected_characters.append(character_list[1])
                            banner_positions.append([250, 400])
                        
                    elif x == 370:
                        if character_list[2] in selected_characters:
                            selected_characters.remove(character_list[2])
                            banner_positions.remove([400, 400])

                        else:
                            selected_characters.append(character_list[2])
                            banner_positions.append([400, 400])
                        
                    elif x == 520:
                        if character_list[3] in selected_characters:
                            selected_characters.remove(character_list[3])
                            banner_positions.remove([550, 400])

                        else:
                            selected_characters.append(character_list[3])
                            banner_positions.append([550, 400])
                        
                    elif x == 670:
                        if character_list[4] in selected_characters:
                            selected_characters.remove(character_list[4])
                            banner_positions.append([700, 400])

                        else:
                            selected_characters.append(character_list[4])
                            banner_positions.append([700, 400])

        update_screen()
        
    return selected_characters


def draw_screen(screen: pygame.surface, character_list: list, enemy_list: list) -> None:
    screen.blit(BACKGROUND_INGAME, START)
    draw_character_list(screen, character_list)
    draw_enemy_list(screen, enemy_list)


def draw_menu(screen: pygame.surface, character_list: list[Character]) -> None:
    screen.blit(MENU, MENU_RECT)


def update_screen() -> None:
    clock.tick(FPS)  # Definir a taxa de quadros
    pygame.display.flip()  # Atualizar a exibição


def draw_character_list(screen: pygame.surface, character_list: list[Character]) -> None:
    x = 100
    for character in character_list:
        character.draw_character_position(screen, [x, 420])
        x += 150


def draw_enemy_list(screen: pygame.surface, enemy_list: list[Character]) -> None:
    x, y = WIDTH-250, 270
    for enemies in enemy_list:
        enemies.draw_character_position(screen, [x, y])
        x -= 250
        y -= 180
