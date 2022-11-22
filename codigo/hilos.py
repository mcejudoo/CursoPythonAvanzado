"""
Creación de hilos utilizando la clase threading.Thread.
Comprobar que ocurre cuando no utilizamos mecanismos de sincronización
"""

from threading import Thread

cont = 0
N = 100000

class Sumador(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        global cont
        for i in range(self.n):
            cont += 1

class Restador(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        global cont
        for i in range(self.n):
            cont -= 1

if __name__ == '__main__':
    s = Sumador(N)            
    r = Restador(N)

    s.start()
    r.start()

    r.join()
    s.join()

    print('Cont: ', cont)
