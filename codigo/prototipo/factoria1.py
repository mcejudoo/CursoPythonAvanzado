"""
Implementación de la fábrica de prototipos. 
En esta versión se crean todos los prototipos 
al inicio.
"""

from figura import Figura
from rectangulo import Rectangulo
from triangulo import Triangulo
from circulo import Circulo

class Factoria1:
    
    def __init__(self):
        # Creamos un objeto de cada subclase de Figura:
        L = [c() for c in Figura.__subclasses__()]

        # Construimos un diccionario con el nombre de la clase  en minúsculas y como el valor el objeto
        self.prototipos = {c.__class__.__name__.lower():c for c in L}

    def getPrototipo(self, nombre):
        nombre = nombre.lower()
        
        if nombre not in self.prototipos:
            raise ValueError("No existe prototipo: "+nombre)
        else:
            return self.prototipos[nombre].clone()
        
    def print(self):
        print('Catalogo de prototipos')
        for k,v in self.prototipos.items():
            print("clave:",k,' -> ',v)

if __name__ == '__main__':
    fact = Factoria1()
    fact.print() 
    circulo = fact.getPrototipo('circulo')           
    circulo.color = 'yellow'
    circulo.etiqueta = 'circulo1'
    print(circulo)

    circulo2 = fact.getPrototipo('circulo') 
    print(circulo2)


