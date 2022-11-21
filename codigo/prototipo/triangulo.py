from figura import Figura

class Triangulo(Figura):
    
    def __init__(self, color='black', etiqueta='triangulo', base=2.5, altura=8.0):
        Figura.__init__(self, color, etiqueta)
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base * self.altura / 2
	    
    def __str__(self):
        return self.__class__.__name__ + " " +\
              super().__str__() + " base: " + str(self.base) + " altura: " + str(self.altura) + \
                " " + str(self.calcularArea())