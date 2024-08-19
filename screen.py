from pygame import *
from characters import *
from points import PointSys
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

WIN_SCREEN = pygame.image.load(os.path.join('imgs', 'forest_sky.png'))
WIN_SCREEN = pygame.transform.scale(WIN_SCREEN, SIZE)

LOST_SCREEN = pygame.image.load(os.path.join('imgs', 'corruption_desert_night.png'))
LOST_SCREEN = pygame.transform.scale(LOST_SCREEN, SIZE)

START_BACKGROUND = pygame.image.load(os.path.join('imgs', 'start_screen.png'))

INTROBATTLE = pygame.image.load(os.path.join('imgs', 'introbattle.png'))
INTROBATTLE = pygame.transform.scale_by(INTROBATTLE, 2)
INTROBATTLE_RECT = INTROBATTLE.get_rect()
INTROBATTLE_RECT.center = (WIDTH/2, 100)

SELECTION_BANNER = pygame.image.load(os.path.join('imgs', 'red_banner.png'))
SELECTION_BANNER = pygame.transform.scale_by(SELECTION_BANNER, 6)

SETA = pygame.image.load(os.path.join('imgs', 'arrow_pointer.png'))
SETA = pygame.transform.rotate(SETA, 136)
SETA = pygame.transform.scale_by(SETA, 0.35)

MENU = pygame.image.load(os.path.join('imgs', 'menu.png'))
MENU_RECT = MENU.get_rect()

FONT = pygame.font.Font(None, 40)
SELECT_TEXT = FONT.render(">", True, pygame.Color("YELLOW"))
ATTACK_TEXT = FONT.render("Attack", True, pygame.Color("YELLOW"))
DEFENSE_TEXT = FONT.render("Defense", True, pygame.Color("YELLOW"))
SPECIAL_TEXT = FONT.render("Special", True, pygame.Color("YELLOW"))

def select_sound():
    sound_bg = pygame.mixer.Sound('assets/select.mp3')
    sound_bg.set_volume(0.1)
    sound_bg.play()

def draw_start_screen(screen: pygame.surface):
    font = pygame.font.Font('assets/Andy.ttf', 30)
    text = font.render("PRESS ANY KEY TO GET START!", True, pygame.Color("yellow"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    
    
    screen.blit(START_BACKGROUND, START)
    screen.blit(INTROBATTLE, INTROBATTLE_RECT)
    screen.blit(text, text_rect)
    update_screen()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                select_sound()
                run = False


def draw_character_selection(screen: pygame.surface, character_list: list):
    font = pygame.font.Font('assets/Andy.ttf', 30)
    text = font.render("PRESS <, > or ENTER TO SELECT", True, pygame.Color("yellow"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    
    selected_characters = list()
    banner_positions = list()
    x, y = 117, 260

    run = True
    while run:
        screen.blit(BACKGROUND, START)
        screen.blit(text, text_rect)

        # imprime os banners ativos
        for banner in banner_positions:
            screen.blit(SELECTION_BANNER, banner)

        # imprime os personagens
        draw_character_list(screen, character_list)

        # imprime a seta
        screen.blit(SETA, [x, y])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            # movimento da seta
            elif event.type == pygame.KEYDOWN:
                select_sound()
                
                if event.key == pygame.K_RIGHT and x+150 <= 800:
                    x += 150
                    
                elif event.key == pygame.K_LEFT and x-150 >= 70: 
                    x -= 150

                elif event.key == pygame.K_RETURN and len(selected_characters) >= 1:
                    return selected_characters

                elif event.key == pygame.K_z and len(selected_characters) <= 3:
                    if x == 117:
                        if character_list[0] in selected_characters:
                            selected_characters.remove(character_list[0])
                            banner_positions.remove([150, 400])
                            
                        else:
                            if len(selected_characters) < 3:
                                selected_characters.append(character_list[0])
                                banner_positions.append([150, 400])
                        
                    elif x == 117+150:
                        if character_list[1] in selected_characters:
                            selected_characters.remove(character_list[1])
                            banner_positions.remove([300, 400])

                        else:
                            if len(selected_characters) < 3:
                                selected_characters.append(character_list[1])
                                banner_positions.append([300, 400])
                        
                    elif x == 117 + 2*150:
                        if character_list[2] in selected_characters:
                            selected_characters.remove(character_list[2])
                            banner_positions.remove([450, 400])

                        else:
                            if len(selected_characters) < 3:
                                selected_characters.append(character_list[2])
                                banner_positions.append([450, 400])
                        
                    elif x == 117 + 3*150:
                        if character_list[3] in selected_characters:
                            selected_characters.remove(character_list[3])
                            banner_positions.remove([600, 400])

                        else:
                            if len(selected_characters) < 3:
                                selected_characters.append(character_list[3])
                                banner_positions.append([600, 400])
                        
                    elif x == 117 + 4*150:
                        if character_list[4] in selected_characters:
                            selected_characters.remove(character_list[4])
                            banner_positions.append([750, 400])

                        else:
                            if len(selected_characters) < 3:
                                selected_characters.append(character_list[4])
                                banner_positions.append([750, 400])

        update_screen()
        
    return selected_characters


def draw_screen(screen: pygame.surface, character_list: list, enemy_list: list) -> None:
    screen.blit(BACKGROUND_INGAME, START)
    draw_character_list(screen, character_list)
    draw_enemy_list(screen, enemy_list)

def update_screen() -> None:
    clock.tick(FPS)  # Definir a taxa de quadros
    pygame.display.flip()  # Atualizar a exibição


def draw_character_list(screen: pygame.surface, character_list: list[Character]) -> None:
    x, y = 150, 420
    for character in character_list:
        if character.get_character_life_points() > 0:
            character.draw_character_position(screen, [x, y])
            character.set_character_post([x, y])
            x += 150


def draw_enemy_list(screen: pygame.surface, enemy_list: list[Character]) -> None:
    x, y = WIDTH-250, 230

    duke_pos = [x, y]
    eye_pos = [x-250, y-250]

    if enemy_list[0].get_character_life_points() > 0:
        enemy_list[0].draw_character_position(screen, duke_pos)
        enemy_list[0].set_character_post(duke_pos)
        
    if enemy_list[1].get_character_life_points() > 0:
        enemy_list[1].draw_character_position(screen, eye_pos)
        enemy_list[1].set_character_post(eye_pos)
        
def draw_win_screen(screen: pygame.surface) -> None:
    screen.blit(WIN_SCREEN, START)
    
    font = pygame.font.Font(None, 40)
    text = font.render("Congrats! You've winned!", True, pygame.Color("YELLOW"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    screen.blit(text, text_rect)
    
    update_screen()
    time.sleep(1.5)
    pygame.quit()
    
def draw_lost_screen(screen: pygame.surface) -> None:
    screen.blit(LOST_SCREEN, START)
    
    font = pygame.font.Font(None, 40)
    text = font.render("You've lost!", True, pygame.Color("YELLOW"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    screen.blit(text, text_rect)
    
    update_screen()
    time.sleep(1.5)
    pygame.quit()

def draw_menu_options(screen: pygame.surface, character: Character, character_list: list[Character], enemy_list: list[Character], pontos: PointSys) -> None:
    screen.blit(MENU, MENU_RECT)
    screen.blit(ATTACK_TEXT, [100, HEIGHT-160])
    screen.blit(SPECIAL_TEXT, [300, HEIGHT-160])
    
    screen.blit(DEFENSE_TEXT, [100, HEIGHT-100])
    
    POINT_TEXT = FONT.render(f"Points: {pontos.get_points()}", True, pygame.Color("YELLOW"))
    screen.blit(POINT_TEXT, [300, HEIGHT-100])
    
    y = 150
    font = pygame.font.Font(None, 30)
    
    # mostra de quem eh o turno
    font_2 = pygame.font.Font(None, 25)
    text = font_2.render(f"It's {character.get_character_name()} turn!", True, pygame.Color("YELLOW"))
    screen.blit(text, [WIDTH-300, HEIGHT-190])
    
    # mostra a vida dos herois
    for char in character_list:
        text = font.render(f"{char.get_character_name()}: {char.get_character_life_points():.0f}/100", 
                           True, pygame.Color("YELLOW"))
        screen.blit(text, [WIDTH-300, HEIGHT-y])
        y -= 20
        
    # mostra a vida dos inimigos
    for enemy in enemy_list:
        text = font.render(f"{enemy.get_character_name()}: {enemy.get_character_life_points():.0f}/{enemy.get_character_max_life_points():.0f}", 
                           True, pygame.Color("YELLOW"))
        screen.blit(text, [WIDTH-300, HEIGHT-y])
        y -= 20

def draw_menu_interactions(screen: pygame.surface.Surface, character: Character, character_list: list, enemy_list: list, pos_txt: list[2], pontos: PointSys) -> None:
    draw_screen(SCREEN, character_list, enemy_list)
    pos_seta = [character.get_caracter_pos_x()-40, character.get_caracter_pos_y()-140]
    
    draw_menu_options(screen, character, character_list, enemy_list, pontos)
    screen.blit(SETA, pos_seta)
    screen.blit(SELECT_TEXT, pos_txt)