import pygame
import characters

pygame.init()

# tempo de acao do jogo
clock = pygame.time.Clock()

# criacao dos personagens
tomate = characters.Vilao1("Tomate")
abobora = characters.Vilao2("Abobora")

# janela do jogo
janela = pygame.display.set_mode((1024, 728))
bg_img = pygame.image.load("./imgs/Background.png")
pygame.display.set_caption("Introbattle")

# game loop
endCondition = False
while not endCondition:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            endCondition = True

    # desenha a janela com o fundo
    janela.blit(bg_img, (0, 0))

    # gera personagens
    tomate.desenha_personagem(janela)
    abobora.desenha_personagem(janela)


    pygame.display.flip()  # Atualizar a exibição
    clock.tick(60)  # Definir a taxa de quadros

pygame.quit()
