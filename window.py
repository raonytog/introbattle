class Window:
    __width = 0             # largura
    __height = 0            # altura
    __color = (0, 0, 0)     # cor

    def __init__(self, largura, altura):
        self.__width = largura
        self.__height = altura

    def return_size(self):
        return self.__width, self.__height
    
    def return_color(self):
        return self.__color
