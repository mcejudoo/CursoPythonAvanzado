import math, abc

class Vector3D:
	
	def __init__(self,x=0,y=0,z=0):
		self.__x = x
		self.__y = y
		self.__z = z
		
	def getX(self):
		return self.__x
		
	def getY(self):
		return self.__y

	def getZ(self):
		return self.__z
				
	def productoEscalar(self, vector):
		return self.__x * vector.__x + self.__y * vector.__y + self.__z * vector.__z
		
	def norma(self):
		return math.sqrt(self.__x**2+self.__y**2+self.__z**2)
		
	def __str__(self):
		return str(self.__x)+","+str(self.__y)+","+str(self.__z)
		
		
class Vector2D(abc.ABC):
	
	@abc.abstractmethod
	def getAbcisa(self): 
		pass
	
	@abc.abstractmethod	
	def getOrdenada(self):
		pass
		
	@abc.abstractmethod
	def prod(self, v):
		pass
		
	@abc.abstractmethod
	def magnitud(self):
		# La norma del vector
		pass

# Adaptador 1: solución por composición: wrapper
class VectorPlano1(Vector2D):

	def __init__(self, x=0, y=0):
		# el att de tipo Vector3D
		self.__vector3D=Vector3D(x,y,0)

	def getAbcisa(self): 
		return self.__vector3D.getX()
		
	def getOrdenada(self):
		return self.__vector3D.getY()
			
	def prod(self, v):
		aux3D = Vector3D(v.getAbcisa(), v.getOrdenada(), 0)
		return self.__vector3D.productoEscalar(aux3D)
			
	def magnitud(self):
		# La norma del vector
		return self.__vector3D.norma()

	def __str__(self):
		return str(self.getAbcisa())+", "+str(self.getOrdenada())

# Adaptador 2: solución por herencia múltiple
class VectorPlano2(Vector2D, Vector3D):

	def __init__(self, x=0, y=0):
		Vector3D.__init__(self, x, y, 0)

	def getAbcisa(self): 
		return self.getX()
		
	def getOrdenada(self):
		return self.getY()

	def prod(self, v):
		aux3D = Vector3D(v.getAbcisa(), v.getOrdenada(), 0)
		return Vector3D.productoEscalar(self, aux3D)
			
	def magnitud(self):
		# La norma del vector
		return Vector3D.norma(self)

	def __str__(self):
		return str(Vector3D.getX(self))+", "+str(Vector3D.getY(self))


if __name__ == '__main__':
	v1 = VectorPlano2(2,6)		
	v2 = VectorPlano2(5,6)

	print(v1)
	print(v2)
	print(v1.prod(v2))