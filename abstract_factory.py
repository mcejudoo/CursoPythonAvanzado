import abc

# Definir la factoría abstracta y otras dos: Apple y Samsung

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

        def __str__(self):
                return "GalaxyS7: " + SmartPhone.__str__(self)

class Titan(SmartPhone):

        def __init__(self, so, ram, hd, name):
                SmartPhone.__init__(self, so, ram, hd, name)

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

class Guru(Tablet):
        
        def __init__(self, so, ram, hd, name):
                Tablet.__init__(self, so, ram, hd, name)

        def __str__(self):
                return "Guru: " + Tablet.__str__(self)

class Genie(Tablet):
        
        def __init__(self, so, ram, hd, name):
                Tablet.__init__(self, so, ram, hd, name)

        def __str__(self):
                return "Genie: " + Tablet.__str__(self)

      