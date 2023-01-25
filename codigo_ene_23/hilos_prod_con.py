"""
Implementación del productor - consumidor en Python
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

BUFFER_SIZE = 10
NUM_MUESTRAS = 25

class Buffer:

    def __init__(self, mutex,semItems, semEmpty):
        self.mutex = mutex
        self.semItems = semItems
        self.semEmpty = semEmpty
        self.indC = 0
        self.indP = 0
        self.buffer = [-1] * BUFFER_SIZE

    def print(self):
        print(self.buffer)


class Productor(Thread):
    
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        for i in range(NUM_MUESTRAS):
            item = randint(0,100)
            # Necesita un hueco para colocar el item:
            self.buffer.semEmpty.acquire()

            with self.buffer.mutex:
                self.buffer.buffer[self.buffer.indP]=item
                self.buffer.indP = (self.buffer.indP+1) % BUFFER_SIZE
                print(f'{i} - P:',item, self.buffer.buffer)

            # Avisa al consumidor de que hay un nuevo item
            self.buffer.semItems.release()
            sleep(randint(0,2))

class Consumidor(Thread):
    
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        for i in range(NUM_MUESTRAS):
            
            # Necesita un item para procesar:
            self.buffer.semItems.acquire()

            with self.buffer.mutex:
                item = self.buffer.buffer[self.buffer.indC]
                self.buffer.buffer[self.buffer.indC] = -1
                self.buffer.indC = (self.buffer.indC+1) % BUFFER_SIZE
                print(f'{i} - C:',item, self.buffer.buffer)

            # Avisa al productor de que hay un nuevo hueco.
            self.buffer.semEmpty.release()
            sleep(randint(1,3))

if __name__ == '__main__':
    mutex = Lock()
    semItems = Semaphore(0)
    semEmpty = Semaphore(BUFFER_SIZE)

    buffer = Buffer(mutex, semItems, semEmpty)
    p = Productor(buffer)
    c = Consumidor(buffer)

    p.start()
    c.start()

    p.join()
    c.join()
