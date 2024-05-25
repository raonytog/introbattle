import pygame
import window

pygame.init()

clock = pygame.time.Clock()
executando = True

janela = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Introbattle")
cor = (0, 100, 255)

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Atualizar a exibição
    pygame.display.flip()

    # Definir a taxa de quadros
    clock.tick(60)
    janela.fill(cor)

pygame.quit()
