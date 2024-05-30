import os
import pygame

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

# definindo o imagens do jogo e ajustando seu tamanho
BACKGROUND = pygame.image.load(os.path.join('imgs', "fundo.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, SIZE)

START_BACKGROUND = pygame.image.load(os.path.join('imgs', 'start_screen.png'))
START_BACKGROUND = pygame.transform.scale(START_BACKGROUND, SIZE)

INTROBATTLE = pygame.image.load(os.path.join('imgs', 'introbattle.png'))
INTROBATTLE = pygame.transform.scale(INTROBATTLE, (400, 100))
INTROBATTLE_RECT = INTROBATTLE.get_rect()
INTROBATTLE_RECT.center = (WIDTH/2, 100)

SELECTION_BANNER = pygame.image.load(os.path.join('imgs', 'banner.png'))
SELECTION_BANNER_RECT = SELECTION_BANNER.get_rect()

def draw_start_screen(SCREEN): 
    """_summary_
        Desenha a tela inicial, com a logo do logo e a ordem de click para coemcar

    Args:
        SCREEN (SURFACE): tela redimensionada
    """
    font = pygame.font.Font(None, 40)
    text = font.render('Click anywhere!', True, pygame.Color("YELLOW"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    
    SCREEN.blit(START_BACKGROUND, START)
    SCREEN.blit(INTROBATTLE, INTROBATTLE_RECT)
    SCREEN.blit(text, text_rect)
    
def draw_screen(SCREEN, CHARACTER_LIST, ENEMIES_LIST):
    """_summary_
        Desenha a tela principal do jogo, contendo:
        1- Herois selecionados
        2- Viloes
        3- Menu

    Args:
        SCREEN (SURFACE): tela redimensionada 
        CHARACTER_LIST (LIST): lista de personagens
    """
    
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(BACKGROUND, START)

    x = 100
    for character in CHARACTER_LIST:
        character.draw_character_position(SCREEN, (x, 420))
        x += 150
        
    x, y = WIDTH-250, 270
    for enemies in ENEMIES_LIST:
        enemies.draw_character_position(SCREEN, (x, y))
        x -= 250
        y -= 180
        
def update_screen():
    """_summary_
        Atualiza a taxa de quadros para 60 e atualiza a exibicao da tela
    """
    clock.tick(FPS)  # Definir a taxa de quadros
    pygame.display.flip()  # Atualizar a exibição