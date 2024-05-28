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
character_list = list()
p1 = personagens.Personagem("Maga", 100, 30, 20, 45, 1, True)
p2 = personagens.Personagem("Maga", 100, 30, 20, 45, 2, True)
p3 = personagens.Personagem("Maga", 100, 30, 20, 45, 3, True)
p4 = personagens.Personagem("Maga", 100, 30, 20, 45, 1, False)
p5 = personagens.Personagem("Maga", 100, 30, 20, 45, 2, False)
character_list.append(p1)
character_list.append(p2)
character_list.append(p3)
character_list.append(p4)
character_list.append(p5)


def main():
    end = False
    while not end:  # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        # desenha a janela com o fundo
        SCREEN.blit(BACKGROUND, START)

        # gera personagens
        for character in character_list:
            character.draw_character(SCREEN)

        clock.tick(FPS)  # Definir a taxa de quadros
        pygame.display.flip()  # Atualizar a exibição

    pygame.quit()


if __name__ == "__main__":
    main()
