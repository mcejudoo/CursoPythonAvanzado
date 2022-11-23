import threading
import queue
import random
import time

try:
	import urllib2
except ImportError:
	import urllib.request as urllib2

class Downloader(threading.Thread):
	
	def __init__(self, ini, fin, cola):
		threading.Thread.__init__(self)
		self.__ini = ini
		self.__fin = fin
		self.__cola = cola
		
	def run(self):
		for i in range(self.__ini, self.__fin+1):
			#url = "http://www.dpii.es/files/fich" + str(i) + ".txt"
			
			# Se puede arrancar el servidor en local: python -m http.server [8000]
			# por defecto, van por el puerto: 8000 --> http://localhost:8000
			url = "http://localhost:8000/fich" + str(i) + ".txt"
			print (self.getName() + " descarga " + url)
			f = urllib2.urlopen(url)                
			numero = int(f.read())
			self.__cola.put(numero)
			print (numero)
			f.close()
			


class Sorter(threading.Thread):

	def __init__(self, cola):
		threading.Thread.__init__(self)
		self.__numeros = []
		self.__cola = cola
		
	def run(self):
		while len(self.__numeros) < 100:
			numero = self.__cola.get()
			self.__numeros.append(numero)
			
		# Cuando termina, ordena y graba en un fichero:
		self.__numeros.sort()
		fich = open("coleccion.txt","w")
		for i in self.__numeros:
			fich.write(str(i)+"\n")
		fich.close()	

				

class Lanzadera(object):
	
	def __init__(self, particiones):
		self.__particiones = particiones
		self.__hilos = []
		self.__cola = queue.Queue()
		
	def lanzarHilos(self):
		n = 100 // self.__particiones
		ini = 0
		
		# Lanzar los hilos que descargan ficheros:
		for i in range(self.__particiones):
			fin = ini+n-1
			print('Lanzar hilo de',ini,fin)
			down = Downloader(ini, fin, self.__cola)			
			self.__hilos.append(down)
			ini+=n
		
		for h in self.__hilos:
			h.start()

			
		# Lanzar el hilo que ordena resultados:
		sorter = Sorter(self.__cola)
		sorter.start()
				
			

if __name__=='__main__':
	lanzadera = Lanzadera(5)
	lanzadera.lanzarHilos()
