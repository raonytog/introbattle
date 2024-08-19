from characters import *
from screen import *
from points import PointSys
 
def character_movement(character: Character, enemy_list: list, ally_list: list, position: list, screen: pygame.surface, pontos: PointSys) -> None:
    # attack
    escolheu = 0
    while not escolheu:
        if position == [80, 568]:
            pontos.inc_point()
            enemy = choose_enemy(screen, character, enemy_list)
            enemy.receive_dmg(character.get_character_attack())
            escolheu = 1
            
        # special
        elif position == [280, 568] and pontos.get_points() >= 3:
            pontos.dec_point()
            pontos.dec_point()
            escolheu = 1
            
            if character.get_character_name() == 'meele':
                enemy = choose_enemy(screen, character, enemy_list)
                character.sp_atk(enemy, screen, enemy_list, ally_list)
                sp_animation(character, enemy, screen, ally_list, enemy_list)
                
            elif character.get_character_name() == 'mage':
                character.sp_atk(enemy_list)
                sp_animation(character, enemy, screen, ally_list, enemy_list)
                
                
            elif character.get_character_name() == 'ranged':
                enemy = choose_enemy(screen, character, enemy_list)
                character.sp_atk(enemy)
                sp_animation(character, enemy, screen, ally_list, enemy_list)
                
            elif character.get_character_name() == 'summoner':
                character.sp_atk(enemy_list)
                sp_animation(character, enemy, screen, ally_list, enemy_list)
                
            elif character.get_character_name() == 'bard':
                ally = choose_ally(screen, ally_list, enemy_list)
                character.sp_atk(ally)
                sp_animation(character, ally, screen, ally_list, enemy_list)
            
        # defense
        elif position == [80, 628] and pontos.get_points() >= 2:
            pontos.dec_point()
            character.sp_def()
            escolheu = 1

def enemy_moviment(character: Character, character_list: list[Character], enemy_list: list[Character], screen: pygame.surface) -> None:
    for char in character_list:
        if char.get_character_life_points() > 0:
            if enemy_list[0].life_points > 0:
                char.receive_dmg(enemy_list[0].attack)
                break
                
            elif enemy_list[1].life_points > 0:
                char.receive_dmg(enemy_list[1].attack)
                break
                
            else: # both death
                break

def combat_loop(screen: pygame.surface, character_list: list[Character], enemy_list: list[Character], pontos: PointSys) -> None:
    run = True
    x, y = 80, HEIGHT-160

    while run:
        for character in character_list:
            # se o caractere estiver vivo, da a opcao de acao para ele
            if character.get_character_life_points() > 0:
                draw_menu_interactions(screen, character, character_list, enemy_list, [x, y], pontos)
                
                pressed_z = False
                while not pressed_z:
                    update_screen()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                
                        # movimento da seta
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT and x == 80:
                                x += 200
                                draw_menu_interactions(screen, character, character_list, enemy_list, [x, y], pontos)
                                
                            elif event.key == pygame.K_LEFT and x == 280:
                                x -= 200
                                draw_menu_interactions(screen, character, character_list, enemy_list, [x, y], pontos)
                                
                            elif event.key == pygame.K_UP and y == 568+60:
                                y -= 60
                                draw_menu_interactions(screen, character, character_list, enemy_list, [x, y], pontos)
                                
                            elif event.key == pygame.K_DOWN and y == 568:
                                y += 60
                                draw_menu_interactions(screen, character, character_list, enemy_list, [x, y], pontos)
                                    
                            elif event.key == pygame.K_z:
                                character_movement(character, enemy_list, character_list, [x, y], screen, pontos)
                                enemy_moviment(character, character_list, enemy_list, screen)
                                pressed_z = True
                                
                                # Verifica se acabou o jogo
                                if is_player_defeated(character_list) or is_player_winner(enemy_list):
                                    update_screen()
                                    return
                                
                        update_screen()

def choose_ally(screen: pygame.surface, character_list: list, enemy_list: list) -> Character:
    seta_y = 250
    seta_x1, seta_x2, seta_x3  = 120, 300, 450
    x, y = seta_x1, seta_y
    
    run = True
    while run:
        draw_screen(screen, character_list, enemy_list)
        screen.blit(SETA, [x, y])
        for event in pygame.event.get():
            select_sound()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and x < 450:
                    x += 150
                        
                elif event.key == pygame.K_LEFT and x > 150:
                    x -= 150
                            
                elif event.key == pygame.K_z:
                    if x == 120:
                        return character_list[0]
                    
                    elif x == 300:
                        return character_list[1]
                        
                    elif x == 450:
                        return character_list[2]
                        
        update_screen()
    

def choose_enemy(screen: pygame.surface, character: Character, enemy_list: list[DukeFisheron, EyeOfCtchulu])-> Character:
    x1, y1 = WIDTH-250, 230
    x2, y2 = x1-250, y1-230
    
    if enemy_list[1].get_character_life_points() > 0:
        screen.blit(enemy_list[1].get_selected_img(), [x2, y2])
        selected = 1
        
    elif enemy_list[0].get_character_life_points() > 0:
        screen.blit(enemy_list[0].get_selected_img(), [x1, y1]) # o outro
        selected = 0
        
    update_screen()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN:
                select_sound()
                
                if event.key == pygame.K_RIGHT and enemy_list[0].get_character_life_points() > 0:
                    screen.blit(enemy_list[0].get_selected_img(), [x1, y1])
                    selected = 0
                    if enemy_list[1].get_character_life_points() > 0:
                        screen.blit(enemy_list[1].img, [x2, y2]) # o outro
                    update_screen()
                            
                elif event.key == pygame.K_LEFT and enemy_list[1].get_character_life_points() > 0:
                    screen.blit(enemy_list[1].get_selected_img(), [x2, y2])
                    selected = 1
                    if enemy_list[0].get_character_life_points() > 0:
                        screen.blit(enemy_list[0].img, [x1, y1]) # o outro
                    update_screen()
                    
                elif event.key == pygame.K_z:
                    return enemy_list[selected]

        update_screen()

def is_player_defeated(character_list: list[Character]) -> bool:
    for char in character_list:
        if char.get_character_life_points() > 0:
            return False
        
    return True

def is_player_winner(enemy_list: list[Character]) -> bool:
    for enemy in enemy_list:
        if enemy.get_character_life_points() > 0:
            return False
        
    return True