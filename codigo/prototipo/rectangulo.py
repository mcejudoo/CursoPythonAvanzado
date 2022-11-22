from figura import Figura

class Rectangulo(Figura):
    
    def __init__(self, color='black', etiqueta='rectangulo', ancho=5.0, alto=10.0):		
        Figura.__init__(self, color, etiqueta)
        self.ancho = ancho
        self.alto = alto
        
    def calcularArea(self):
        return self.ancho * self.alto
	    
    def __str__(self):
        return self.__class__.__name__ + " " +\
              super().__str__() + " ancho: " + str(self.ancho) + " alto: " + str(self.alto) + \
                " " + str(self.calcularArea())

    def clone(self):        
        return Rectangulo(**self.__dict__)


if __name__ == '__main__':
    r = Rectangulo()
    r2 = r.clone()        
    print(r2)
		
	