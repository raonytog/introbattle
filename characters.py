import pygame
import os

WIDTH, HEIGHT = 1024, 728
HERO_SIZE = (70, 100)

class Character(pygame.sprite.Sprite):
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

    def __init__(self, life_poins, defense, speed, attack, name):
        super().__init__()
        self.life_points = life_poins
        self.defense = defense
        self.speed = speed
        self.attack = attack
        
        self.name = name
        self.img = pygame.image.load(os.path.join('imgs', f'{name}.png'))
        
        if name == 'duke_fishron' or name == 'eye_of_ctchulu':
            if name == 'eye_of_ctchulu':
                self.img = pygame.transform.flip(self.img, False, True)
                self.img = pygame.transform.rotate(self.img, -135)
            
        else:
            self.img = pygame.transform.scale(self.img, HERO_SIZE)
            
        self.img = pygame.transform.flip(self.img, True, False)
        self.rect = self.img.get_rect()

    def draw_character(self, screen):
        screen.blit(self.img, self.rect)
        
    def draw_character_position(self, screen, position):
        screen.blit(self.img, position)

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
    
class Meele(Character):
    def __init__(self):
        super().__init__(120, 40, 30, 30, 'meele')


class Mage(Character):
    def __init__(self):
        super().__init__(100, 20, 50, 50, 'mage') 


class Ranged(Character):
    def __init__(self):
        super().__init__(80, 10, 100, 100, 'ranged')
        
        
class Summoner(Character):
    def __init__(self):
        super().__init__(80, 5, 50, 150, 'summoner')
        

class Bard(Character):
    def __init__(self):
        super().__init__(80, 40, 50, 45, 'bard')
        

class EyeOfCtchulu(Character):
    def __init__(self):
        super().__init__(400, 40, 70, 40, 'eye_of_ctchulu')
        

class DukeFisheron(Character):
    def __init__(self):
        super().__init__(170, 10, 150, 100, 'duke_fishron')

