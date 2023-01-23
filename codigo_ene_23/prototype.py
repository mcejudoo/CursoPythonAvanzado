"""
Patrón prototype
Editor de figuras en 2D
"""
import abc, copy

class Factoria1:
    """
    Crear los prototipos al principio
    """
    
    def __init__(self):
        """
        Crear los prototipos
        """
        pass


    def getPrototipo(self, nombreFigura):
        """
        Devuelve un clon del prototipo elegido
        """
        pass


class Factoria2:
    """
    Crear los prototipos bajo demanda
    """
    pass



class Prototipo(abc.ABC):
	
	def __init__(self, etiqueta='', color='black'):
		self.etiqueta = etiqueta
		self.color = color
				
	def __str__(self):
		return "etiqueta: " + self.etiqueta + " color: " + self.color
			
	@abc.abstractmethod
	def clone(self):
		pass
	
	
class Circulo(Prototipo):
	
	def __init__(self, etiqueta='circulo', color='black', radio=5.0):
		Prototipo.__init__(self, etiqueta, color)
		self.radio = radio
		
	def __str__(self):		
		return super().__str__() + " radio: " + str(self.radio)
			
	def clone(self):
		return copy.copy(self)
			
		
	
class Rectangulo(Prototipo):
	
	def __init__(self, etiqueta='rectangulo', color='black', ancho=5.0, alto=10.0):		
		Prototipo.__init__(self, etiqueta, color)
		self.ancho = ancho
		self.alto = alto
		
	def __str__(self):		
		return super().__str__() + 	" ancho: " + str(self.ancho) + " alto: " + str(self.alto)
	
	def clone(self):
		return copy.copy(self)
	
	
class Triangulo(Prototipo):
	
	def __init__(self, etiqueta='triangulo', color='black', base=2.5, altura=8.0):		
		Prototipo.__init__(self, etiqueta, color)
		self.base = base
		self.altura = altura
		
	def __str__(self):		
		return super().__str__() + 	" base: " + str(self.base) + " altura: " + str(self.altura)
			
	
	def clone(self):
		return copy.copy(self)
	