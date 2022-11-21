"""
Pruebas para crear clases
"""

from figura import Figura
from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo

L = Figura.__subclasses__()
objetos = [c() for c in L]
for obj in objetos:
    print(obj)

clases = [obj.__class__.__name__ for obj in objetos]    
print(clases)

for c in clases:
    s = "{}()".format(c)
    obj = eval(s)
    print(obj)

    s2 = f"{c}()"
    obj2 = eval(s2)
    print(obj2)

