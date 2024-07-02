from characters import *
from screen import *

MENU = pygame.image.load(os.path.join('imgs', 'menu.png'))
MENU_RECT = MENU.get_rect()

FONT = pygame.font.Font(None, 40)
ATTACK_TEXT = FONT.render("Attack", True, pygame.Color("YELLOW"))
ATTACK_RECT = ATTACK_TEXT.get_rect()

DEFENSE_TEXT = FONT.render("Defense", True, pygame.Color("YELLOW"))
DEFENSE_RECT = DEFENSE_TEXT.get_rect()

SPECIAL_TEXT = FONT.render("Special", True, pygame.Color("YELLOW"))
SPECIAL_RECT = SPECIAL_TEXT.get_rect()

CHARM_TEXT = FONT.render("Charm", True, pygame.Color("YELLOW"))
CHARM_RECT = CHARM_TEXT.get_rect()

def draw_menu(screen: pygame.surface, character_list: list[Character]) -> None:
    screen.blit(MENU, MENU_RECT)
    screen.blit(ATTACK_TEXT, [100, HEIGHT-160])
    screen.blit(SPECIAL_TEXT, [300, HEIGHT-160])
    
    screen.blit(DEFENSE_TEXT, [100, HEIGHT-100])
    screen.blit(CHARM_TEXT, [300, HEIGHT-100])
    
    y = 150
    for character in character_list:
        font = pygame.font.Font(None, 30)
        text = font.render(f"{character.get_character_name()} - {character.get_character_life_points()}/100", 
                           True, pygame.Color("YELLOW"))
        screen.blit(text, [WIDTH-300, HEIGHT-y])
        y -= 20
    
    
