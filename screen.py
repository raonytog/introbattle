import pygame
import os

FPS = 60

pygame.init()

# tempo de ação do jogo
clock = pygame.time.Clock()

# titulo do jogo
pygame.display.set_caption("Introbattle")

# tamanhos da janela do jogo
WIDTH, HEIGHT = 1024, 728
START = (0, 0)
SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)

# definindo imagens do jogo e ajustando seu tamanho
BACKGROUND = pygame.image.load(os.path.join('imgs', "fundo.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, SIZE)

START_BACKGROUND = pygame.image.load(os.path.join('imgs', 'start_screen.png'))
START_BACKGROUND = pygame.transform.scale(START_BACKGROUND, SIZE)

INTROBATTLE = pygame.image.load(os.path.join('imgs', 'introbattle.png'))
INTROBATTLE = pygame.transform.scale(INTROBATTLE, (400, 100))
INTROBATTLE_RECT = INTROBATTLE.get_rect()
INTROBATTLE_RECT.center = (WIDTH/2, 100)

SELECTION_BANNER = pygame.image.load(os.path.join('imgs', 'banner.png'))
SELECTION_BANNER = pygame.transform.scale(SELECTION_BANNER, (80, 110))
SELECTION_BANNER_RECT = SELECTION_BANNER.get_rect()


def draw_start_screen(screen):
    """_summary_
        Desenha a tela inicial, com a logo do logo e a ordem de click para coemcar

    Args:
        screen (SURFACE): tela redimensionada
    """
    font = pygame.font.Font(None, 40)
    text = font.render('Click anywhere!', True, pygame.Color("YELLOW"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    
    screen.blit(START_BACKGROUND, START)
    screen.blit(INTROBATTLE, INTROBATTLE_RECT)
    screen.blit(text, text_rect)


def draw_character_selection(screen, character_list):
    """Desenha a tela de seleção de personagens e permite ao jogador selecionar até 3 personagens.

    Args:
        screen (pygame.Surface): Tela redimensionada.
        character_list (pygame.sprite.Group): Grupo com todos os personagens do jogo.

    Returns:
        pygame.sprite.Group: Grupo com apenas os 3 personagens selecionados.
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
    
    pygame.display.flip()

    run = True
    while run and len(selected_characters) < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                for character, rect in character_positions:
                    if rect.collidepoint(mouse_position):  # se o mouse tiver no retangulo
                        if character in selected_characters:  # se ja tiver selecionado, remove-o
                            selected_characters.remove(character)
                            
                        elif len(selected_characters) < 3:  # caso contrario, adiciona-o
                            selected_characters.add(character)
                            
                        break

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

        pygame.display.flip()

    return selected_characters


def draw_screen(screen, character_list, enemies_list):
    """_summary_
        Desenha a tela principal do jogo, contendo:
        1- Herois selecionados
        2- Viloes
        3- Menu

    Args:
        screen (SURFACE): tela redimensionada
        character_list (LIST): lista de personagens
        enemies_list (LIST): lista dos inimigos
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


def update_screen():
    """_summary_
        Atualiza a taxa de quadros para 60 e atualiza a exibicao da tela
    """
    clock.tick(FPS)  # Definir a taxa de quadros
    pygame.display.flip()  # Atualizar a exibição
