"""
Creación de hilos utilizando la clase threading.Thread.
Utilizamos un mecanismo de sincronización: Lock  (semáforo binario)
"""

from threading import Thread, Lock

cont = 0
N = 1000000

class Sumador(Thread):

    def __init__(self, n, cerrojo):
        Thread.__init__(self)
        self.n = n
        self.cerrojo = cerrojo

    def run(self):
        global cont
        for i in range(self.n):
            self.cerrojo.acquire()
            cont += 1
            self.cerrojo.release()

class Restador(Thread):

    def __init__(self, n, cerrojo):
        Thread.__init__(self)
        self.n = n
        self.cerrojo = cerrojo

    def run(self):
        global cont
        for i in range(self.n):
            with self.cerrojo:
                cont -= 1

if __name__ == '__main__':
    cerrojo = Lock()
    s = Sumador(N, cerrojo)            
    r = Restador(N, cerrojo)

    s.start()
    r.start()

    r.join()
    s.join()

    print('Cont: ', cont)
