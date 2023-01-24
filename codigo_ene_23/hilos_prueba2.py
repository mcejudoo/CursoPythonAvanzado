"""
Comprobar como se corrompe la memoria cuando 2 hilos comparten una variable
sin mecanismos de sincronización y luego con sincronización
"""

from threading import Thread, Lock

contador = 0
contador2 = 0
iteraciones = 1000000

def sumar():
    global contador

    for i in range(iteraciones):
        contador += 1

def sumar2(mutex):
    global contador2

    for i in range(iteraciones):
        mutex.acquire()
        contador2 += 1
        mutex.release()

def restar():
    global contador

    for i in range(iteraciones):
        contador -= 1

def restar2(mutex):
    global contador2

    for i in range(iteraciones):
        with mutex:
            contador2 -= 1        


if __name__=='__main__':
    h1 = Thread(target=sumar)
    h2 = Thread(target=restar)

    mutex = Lock()
    h3 = Thread(target=sumar2, args=(mutex,))
    h4 = Thread(target=restar2, args=(mutex,))

    h1.start()
    h2.start()

    h3.start()
    h4.start()

    h1.join()
    h2.join()
    h3.join()
    h4.join()

    print('Contador: ', contador)
    print('Contador2: ', contador2)