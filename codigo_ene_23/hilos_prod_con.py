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
        self.buffer = list()

    def print(self):
        print(self.buffer)


class Productor(Thread):
    
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        pass

class Consumidor(Thread):
    
    def __init__(self, buffer):
        Thread.__init__(self)
        self.buffer = buffer

    def run(self):
        pass

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
