"""
Colecciones: deque, default_dict y namedtuple
"""

from collections import namedtuple, defaultdict, deque

def testDeque():
    L = list('hola que tal')
    d = deque(L)
    #d.appendleft(list('hoy'))
    d.extendleft(list('hoy'))
    d.rotate(-5)
    print(d)

def testCC():
    Cuenta = namedtuple('Cuenta',['sucursal','entidad','dc','numero'])
    cc1 = Cuenta("2000","4500","99","12345678")
    print(cc1, type(cc1))
    print(cc1.dc)
    print(cc1._asdict())

if __name__ == '__main__':
    #testDeque()
    testCC()