"""
Ejemplo sobre carga de operadores
"""

class Punto2D:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __add__(self,other):
        return Punto2D(self.x + other.x, \
            self.y + other.y)

if __name__ == '__main__':
    p1 = Punto2D(8,4)
    print(p1)
    p2 = Punto2D(2,-4)
    print(p2)
    s = p1 + p2 # s = p1.__add__(p2)
    print(s)