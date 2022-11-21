
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

    def cumple(self):
        self.edad += 1


class Guia(Persona):

    def __init__(self,nombre="", edad=0, altura=0,ambito='',idiomas=[]):
        Persona.__init__(self, nombre,edad,altura)
        self.ambito=ambito
        self.idiomas=idiomas

    def __str__(self):
        return Persona.__str__(self)+" "+self.ambito+" ["+ ",".join(self.idiomas)+"]"

    def hablar(self, otro=None):
        if otro==None:
            Persona.hablar(self)
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)
            i = c1 & c2
            if len(i) > 0:
                print(self.nombre,'y',otro.nombre,'hablan en'," o ".join(i))
            else:
                raise ValueError('No coinciden en un idioma')

class Empleado(Persona):
    pass

class Profesor(Persona):
    pass

if __name__ == '__main__':
    g1 = Guia('Sara',34,1.7,'N',['ingles','frances'])    
    g2 = Guia('Pedro',37,1.67,'L',['italiano','frances'])    
    g1.hablar(g2)
    print(g1)
    g1.cumple()
    print(g1)
    print('g1 isinstance Persona:', isinstance(g1, Persona))
    print('g1 isinstance Guia:', isinstance(g1, Guia))
    print(issubclass(Guia, Persona))
    print(issubclass(g1.__class__, Persona))
    L = [c.__name__ for c in Persona.__subclasses__()]
    print(L)

