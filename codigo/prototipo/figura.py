"""
Clase Abstracta que representa una figura
"""

import abc
from abc import ABC

class Figura(ABC):

    def __init__(self, color='black', etiqueta="label"):
        self.color = color
        self.etiqueta = etiqueta

    def __str__(self):
        return self.color + " " + self.etiqueta

    @abc.abstractmethod
    def calcularArea(self):
        pass

if __name__ == '__main__':
    pass

    """ Ojo no se puede instanciar: es abstracta
    fig = Figura(etiqueta='Prueba1')
    print(fig)
    """