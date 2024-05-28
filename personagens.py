import pygame
import os

WIDTH, HEIGHT = 1024, 728

hero_positions = [(100, 500), (250, 500), (400, 500)]
vilain_positions = [(700, 500), (800, 500)]


class Personagem(pygame.sprite.Sprite):
    """
        // stats
        life_points: pontos de vida
        defense: pontos de defesa
        speed: pontos de velocidade
        attack: pontos de ataque

        // self
        name: character name
        rect: retangulo de atuacao do personagem
        img: sprite do personagem
        pos: posicao na tela (x, y)
    """

    def __init__(self, name, life_points, defense, speed, attack, nesm_chooise, is_hero):
        super().__init__()
        self.life_points = life_points
        self.defense = defense
        self.speed = speed
        self.attack = attack
        self.name = name

        self.img = pygame.image.load(os.path.join('imgs', f"{self.name}.png"))
        self.rect = self.img.get_rect()

        if is_hero is True:
            self.position = hero_positions[nesm_chooise-1]

        else:
            self.position = vilain_positions[nesm_chooise-1]

        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def draw_character(self, screen):
        screen.blit(self.img, self.rect)

    def get_character_life_points(self):
        return self.life_points
    
    def get_character_defense(self):
        return self.defense
    
    def get_character_speed(self):
        return self.speed
    
    def get_character_attack(self):
        return self.attack
    
    def get_character_name(self):
        return self.name
    
    def get_caracter_rect(self):
        return self.rect

