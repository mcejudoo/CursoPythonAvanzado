"""
Generar dos hilos heredando de la clase Thread.
"""

from threading import Thread
from random import randint
from time import sleep

class Mensajes(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print('mensaje: ', (i+1))
            sleep(randint(0,2))
        print('Termina hilo Mensajes')

class Aleatorio(Thread):

    def __init__(self, n, tope):
        Thread.__init__(self)
        self.n = n
        self.tope = tope

    def run(self):
        for i in range(self.n):
            print('aleatorio: ', randint(0,self.tope))
            sleep(randint(0,2))
        print('Termina hilo Aleatorio')

if __name__=='__main__':
    mensajes = Mensajes(10)
    aleatorio = Aleatorio(15,100)

    mensajes.start()
    aleatorio.start()

    mensajes.join()
    aleatorio.join()

    print('Main termina')

    