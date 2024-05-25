class Characters:
    __pv = 0
    __atk = 0
    __def = 0
    __spd = 0

    def __init__(self, vida, ataque, defesa, speed):
        self.__pv = vida
        self.__atk = ataque
        self.__def = defesa
        self.__spd = speed

    def retorna_vida(self):
        return self.__pv

    def retorna_ataque(self):
        return self.__atk

    def retorna_defesa(self):
        return self.__def

    def retorna_velocidade(self):
        return self.__spd

    def ataca(self, defesa_inimiga):
        return self.__atk * (50/(50 + defesa_inimiga))

    def defende(self):
        return self.__def * 2
