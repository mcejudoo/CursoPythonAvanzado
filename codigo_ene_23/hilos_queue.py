"""
Descargar 100 ficheros  de un servidor con N hilos
Colocar los números en una Queue y luego ordenarlos o grabarlos en un fichero.
"""

import urllib.request as urllib2
from queue import Queue
from threading import Thread

N_hilos = 4
N_files = 100


class Download(Thread):

    def __init__(self, q, ini, fin):
        nombre = f"thread_{ini}_{fin}"
        Thread.__init__(self, name=nombre)
        self.q = q
        self.ini = ini
        self.fin = fin

    def run(self):
        print('Inicio:', self.getName(), self.ini, self.fin)

        for i in range(self.ini, self.fin):
            try:
                url = f"http://localhost:8000/fich{i}.txt"
                numero = self.descargaURL(url)
                print(self.getName(), url, numero)
            except Exception as e:
                print(e)


    def descargaURL(self,url):
        f = None
        numero = None
        
        try:
            f = urllib2.urlopen(url)                
            numero = int(f.read())
            print (numero)
            
        except Exception as e:
            print("ERROR: ", e)
            raise e
            
        finally:
            if f != None: f.close()
            return numero

if __name__=='__main__':
    hilos = []
    q = Queue()

    numFich = N_files // N_hilos
    for i in range(0, N_files, numFich):
        ini = i
        fin = ini+numFich
        hilo = Download(q, ini, fin)
        hilo.start()
        hilos.append(hilo)        

    for h in hilos:
        h.join()

    # Han terminado todos de descargar los 100 ficheros.



