import characters
from screen import *
from combat import *
from points import PointSys

pontos = PointSys()

pygame.init()

sound_bg = pygame.mixer.Sound('assets/terraria_day.mp3')
sound_bg.set_volume(0.03)

# personagens
CHARACTER_LIST = list()
CHARACTER_LIST.append(characters.Meele())
CHARACTER_LIST.append(characters.Mage())
CHARACTER_LIST.append(characters.Ranged())
CHARACTER_LIST.append(characters.Summoner())
CHARACTER_LIST.append(characters.Bard())
SELECTED_CHARACTERS_LIST = pygame.sprite.Group()

# inimigos
ENEMIES_LIST = list()
ENEMIES_LIST.append(characters.DukeFisheron())
ENEMIES_LIST.append(characters.EyeOfCtchulu())


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
        combat_loop(SCREEN, SELECTED_CHARACTERS_LIST, ENEMIES_LIST, pontos)
        
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
