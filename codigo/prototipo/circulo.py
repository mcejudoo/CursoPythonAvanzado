from figura import Figura
from math import pi
import copy

class Circulo(Figura):

    def __init__(self, color='black', etiqueta="label", radio=5.0):
        Figura.__init__(self, color, etiqueta)
        self.radio = radio

    def calcularArea(self):
        return pi * self.radio**2

    def __str__(self):
        return self.__class__.__name__ + " " +\
              super().__str__() + " R:" + str(self.radio) + " " + str(self.calcularArea())

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    cir = Circulo()
    print(cir)
