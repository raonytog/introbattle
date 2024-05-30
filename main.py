from pygame import *
from characters import *
from os import *
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

def main():
    start_screen = True
    character_select_screen = False
    end = False
    
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # sai do jogo
                end = True
                
            elif start_screen is True:  # tela de entrada
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start_screen = False
                    character_select_screen = True
            
        if start_screen is True:
            draw_start_screen(SCREEN)
        
        else:
            draw_screen(SCREEN, CHARACTER_LIST, ENEMIES_LIST)
        
        update_screen()
        # fim do for
        
    pygame.quit()
    # fim do while

if __name__ == "__main__":
    main()
