from characters import *
from screen import *

pygame.init()

# personagens
CHARACTER_LIST = pygame.sprite.Group()
CHARACTER_LIST.add(Meele())
CHARACTER_LIST.add(Mage())
CHARACTER_LIST.add(Ranged())
CHARACTER_LIST.add(Summoner())
CHARACTER_LIST.add(Bard())

ENEMIES_LIST = pygame.sprite.Group()
ENEMIES_LIST.add(DukeFisheron())
ENEMIES_LIST.add(EyeOfCtchulu())

SELECTED_CHARACTERS_LIST = pygame.sprite.Group()


def main():
    draw_start_screen(SCREEN)
    SELECTED_CHARACTERS_LIST = draw_character_selection(SCREEN, CHARACTER_LIST)
    
    end = False
    while not end:
        draw_screen(SCREEN, SELECTED_CHARACTERS_LIST, ENEMIES_LIST)
        draw_menu(SCREEN, SELECTED_CHARACTERS_LIST)
        update_screen()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # sai do jogo
                end = True
                
            # fim do for
        # fim do while
        
    pygame.quit()


if __name__ == "__main__":
    main()
