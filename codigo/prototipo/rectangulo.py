from figura import Figura

class Rectangulo(Figura):
	
	def __init__(self, color='black', etiqueta='rectangulo', ancho=5.0, alto=10.0):		
		Figura.__init__(self, color, etiqueta)
		self.ancho = ancho
		self.alto = alto
		
	def __str__(self):		
		return super().__str__() + " ancho: " + str(self.ancho) + " alto: " + str(self.alto)
		
	