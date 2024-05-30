import pygame
import os

FPS = 60

pygame.init()

# tempo de ação do jogo
clock = pygame.time.Clock()

# titulo do jogo
pygame.display.set_caption("Introbattle: Terraria project")

# tamanhos da janela do jogo
WIDTH, HEIGHT = 1024, 728
START = (0, 0)
SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)

# definindo imagens do jogo e ajustando seu tamanho
BACKGROUND = pygame.image.load(os.path.join('imgs', "fundo.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, SIZE)

START_BACKGROUND = pygame.image.load(os.path.join('imgs', 'start_screen.png'))

INTROBATTLE = pygame.image.load(os.path.join('imgs', 'introbattle.png'))
INTROBATTLE = pygame.transform.scale_by(INTROBATTLE, 2)
INTROBATTLE_RECT = INTROBATTLE.get_rect()
INTROBATTLE_RECT.center = (WIDTH/2, 100)

SELECTION_BANNER = pygame.image.load(os.path.join('imgs', 'red_banner.png'))
SELECTION_BANNER = pygame.transform.scale_by(SELECTION_BANNER, 6)
SELECTION_BANNER_RECT = SELECTION_BANNER.get_rect()

SETA = pygame.image.load(os.path.join('imgs', 'seta.png'))
SETA = pygame.transform.scale_by(SETA, 2)
SETA_RECT = SETA.get_rect()

MENU = pygame.image.load(os.path.join('imgs', 'menu.png'))

MENU_RECT = MENU.get_rect()


def draw_start_screen(screen):
    """_summary_
        Desenha a tela inicial, com a logo do logo e a ordem de click para comecar
        a selecao de personagem

    Args:
        screen (Surface): tela redimensionada
    """
    font = pygame.font.Font(None, 40)
    text = font.render('Click anywhere to star!', True, pygame.Color("YELLOW"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    
    screen.blit(START_BACKGROUND, START)
    screen.blit(INTROBATTLE, INTROBATTLE_RECT)
    screen.blit(text, text_rect)
    update_screen()
    
    run = True
    while run:  # loop para verificar se o botao do mouse foi clickado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            


def draw_character_selection(screen, character_list):
    """Desenha a tela de seleção de personagens e permite ao jogador selecionar até 3 personagens.

    Args:
        screen (Surface): Tela redimensionada.
        character_list (Group): Grupo com todos os personagens do jogo.

    Returns:
        Group: Grupo com apenas os 3 personagens selecionados.
    """
    selected_characters = pygame.sprite.Group()
    character_positions = []

    # Desenha os personagens no lugar
    screen.blit(BACKGROUND, START)
    x = 180
    for character in character_list:
        character.draw_character_position(screen, (x, 420))
        character_positions.append((character, pygame.Rect(x, 420, character.rect.width, character.rect.height)))
        x += 150

    # Inicializando a posição da seta
    seta_index = 0
    SETA_RECT.midbottom = character_positions[seta_index][1].midtop

    # Criando o botão 'Start'
    start_button_font = pygame.font.Font(None, 40)
    start_button_text = start_button_font.render('START', True, pygame.Color("YELLOW"))
    start_button_rect = start_button_text.get_rect(center=(WIDTH / 2, 600))

    run = True
    while run:
        for event in pygame.event.get():
            # se fechou o jogo
            if event.type == pygame.QUIT:
                run = False
                
            # se apertou tecla do teclado
            elif event.type == pygame.KEYDOWN:
                
                # left arrow (<-)
                if event.key == pygame.K_LEFT:
                    seta_index = max(0, seta_index - 1)
                    
                # right arrow (->)
                elif event.key == pygame.K_RIGHT:
                    seta_index = min(len(character_positions) - 1, seta_index + 1)
                    
                # select key (Z)
                elif event.key == pygame.K_z:  # selection
                    character, rect = character_positions[seta_index]
    
                    # Verifica se o personagem ja esta no grupo para removelo,
                    if character in selected_characters:  # se ja ta no grupo
                        selected_characters.remove(character)
                        
                    # caso nao esteja e o grupo nao esteja cheio, ele é adicionado 
                    elif len(selected_characters) < 3:  #
                        selected_characters.add(character)
                
                # Atualizando a posição da seta de acordo com o ultimo movimento
                SETA_RECT.midbottom = character_positions[seta_index][1].midtop

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos) and len(selected_characters) >= 1:
                    run = False
        #fim do for
        
        # Redesenha os personagens e destaca os selecionados
        screen.blit(BACKGROUND, START)
        for character, rect in character_positions:
            character.draw_character_position(screen, rect.topleft)
            if character in selected_characters:
                # Calcula a posição para desenhar o banner de seleção atrás do personagem
                banner_position = (rect.centerx - SELECTION_BANNER_RECT.width / 2,
                                   rect.centery - SELECTION_BANNER_RECT.height / 2)
                screen.blit(SELECTION_BANNER, banner_position)
                character.draw_character_position(screen, rect.topleft)

        # Desenha a seta
        screen.blit(SETA, SETA_RECT.topleft)

        # Desenha o texto de instruções
        font = pygame.font.Font(None, 40)
        text = font.render('Press Z and arrows to select till 3 characters!', True, pygame.Color("YELLOW"))
        text_rect = text.get_rect(center=(WIDTH / 2, 200))
        screen.blit(text, text_rect)

        # Desenha o botão 'Start' se 3 personagens estiverem selecionados
        if len(selected_characters) >= 1:
            screen.blit(start_button_text, start_button_rect)

        pygame.display.flip()
        # fim do while

    return selected_characters


def draw_screen(screen, character_list, enemies_list):
    """_summary_
        Desenha a tela principal do jogo, contendo:
        1- Herois selecionados
        2- Viloes
        3- Menu

    Args:
        screen (Surface): tela redimensionada
        character_list (List): lista de personagens
        enemies_list (List): lista dos inimigos
    """
    
    screen.blit(BACKGROUND, START)

    x = 100
    for character in character_list:
        character.draw_character_position(screen, (x, 420))
        x += 150
        
    x, y = WIDTH-250, 270
    for enemies in enemies_list:
        enemies.draw_character_position(screen, (x, y))
        x -= 250
        y -= 180


def draw_menu(screen, character_list):
    screen.blit(MENU, MENU_RECT)


def update_screen():
    """_summary_
        Atualiza a taxa de quadros para 60 e atualiza a exibicao da tela
    """
    clock.tick(FPS)  # Definir a taxa de quadros
    pygame.display.flip()  # Atualizar a exibição
