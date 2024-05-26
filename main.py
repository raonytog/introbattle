import pygame
import characters

pygame.init()

clock = pygame.time.Clock() # tempo de acao do jogo
endCondition = False

tomate = characters.Vilao1("Tomate")
abobora = characters.Vilao2("Abobora")

# janela do jogo
janela = pygame.display.set_mode((1024, 728))
bg_img = pygame.image.load("./imgs/Background.png")

pygame.display.set_caption("Introbattle")

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
