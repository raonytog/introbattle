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

    def __init__(self, life_poins: float, defense: int, speed: int, attack: int, name: str):
        super().__init__()
        self.life_points = life_poins
        self.max_life_points = life_poins
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


    # funcoes de desenhar
    def draw_character(self, screen: pygame.surface):
        screen.blit(self.img, self.rect)
        
    def draw_character_position(self, screen: pygame.surface, position: list):
        screen.blit(self.img, position)


    # funcoes de get
    def get_character_life_points(self) -> float:
        return self.life_points
    
    def get_character_max_life_points(self) -> float:
        return self.max_life_points
    
    def get_character_defense(self) -> int:
        return self.defense
    
    def get_character_speed(self) -> int:
        return self.speed
    
    def get_character_attack(self) -> int:
        return self.attack
    
    def get_character_name(self) -> str:
        return self.name
    
    def get_caracter_rect(self) -> pygame.rect:
        return self.rect
    
    
    # funcoes de combate
    def receive_dmg(self, damage: int) -> None:
        self.life_points -= damage * (50/(50 + self.defense))
        if self.life_points < 0:
            self.life_points = 0
        

class Meele(Character):
    def __init__(self):
        super().__init__(100, 40, 30, 30, 'meele')
        
    # def special(self):
    # dano critico


class Mage(Character):
    def __init__(self):
        super().__init__(100, 30, 50, 50, 'mage') 
        
    # def special(self):
    # dano em area com atk/2


class Ranged(Character):
    def __init__(self):
        super().__init__(100, 10, 100, 100, 'ranged')
        
    # def special(self):
    # ataca 2x seguidas
        
        
class Summoner(Character):
    def __init__(self):
        super().__init__(100, 5, 40, 150, 'summoner')
        
    # def special(self):
    # invoca um pet que causa dpt (dano por turno)
        

class Bard(Character):
    def __init__(self):
        super().__init__(100, 40, 50, 45, 'bard')
        
    # def special(self):
    # cura ul aliado
        

class EyeOfCtchulu(Character):
    def __init__(self):
        super().__init__(400, 40, 70, 20, 'eye_of_ctchulu')
        self.selected = pygame.image.load(os.path.join('imgs', 'eye_of_ctchulu_selected.png'))
        self.selected = pygame.transform.flip(self.selected, False, True)
        self.selected = pygame.transform.rotate(self.selected, 135)

        
    def get_selected_img(self):
        return self.selected
    
    # def special(self):
    # tira um personagem de campo
        

class DukeFisheron(Character):
    def __init__(self):
        super().__init__(200, 10, 150, 100, 'duke_fishron')
        self.selected = pygame.image.load(os.path.join('imgs', 'duke_fishron_selected.png'))
        self.selected = pygame.transform.flip(self.selected, True, False)
        
    def get_selected_img(self):
        return self.selected
    # def special(self):
    # dano em area atk/3 

def is_player_defeated(character_list: list[Character]) -> bool:
    for char in character_list:
        if char.get_character_life_points() > 0:
            return False
        
    return True

def is_player_winner(enemy_list: list[Character]) -> bool:
    for enemy in enemy_list:
        if enemy.get_character_life_points() > 0:
            return False
        
    return True
