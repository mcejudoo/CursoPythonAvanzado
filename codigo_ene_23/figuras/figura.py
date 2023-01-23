
import abc

class Figura(abc.ABC):

    def __init__(self, color='red', etiqueta=''):
        self.color = color
        self.etiqueta = etiqueta

    def __str__(self):
        return self.color+" "+self.etiqueta

    @abc.abstractmethod
    def calcularArea(self):
        pass

class Triangulo(Figura):

    def __init__(self,color='red', etiqueta='',base=0,altura=0):
        # 1ª forma:
        #Figura.__init__(self,color, etiqueta)

        # 2ª forma:
        super().__init__(color, etiqueta)

        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura / 2

    def __str__(self):
        return Figura.__str__(self)+" "+str(self.base)+" "+str(self.altura)


if __name__ == '__main__':
    #fig = Figura()

    t = Triangulo('green','T1',23,5)
    print(t, t.calcularArea())
