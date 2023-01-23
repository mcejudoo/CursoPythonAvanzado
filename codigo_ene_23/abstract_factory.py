import abc

# Definir la factoría abstracta y otras dos: Apple y Samsung
class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def createSmartPhone(self):
        pass

    @abc.abstractmethod
    def createTablet(self):
        pass

class FactoryApple(AbstractFactory):

    def createSmartPhone(self):
        return IPhone('ios',5,64,'modelo 10')
    
    def createTablet(self):
        return IPad('ios',10,128,'tablet 5')

class FactorySamsung(AbstractFactory):

    def createSmartPhone(self):
        return GalaxyS7('android 8',5,64,'xxx 10')
    
    def createTablet(self):
        return GalaxyA('ios',10,128,'xx 5')


#productos
class Dispositivo():

        def __init__(self, so, ram, hd, name):
                self.__so = so
                self.__ram = ram
                self.__hd = hd
                self.__name = name

        def __str__(self):
                return self.__so + ", " + str(self.__ram) + ", " + str(self.__hd) + ", " + self.__name

##########################################################################
class SmartPhone(Dispositivo, abc.ABC):

        def __init__(self, so, ram, hd, name):
                Dispositivo.__init__(self, so, ram, hd, name)

        @abc.abstractmethod
        def call(self):
            pass

        def __str__(self):
                return "SmartPhone: " + Dispositivo.__str__(self)

class GalaxyS7(SmartPhone):

        def __init__(self, so, ram, hd, name):
                SmartPhone.__init__(self, so, ram, hd, name)

        def call(self):
            print('Llamar con GalaxyS7')

        def __str__(self):
                return "GalaxyS7: " + SmartPhone.__str__(self)

class IPhone(SmartPhone):

        def __init__(self, so, ram, hd, name):
                SmartPhone.__init__(self, so, ram, hd, name)

        def call(self):
            print('Llamar con IPhone')

        def __str__(self):
                return "Titan: " + SmartPhone.__str__(self)
 

##############################################################################        
class Tablet(Dispositivo, abc.ABC):

        def __init__(self, so, ram, hd, name):
                Dispositivo.__init__(self, so, ram, hd, name)

        @abc.abstractmethod
        def internet(self):
            pass

        def __str__(self):
                return "Tablet: " + Dispositivo.__str__(self)

class GalaxyA(Tablet):
        
        def __init__(self, so, ram, hd, name):
                Tablet.__init__(self, so, ram, hd, name)

        def internet(self):
            print('internet con GalaxyA')

        def __str__(self):
                return "Guru: " + Tablet.__str__(self)

class IPad(Tablet):
        
        def __init__(self, so, ram, hd, name):
                Tablet.__init__(self, so, ram, hd, name)

        def internet(self):
            print('internet con IPad')


        def __str__(self):
                return "Genie: " + Tablet.__str__(self)

def selectFactory(L):
    print('Seleccionar fabricante:')
    for pos, nombre in enumerate(L):
        print(pos+1, nombre)
    op = int(input('Opción: '))
    nombreClase = L[op-1]
    cadena = "{}()".format(nombreClase)
    return eval(cadena)

if __name__ == '__main__':
    L = [c.__name__ for c in AbstractFactory.__subclasses__()]    
    fact = selectFactory(L)  
    telefono = fact.createSmartPhone()
    telefono.call()

    tableta  = fact.createTablet()
    tableta.internet()
    
