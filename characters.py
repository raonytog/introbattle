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
        desc: descricao do personagem
        special_desc = descricao do especial
    """

    def __init__(self, life_poins: float, defense: int, speed: int, attack: int, name: str):
        super().__init__()
        # descricoes
        self.desc = ""
        self.special_desc = ""
        
        # status
        self.life_points = life_poins
        self.max_life_points = life_poins
        self.defense = defense
        self.speed = speed
        self.attack = attack
        self.name = name
        
        
        self.pos = [0, 0]
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
    
    def get_caracter_pos(self) -> int:
        return self.pos
        
    def get_caracter_pos_x(self) -> int:
        return self.pos[0]
        
    def get_caracter_pos_y(self) -> int:
        return self.pos[1]
    
    # setters
    def set_character_post(self, position: list[2]) -> None:
        self.pos = position
        
    def give_character_life_points(self, bonus_life: int) -> None:
        self.life_points += bonus_life
        if self.life_points > self.max_life_points:
            self.life_points = self.max_life_points
        
    def receive_dmg(self, damage: int) -> None:
        # verifica se eh possivel receber dano
        if self.life_points > 0:
            self.life_points -= damage * (50/(50 + self.defense))
            
        # correcao de vida
        if self.life_points < 0:
            self.life_points = 0
            
    # logical
    def is_character_alive(self) -> bool:
        if self.life_points > 0:
            return True
        
        return False

class Meele(Character):
    def __init__(self):
        super().__init__(100, 40, 30, 40, 'meele')
        self.desc = "Uma aventureira que adora combate"
        self.special_desc = "Dano explosivo unitário automultilador"
        
    # Da um dado critico no inimio. Caso mate, o usuario tambem morre
    def sp_atk(self, enemy: Character, screen, enemy_list, ally_list):
        enemy.receive_dmg(4 * self.get_character_attack())
        self.receive_dmg(self.attack * 0.2)
        if enemy.life_points < 0:
            self.life_points = 0
            
            
    def sp_def(self):
        self.defense = 50

class Mage(Character):
    def __init__(self):
        super().__init__(100, 30, 50, 50, 'mage')
        self.desc = "Um velho sábio do bosque"
        self.special_desc = "Dano em área"
        
    # causa dano em área
    def sp_atk(self, enemy_list: list[Character]):
        for enemy in enemy_list:
            enemy.receive_dmg(self.get_character_attack())
            
    def sp_def(self):
        self.defense = 40
        

class Ranged(Character):
    def __init__(self):
        super().__init__(100, 10, 100, 100, 'ranged')
        self.desc = "Um metido arqueiro e escritor"
        self.special_desc = "Reduz a defesa ao inimigo, causando dano crítico"
        
    # causa um ataque critico e diminui a defesa do inimigo em 25%

    def sp_atk(self, enemy: Character):
        enemy.receive_dmg(self.get_character_attack()*2)
        enemy.defense = enemy.get_character_defense() * 0.75
        
    def sp_def(self):
        self.defense = 20
        
class Summoner(Character):
    def __init__(self):
        super().__init__(100, 5, 40, 100, 'summoner')
        self.desc = "?"
        self.special_desc = "Amigos morcegos atacam os inimigos"
    
    # cria morcegos que atacam os inimigos
    def sp_atk(self, enemy_list: list[Character]):
        # ataque dos morcegos
        for enemy in enemy_list:
            enemy.receive_dmg(20)
            
        # attk do aliado no primeiro inimigo vivo
        if enemy_list[0].is_character_alive():
            enemy_list[0].receive_dmg(self.get_character_attack())
            
        elif enemy_list[1].is_character_alive():
            enemy_list[1].receive_dmg(self.get_character_attack())
            
    def sp_def(self):
        self.defense = 10

class Bard(Character):
    def __init__(self):
        super().__init__(100, 30, 50, 45, 'bard')
        self.desc = "Uma princesa que adora músicas"
        self.special_desc = "Cura seus aliados"
        
    # cura 65% da vida do aliado escolhido
    def sp_atk(self, ally: Character):
        print(ally.get_character_life_points())
        ally.give_character_life_points(ally.get_character_max_life_points() * 0.65)
        print(ally.get_character_life_points())
        
        
    def sp_def(self):
        self.defense = 40
        

class EyeOfCtchulu(Character):
    def __init__(self):
        super().__init__(200, 40, 70, 20, 'eye_of_ctchulu')
        self.selected = pygame.image.load(os.path.join('imgs', 'eye_of_ctchulu_selected.png'))
        self.selected = pygame.transform.flip(self.selected, False, True)
        self.selected = pygame.transform.rotate(self.selected, 135)

    def get_selected_img(self):
        return self.selected

class DukeFisheron(Character):
    def __init__(self):
        super().__init__(200, 10, 150, 20, 'duke_fishron')
        self.selected = pygame.image.load(os.path.join('imgs', 'duke_fishron_selected.png'))
        self.selected = pygame.transform.flip(self.selected, True, False)
        
    def get_selected_img(self):
        return self.selected