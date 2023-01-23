
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

def funcion1():
    print('prueba')
    print(funcion1.__dict__)

if __name__ == '__main__':
    #fig = Figura()

    t = Triangulo('green','T1',23,5)
    t.lado = 10
    t.__dict__['extremo']=20
    print(t, t.calcularArea())

    print(t.__dict__)
    print(type(funcion1))
    if hasattr(funcion1, 'att'):
        print('Existe att')
    else:
        print('No existe att')
        
    funcion1.att = 100
    print(funcion1.att)
    print(funcion1.__dict__)
    funcion1()

