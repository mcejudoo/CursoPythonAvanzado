
class Idioma:
	
	def __init__(self, lengua='es'):
		self.lengua = lengua
		self.palabras = dict()
		self.__cargaFichero()

	def __cargaFichero(self):
		f = None
		try:
			nombreFich = 'idiomas\\'+self.lengua+'.txt'
			f = open(nombreFich, 'r')
			while True:
				try:
					linea = f.readline()
					linea = linea.rstrip('\r\n')
					print(linea)
					if not linea: break					
					L = linea.split('=')
					self.palabras[L[0]]=L[1]
					#t = linea.partition('=')
					#self.palabras[t[0]]=t[2]
										
				except Exception as e:
					print('Error: ', e)
					
		except IOError as e:
			raise Exception('Idioma no soportado...')
			
		except Exception as e:
			raise Exception(str(e))	
			
		finally:
			if f != None: f.close()

	def getString(self,key):
		if key in self.palabras:
			return self.palabras[key]
		else:
			raise Exception('La clave no existe en el fichero')
			
#########################################################################################################################################################			

# Con Clase:

class Singleton:
		
	__idioma = None
	__palabras = None
	
	@staticmethod
	def getInstance(idioma="es"):
		if Singleton.__idioma != idioma:
			# Se carga el idioma:		
			Singleton.__idioma = idioma			
			Singleton.__cargaFichero()
			
		
		return Singleton.__palabras
							
								
	@staticmethod		
	def __cargaFichero():
		f = None
		Singleton.__palabras = dict()
		try:
			print('Carga fichero con: ', Singleton.__idioma)
			nombreFich = 'idiomas\\'+Singleton.__idioma+'.txt'
			f = open(nombreFich, 'r')
			while True:
				try:
					linea = f.readline()
					linea = linea.rstrip('\r\n')
					#print(linea)
					if not linea: break					
					L = linea.split('=')
					Singleton.__palabras[L[0]]=L[1]					
										
				except Exception as e:
					print('Error: ', e)
					
		except IOError as e:
			raise Exception('Idioma no soportado...')
			
		except Exception as e:
			raise Exception(str(e))	
			
		finally:
			if f != None: f.close()			



#########################################################################################################################################################

if __name__=='__main__':
	
	print(Singleton.getInstance()['facebook'])
	print(Singleton.getInstance('es')['instagram'])
	print(Singleton.getInstance('en')['inicio'])
