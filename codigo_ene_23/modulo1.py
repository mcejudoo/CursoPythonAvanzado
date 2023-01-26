'''
Created on 26-ene-2023

@author: Anton
'''

from java.util import ArrayList, Random
from random import randint
from es.curso.objetos import Persona, Direccion

class Grupo:
    
    def __init__(self, persona):
        self.grupo = [persona]
        
    def add(self, *personas):
        self.grupo.extend(personas)
    
    def imprimir(self):
        print('Grupo')
        for i in self.grupo:
            print(i)

if __name__ == '__main__':
    r = Random(123)
    for i in range(10):
        print(r.nextInt())
    
    col = ArrayList()
    for i in range(10):
        col.add(i)
        
    print(col)
    print(type(col))
    
    L = list(col)
    print(L)
    
    L = [randint(1,100) for _ in range(10)]
    print(L)
    
    p0 = Persona("Andres","Garcia",44, Direccion('Salamanca',12))
    
    p1 = Persona("Juan","Perez",34, Direccion('Salamanca',12))
    print(p1)
    p1.apellidos = "Sanz"
    print(p1)
    #print(p1.__dict__)
    
    p2 = Persona("Ana","Rodriguez",37, Direccion('Salamanca',12))
    personas = [p1, p2]
    for p in personas:
        print(p)
        
    print(personas)
    g = Grupo(p0)
    g.add(p1,p2)
    g.imprimir()
    
    
    