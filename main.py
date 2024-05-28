import pygame
import personagens
import os

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
BACKGROUND = pygame.image.load(os.path.join('imgs', "background.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, SIZE)

# titulo do jogo
pygame.display.set_caption("Introbattle")

# retangulo de selecao
SELECTION_RECTANGLE = pygame.image.load(os.path.join('imgs', "frame.png"))

# personagens
CHARACTER_LIST = list()
CHARACTER_LIST.append(personagens.Personagem("Maga", 100, 30, 20, 45, 1, True))
CHARACTER_LIST.append(personagens.Personagem("Maga", 100, 30, 20, 45, 2, True))
CHARACTER_LIST.append(personagens.Personagem("Maga", 100, 30, 20, 45, 3, True))
CHARACTER_LIST.append(personagens.Personagem("Maga", 100, 30, 20, 45, 1, False))
CHARACTER_LIST.append(personagens.Personagem("Maga", 100, 30, 20, 45, 2, False))


def draw_character_select(SCREEN, CHARACTER_LIST):
    """_summary_
        Desenha a tela de selecao dos personagens para escolha dos quais 
        participarao do decorrer do jogo

    Args:
        SCREEN (SURFACE): tela redimencionada 
        CHARACTER_LIST (LIST): lista de personagens

    Returns:
        LIST: Lista de personagens selecionados
    """
    
    count = 0
    PRESENT_CHARACTER = list()
    
    SCREEN.fill(255, 255, 255)
    for character in CHARACTER_LIST:
        character.draw_character(SCREEN)
        
    return PRESENT_CHARACTER
        

def draw_screen(SCREEN, CHARACTER_LIST):
    """_summary_
        Dsenha uma tela com todos os personagens presentes no jogo

    Args:
        SCREEN (SURFACE): tela redimencionada 
        CHARACTER_LIST (LIST): lista de personagens
    """
    
    SCREEN.fill(color="WHITE")
    SCREEN.blit(BACKGROUND, START)

    for character in CHARACTER_LIST:
        character.draw_character(SCREEN)

    clock.tick(FPS)  # Definir a taxa de quadros
    pygame.display.flip()  # Atualizar a exibição


def main():
    end = False
    while not end:  # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        keys_pressed = pygame.key.get_pressed()


        # desenha toda a game screen
        draw_screen(SCREEN, CHARACTER_LIST)

    pygame.quit()


if __name__ == "__main__":
    main()
