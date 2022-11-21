

class Persona:
    """
    Clase persona con sus propiedades y metodos
    """

    def __init__(self, nombre="", edad=0, altura=0):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura

    def __str__(self):
        # Se liga a la función str()
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        # Se liga a la función: repr()
        return str(self)

    def __lt__(self, other):
        return self.edad < other.edad    

    def hablar(self, otro=None):
        if otro:
            print(self.nombre, "habla con", otro.nombre)
        else:
            print(self.nombre, "habla solo")

    """
    def __del__(self):
        # Se liga con la función del de Python
        print('Se borra ',self.nombre)
    """

    def cumple(self):
        self.edad += 1


