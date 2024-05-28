import pygame
import personagens

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
BACKGROUND = pygame.image.load("./imgs/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, SIZE)

# titulo do jogo
pygame.display.set_caption("Introbattle")

# personagens
p1 = personagens.Personagem("Maga", 100, 30, 20, 45, 1, True)
p2 = personagens.Personagem("Maga", 100, 30, 20, 45, 2, True)
p3 = personagens.Personagem("Maga", 100, 30, 20, 45, 3, True)


def main():
    end = False
    while not end:  # game loop
        for evento in pygame.event.get():

            # se fechou a janela
            if evento.type == pygame.QUIT:
                end = True

        # desenha a janela com o fundo
        SCREEN.blit(BACKGROUND, START)

        # gera personagens
        p1.draw_character(SCREEN)
        p2.draw_character(SCREEN)
        p3.draw_character(SCREEN)

        clock.tick(FPS)  # Definir a taxa de quadros
        pygame.display.flip()  # Atualizar a exibição

    pygame.quit()


if __name__ == "__main__":
    main()
