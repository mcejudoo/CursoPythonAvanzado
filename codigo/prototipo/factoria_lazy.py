"""
Implementación de la fábrica de prototipos. 
En esta versión se crean los prototipos
bajo demanda.
Se pide un prototipo si no existe, se crea.
"""
from figura import Figura
from rectangulo import Rectangulo
from triangulo import Triangulo
from circulo import Circulo

class FactoriaLazy:

    def __init__(self):
        self.prototipos = {c.__name__.lower():None for c in Figura.__subclasses__()}
       
    def getPrototipo(self, nombre):
        nombre = nombre.lower()

        if nombre not in self.prototipos:
            raise ValueError("No existe prototipo: "+nombre)

        elif self.prototipos[nombre] == None:  
            print('Se crea el prototipo: ', nombre)          
            nombreClase = nombre.capitalize()
            self.prototipos[nombre] = eval(f"{nombreClase}()")

        return self.prototipos[nombre].clone()

    def print(self):
        print('Catalogo de prototipos')
        for k,v in self.prototipos.items():
            print("clave:",k,' -> ',v)

if __name__ == '__main__':
    fact = FactoriaLazy()
    fact.print() 
    
    circulo = fact.getPrototipo('circulo')           
    circulo.color = 'yellow'
    circulo.etiqueta = 'circulo1'
    print(circulo)

    circulo2 = fact.getPrototipo('circulo') 
    print(circulo2)
    fact.print()
    