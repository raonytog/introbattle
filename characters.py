import pygame

max_size_sprite = (150, 150)

largura = 1024
altura = 728


class Personagem(pygame.sprite.Sprite):
    """
    Propriedades:
        rect = area do sprite
        img = sprite do personagem
        pos_x = posicao x
        pos_y = posicao y
    """

    def __init__(self, nome, escolha):
        super().__init__()
        self.imagem = pygame.image.load(f"./imgs/{nome}.png")
        self.imagem = pygame.transform.scale(self.imagem, max_size_sprite)
        self.rect = self.imagem.get_rect()

        self.pos_x = 200
        if escolha == 1:
            self.pox_y = 150

        elif escolha == 2:
            self.pos_x = 350
            self.pox_y = 300

        else:
            self.pox_y = 450

        self.rect.x = self.pos_x
        self.rect.y = self.pox_y

    def desenha_personagem(self, game_window):
        game_window.blit(self.imagem, self.rect)


class Vilao1(Personagem):
    """
    Propriedades:
        hp
        atk
        def
        spd
    """

    def __init__(self, nome):
        super().__init__(nome, 1)
        self.__lp = 200
        self.__atk = 30
        self.__def = 10
        self.__spd = 30

        self.rect.x = self.pos_x = 800
        self.rect.y = self.pox_y = 300


class Vilao2(Personagem):
    """
        Propriedades:
            hp
            atk
            def
            spd
        """

    def __init__(self, nome):
        super().__init__(nome, 1)
        self.__lp = 100
        self.__atk = 10
        self.__def = 5
        self.__spd = 50

        self.rect.x = self.pos_x = 730
        self.rect.y = self.pox_y = 450

