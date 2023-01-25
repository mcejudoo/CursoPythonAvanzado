# Ejemplo de sincronizacion con Eventos

from threading import Thread, Event
import time
import random

class Consumer(Thread):
	
	def __init__(self, items, evento):
		Thread.__init__(self)
		self.__items = items
		self.__evento = evento
		
	def run(self):
		while True:
			try:
				time.sleep(1)
				self.__evento.wait() # Espera a que le avisen
				item = self.__items.pop() # Quita un elemento de la lista
				print("Consumer quita el %d" % (item,))
			except Exception as e:
				print('error: ', e)
			
class Producer(Thread):
	
	def __init__(self, items, evento):
		Thread.__init__(self)
		self.__items = items
		self.__evento = evento
		
	def run(self):
		for i in range(10):
			time.sleep(1)
			item = random.randint(0,256)
			self.__items.append(item)
			print("Productor poner el %d" % (item,))
			self.__evento.set() # Enviar evento
			#time.sleep(2)
			self.__evento.clear() # limpiar evento
			
if __name__ == '__main__':
	evento = Event()
	items=[]
	p = Producer(items, evento)
	c = Consumer(items, evento)
	p.start()
	c.start()
	p.join()
	c.join()
	
				
							
			
	

