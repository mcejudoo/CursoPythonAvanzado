"""
Patrón estrategia (de comportamiento). 
Distintas formas de ordenar una lista
"""
import abc
from random import randint
from datetime import datetime

N = 5000

class Estrategia(abc.ABC):
    @abc.abstractmethod
    def ordenar(self,L):
        pass

class Burbuja(Estrategia):
    def ordenar(self,L):
        for numPasada in range(len(L)-1,0,-1):
            for i in range(numPasada):
                if L[i]>L[i+1]:
                    temp = L[i]
                    L[i] = L[i+1]
                    L[i+1] = temp

class InsercionDirecta(Estrategia):
    def ordenar(self,L):
        for indice in range(1,len(L)):
            valorActual = L[indice]
            posicion = indice
            while posicion>0 and L[posicion-1]>valorActual:
                L[posicion]=L[posicion-1]
                posicion = posicion-1
            L[posicion]=valorActual

class EPython(Estrategia):
    def ordenar(self,L):
        L.sort()

class Contexto:

    lista = []

    def __init__(self):
        self.estrategia = None
        Contexto.lista = [randint(1,50000) for _ in range(N)]

    def ordenar(self):
        L = Contexto.lista.copy()
        t1 = datetime.now()
        self.estrategia.ordenar(L)
        t2 = datetime.now()
        print("Tiempo para: ", self.estrategia.__class__.__name__, t2-t1)

estrategias = [c() for c in Estrategia.__subclasses__()]
for e in estrategias:
    c = Contexto() 
    c.estrategia = e       
    c.ordenar()


