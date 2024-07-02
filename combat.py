from characters import *
from screen import *

MENU = pygame.image.load(os.path.join('imgs', 'menu.png'))
MENU_RECT = MENU.get_rect()


FONT = pygame.font.Font(None, 40)
SELECT_TEXT = FONT.render(">", True, pygame.Color("YELLOW"))
SELECT_RECT = SELECT_TEXT.get_rect()

ATTACK_TEXT = FONT.render("Attack", True, pygame.Color("YELLOW"))
ATTACK_RECT = ATTACK_TEXT.get_rect()

DEFENSE_TEXT = FONT.render("Defense", True, pygame.Color("YELLOW"))
DEFENSE_RECT = DEFENSE_TEXT.get_rect()

SPECIAL_TEXT = FONT.render("Special", True, pygame.Color("YELLOW"))
SPECIAL_RECT = SPECIAL_TEXT.get_rect()

CHARM_TEXT = FONT.render("Charm", True, pygame.Color("YELLOW"))
CHARM_RECT = CHARM_TEXT.get_rect()

def draw_menu_options(screen: pygame.surface, character_list: list[Character]) -> None:
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

def draw_menu(screen: pygame.surface, character_list: list[Character]) -> None:
    
        
    run = True
    x, y = 80, HEIGHT-160
    while run:
        draw_menu_options(screen, character_list)
        screen.blit(SELECT_TEXT, [x, y])
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                # movimento da seta
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and x == 80:
                        x += 200
                        
                    elif event.key == pygame.K_LEFT and x == 280:
                        x -= 200
                        
                    elif event.key == pygame.K_UP and y == 568+60:
                        y -= 60
                    
                    elif event.key == pygame.K_DOWN and y == 568:
                        y += 60
                        
        update_screen()
                        
        
                    
                
                    
                
