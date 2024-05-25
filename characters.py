class Characters:
    """
    Propriedades:
        __pv = pontos de vida atual
        __atk = ataque
        __def = defesa
        __spd = velocidade
    """

    def __init__(self, vida, ataque, defesa, speed):
        self.__lp = vida
        self.__atk = ataque
        self.__def = defesa
        self.__spd = speed

    def get_pv(self):
        return self.__lp

    def get_atk(self):
        return self.__atk

    def get_def(self):
        return self.__def

    def get_spd(self):
        return self.__spd

    def attack_turn(self, defesa_inimiga):
        return self.__atk * (50/(50 + defesa_inimiga))

    def defense_turn(self):
        return self.__def * 2
