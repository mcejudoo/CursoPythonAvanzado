"""
Abstract Factory: Clases de tipo factoria
"""
import abc
from productos import *

class Factoria(abc.ABC):
    """
    Factoria abstracta. Mantiene un método abstracto por cada tipo de producto que tengamos
    """

    @abc.abstractmethod
    def createSmartPhone(self):
        pass

    @abc.abstractmethod
    def createTablet(self):
        pass


class FactoriaSamsung(Factoria):
    
    def createSmartPhone(self):
        return S20()

    def createTablet(self):
        return GalaxyS20()


class FactoriaApple(Factoria):

    def createSmartPhone(self):
        return IPhone()

    def createTablet(self):
        return IPad()