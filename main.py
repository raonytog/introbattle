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
    
    run = True
    while run:
        draw_screen(SCREEN, SELECTED_CHARACTERS_LIST, ENEMIES_LIST)
        draw_menu(SCREEN, SELECTED_CHARACTERS_LIST)
        update_screen()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # sai do jogo
                run = True
                pygame.quit()
                
            # fim do for
        # fim do while
        
    pygame.quit()


if __name__ == "__main__":
    main()
