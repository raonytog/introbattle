import pygame
import personagens

pygame.init()

# tempo de ação do jogo
clock = pygame.time.Clock()

# criação dos personagens
characters = pygame.sprite.Group()

v1 = personagens.Vilao1("Abobora")
v2 = personagens.Vilao2("Tomate")
p1 = personagens.Mage("Maga", 1)
p2 = personagens.Mage("p2", 2)
p3 = personagens.Mage("p3", 3)

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
    v1.desenha_personagem(janela)
    v2.desenha_personagem(janela)
    p1.desenha_personagem(janela)
    p2.desenha_personagem(janela)
    p3.desenha_personagem(janela)

    pygame.display.flip()  # Atualizar a exibição
    clock.tick(60)  # Definir a taxa de quadros

pygame.quit()
