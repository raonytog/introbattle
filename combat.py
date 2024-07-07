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

def draw_menu_options(screen: pygame.surface, character: Character, character_list: list[Character], enemy_list: list[Character]) -> None:
    screen.blit(MENU, MENU_RECT)
    screen.blit(ATTACK_TEXT, [100, HEIGHT-160])
    screen.blit(SPECIAL_TEXT, [300, HEIGHT-160])
    
    screen.blit(DEFENSE_TEXT, [100, HEIGHT-100])
    screen.blit(CHARM_TEXT, [300, HEIGHT-100])
    
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
        
        
def character_movement(character: Character, enemy_list: list[Character], position: list, screen: pygame.surface) -> None:
    # attack
    if position == [80, 568]:
        enemy = choose_enemy(screen, character, enemy_list)
        enemy.receive_dmg(character.get_character_attack())
        
        
    # elif list == [280, 160]:
    #
    # elif list == [80, 628]:
    #
    # elif list == [80, 568]:
        
        
def enemy_moviment(character: Character, character_list: list[Character], enemy_list: list[Character], screen: pygame.surface) -> None:
    for char in character_list:
        if char.get_character_life_points() > 0:
            if enemy_list[0].life_points > 0:
                char.receive_dmg(enemy_list[0].attack)
                break
                
            elif enemy_list[1].life_points > 0:
                char.receive_dmg(enemy_list[1].attack)
                break
                
            # ambos inimigos mortos
            else:
                break

def combat_loop(screen: pygame.surface, character_list: list[Character], enemy_list: list[Character]) -> None:
    run = True
    x, y = 80, HEIGHT-160
    while run:
        draw_screen(SCREEN, character_list, enemy_list)
        
        for character in character_list:
            draw_menu_options(screen, character, character_list, enemy_list)
        
            # seta apontando pra opcao de acao selecionada
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
                            
                        elif event.key == pygame.K_z:
                            character_movement(character, enemy_list, [x, y], screen)
                            update_screen()
                            
                            enemy_moviment(character, character_list, enemy_list, screen)
                            update_screen()
                            
        update_screen()
        
# def choose_ally(character_list: list[Character]) -> Character:
    
    

def choose_enemy(screen: pygame.surface, character: Character, enemy_list: list[DukeFisheron, EyeOfCtchulu])-> Character:
    x1, y1 = WIDTH-250, 170
    x2, y2 = WIDTH-250-250, 170-150
    
    screen.blit(enemy_list[1].get_selected_img(), [x2, y2])
    selected = 1
    screen.blit(enemy_list[0].img, [x1, y1]) # o outro
    update_screen()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    screen.blit(enemy_list[0].get_selected_img(), [x1, y1])
                    selected = 0
                    screen.blit(enemy_list[1].img, [x2, y2]) # o outro
                    update_screen()
                            
                elif event.key == pygame.K_LEFT:
                    screen.blit(enemy_list[1].get_selected_img(), [x2, y2])
                    selected = 1
                    screen.blit(enemy_list[0].img, [x1, y1]) # o outro
                    update_screen()
                    
                elif event.key == pygame.K_z:
                    return enemy_list[selected]

                
        # tem que fazer a logica ainda para retornar o inimigo selecionado 
        update_screen()
                    
            