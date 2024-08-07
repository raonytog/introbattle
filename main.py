from characters import *
from screen import *
from combat import *

pygame.init()

# personagens
CHARACTER_LIST = list()
CHARACTER_LIST.append(Meele())
CHARACTER_LIST.append(Mage())
CHARACTER_LIST.append(Ranged())
CHARACTER_LIST.append(Summoner())
CHARACTER_LIST.append(Bard())

ENEMIES_LIST = list()
ENEMIES_LIST.append(DukeFisheron())
ENEMIES_LIST.append(EyeOfCtchulu())

SELECTED_CHARACTERS_LIST = pygame.sprite.Group()


def main():
    draw_start_screen(SCREEN)
    SELECTED_CHARACTERS_LIST = draw_character_selection(SCREEN, CHARACTER_LIST)
    SELECTED_CHARACTERS_LIST.sort(key=lambda character: character.speed, reverse=True)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
                pygame.quit()
                
        combat_loop(SCREEN, SELECTED_CHARACTERS_LIST, ENEMIES_LIST)
        update_screen()
        
        # player perdeu
        if is_player_defeated(SELECTED_CHARACTERS_LIST):
            draw_lost_screen(SCREEN)
    
        # player ganhou
        elif is_player_winner(ENEMIES_LIST):
            draw_win_screen(SCREEN)
        
        update_screen()
                
        # fim do for
    # fim do while
    
    pygame.quit()

if __name__ == "__main__":
    main()
