import characters
from screen import *
from combat import *
from points import PointSys

pontos = PointSys()
pygame.init()

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


def game_result(ally_list: list[Character], enemy_list: list[Character], screen: pygame.surface.Surface):
    """Atualiza a tela para a tela resultado do jogo (vitória ou derrota)

    Args:
        ally_list (list[Character]): Lista de aliados
        enemy_list (list[Character]): Lista de inimigos
        screen (pygame.surface.Surface): Tela
    """
    # player perdeu
    if is_player_defeated(ally_list):
        time.sleep(0.2)
        draw_lost_screen(screen)
    
    # player ganhou
    elif is_player_winner(enemy_list):
        time.sleep(0.2)
        draw_win_screen(SCREEN)

def main():
    play_sound('assets/terraria_day.mp3', 0.01)
    draw_start_screen(SCREEN)
    SELECTED_CHARACTERS_LIST = draw_character_selection(SCREEN, CHARACTER_LIST)
    SELECTED_CHARACTERS_LIST.sort(key=lambda character: character.speed, reverse=True)

    run = True
    while run:
        run = close_screen()
        combat_loop(SCREEN, SELECTED_CHARACTERS_LIST, ENEMIES_LIST, pontos)
        game_result(SELECTED_CHARACTERS_LIST, ENEMIES_LIST, SCREEN)
        update_screen()

    pygame.quit()

if __name__ == "__main__":
    main()
