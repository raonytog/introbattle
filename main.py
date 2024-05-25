import pygame

pygame.init()

clock = pygame.time.Clock()
endCondition = False

# janela do jogo
janela = pygame.display.set_mode((1024, 720))
pygame.display.set_caption("Introbattle")

while not endCondition:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            endCondition = True

    pygame.display.flip()  # Atualizar a exibição
    clock.tick(60)  # Definir a taxa de quadros

pygame.quit()
