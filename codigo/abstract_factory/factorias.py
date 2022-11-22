"""
Abstract Factory: Clases de tipo factoria
"""
import abc

class Factoria(abc.ABC):
    """
    Factoria abstracta. Mantiene un método abstracto por cada tipo de producto que tengamos
    """

    @abc.abstractmethod
    def createSmartPhone():
        pass

    @abc.abstractmethod
    def createTablet():
        pass


class FactoriaSamsung(Factoria):
    
    def createSmartPhone():
        pass

    def createTablet():
        pass


class FactoriaApple(Factoria):

    def createSmartPhone():
        pass

    def createTablet():
        pass