from characters import *
from screen import *
from combat import *

pygame.init()

sound_bg = pygame.mixer.Sound('lofi.mp3')
sound_bg.set_volume(0.05)

# personagens
CHARACTER_LIST = list()
CHARACTER_LIST.append(Meele())
CHARACTER_LIST.append(Mage())
CHARACTER_LIST.append(Ranged())
CHARACTER_LIST.append(Summoner())
CHARACTER_LIST.append(Bard())
SELECTED_CHARACTERS_LIST = pygame.sprite.Group()

# inimigos
ENEMIES_LIST = list()
ENEMIES_LIST.append(DukeFisheron())
ENEMIES_LIST.append(EyeOfCtchulu())


def main():
    sound_bg.play()
    draw_start_screen(SCREEN)
    SELECTED_CHARACTERS_LIST = draw_character_selection(SCREEN, CHARACTER_LIST)
    SELECTED_CHARACTERS_LIST.sort(key=lambda character: character.speed, reverse=True)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True
                pygame.quit()
        
        # game loop 
        combat_loop(SCREEN, SELECTED_CHARACTERS_LIST, ENEMIES_LIST)
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
