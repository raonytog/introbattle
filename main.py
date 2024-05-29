from pygame import *
from characters import *
from os import *

pygame.init()

# tempo de ação do jogo
clock = pygame.time.Clock()
FPS = 60

# tamanhos da janela do jogo
WIDTH, HEIGHT = 1024, 728
START = (0, 0)
SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)

# definindo o background do jogo e ajustando seu tamanho
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

# titulo do jogo
pygame.display.set_caption("Introbattle")

# personagens
CHARACTER_LIST = pygame.sprite.Group()
# CHARACTER_LIST.add(Meele())
CHARACTER_LIST.add(Mage())
# CHARACTER_LIST.add(Ranged())
CHARACTER_LIST.add(Summoner())
# CHARACTER_LIST.add(Tanker())

ENEMIES_LIST = pygame.sprite.Group()
ENEMIES_LIST.add(DukeFisheron())
ENEMIES_LIST.add(EyeOfCtchulu())

# def mov_selection(SCREEN, CHARACTER_LIST):
    

def draw_start_screen(SCREEN): 
    font = pygame.font.Font(None, 40)
    text = font.render('Click anywhere!', True, pygame.Color("YELLOW"))
    text_rect = text.get_rect(center=(WIDTH/2, 200))
    
    SCREEN.blit(START_BACKGROUND, START)
    SCREEN.blit(INTROBATTLE, INTROBATTLE_RECT)
    SCREEN.blit(text, text_rect)

def draw_screen(SCREEN, CHARACTER_LIST):
    """_summary_
        Desenha uma tela com todos os personagens presentes no jogo

    Args:
        SCREEN (SURFACE): tela redimensionada 
        CHARACTER_LIST (LIST): lista de personagens
    """
    
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(BACKGROUND, START)

    for character in CHARACTER_LIST:
        character.draw_character(SCREEN)

def update_screen():
    clock.tick(FPS)  # Definir a taxa de quadros
    pygame.display.flip()  # Atualizar a exibição

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
            draw_screen(SCREEN, CHARACTER_LIST)
        
        update_screen()
        
        # Lógica para mudar de tela inicial para o jogo
        # Se necessário, adicionar uma condição para mudar start_screen para False
        
    pygame.quit()

if __name__ == "__main__":
    main()
