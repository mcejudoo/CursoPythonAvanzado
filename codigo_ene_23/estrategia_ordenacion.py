"""
Patrón estrategia
"""
import abc
from datetime import datetime
from random import randint

class Contexto:

    def __init__(self):
        self.algoritmo=None

    @staticmethod
    def cronometrar(ClaseEstrategia):
        """
        Mide los tiempo de ejecución de todas las estrategias
        """
        L = [randint(0,10000) for _ in range(20000)]
        for c in ClaseEstrategia.__subclasses__():
            L2 = L.copy()
            obj = c()
            t1 = datetime.now()
            obj.ordenar(L2)
            t2 = datetime.now()
            print('Clase ', c.__name__)
            print('Tiempo de ordenación: ', t2-t1)

class Estrategia:

    @abc.abstractmethod
    def ordenar(self, L):
        pass

class EstrategiaPy(Estrategia):

    def ordenar(self, L):
        L.sort()


class EstrategiaBurbuja(Estrategia):

    def ordenar(self,L):
        for numPasada in range(len(L)-1,0,-1):
            for i in range(numPasada):
                if L[i]>L[i+1]:
                    temp = L[i]
                    L[i] = L[i+1]
                    L[i+1] = temp


class EstrategiaPorInsercion(Estrategia):

    def ordenar(self,L):
        for indice in range(1,len(L)):

            valorActual = L[indice]
            posicion = indice

            while posicion>0 and L[posicion-1]>valorActual:
                L[posicion]=L[posicion-1]
                posicion = posicion-1

            L[posicion]=valorActual


if __name__=='__main__':
    Contexto.cronometrar(Estrategia)



