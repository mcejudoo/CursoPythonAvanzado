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

	def __init__(self):
		# el att de tipo Vector3D
		self.vector3D=0

# Adaptador 2: solución por herencia múltiple
class VectorPlano2(Vector2D, Vector3D):

	def __init__(self) -> None:
		Vector3D.__init__(self)