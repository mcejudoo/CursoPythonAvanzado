"""
Implementación de las clases Categoria y Producto
"""
import sqlite3 as dbapi
from os.path import isfile

path = "../practicas/avanzado2/BBDD/empresa3.db"

class Categoria:

    __num_instancias = 0

    def __init__(self,id=0,nombre=""):
        self.id = id
        self.nombre = nombre
        Categoria.__num_instancias+=1

    @staticmethod
    def getNumInstancias():
        return Categoria.__num_instancias

    def __del__(self):
        Categoria.__num_instancias-=1

    def __str__(self):
        return str(self.id) + " " + self.nombre

    def __repr__(self):
        return str(self)

    def __lt__(self, otro):
        return self.id < otro.id

    def __eq__(self,o):
        return self.id==o.id and self.nombre==o.nombre

    def print(self):
        print(self.id, self.nombre)

    """
    def __del__(self):
        print('Se borra: ',self.nombre)
    """

class Producto:
    
    def __init__(self,id=0,nombre="",cat=None, precio=0.0, exis=0):
        self.id = id
        self.nombre = nombre
        self.cat = cat
        self.precio = precio
        self.exis = exis

    def __str__(self):
        return str(self.id)+" "+self.nombre+" "+str(self.cat)+" "+str(self.precio)+" "+str(self.exis)

    def __repr__(self):
        return str(self)

    def getTupla(self):
        return (self.id,self.nombre,self.cat.id,self.precio,self.exis)

    def getTupla2(self):
        return (self.nombre,self.cat.id,self.precio,self.exis,self.id)
    
class BaseDatos:
    """
    Implementar las operaciones CRUD: Create, Read, Delete y Update con la entidad Producto
    """    
    def __init__(self, path):
        
        if not isfile(path):
            raise ValueError("No se encuentra el fichero: "+path)
        else:
            self.con = dbapi.connect(path)
            print('Base de datos abierta!')

    def __getProducto(self, t):
        tcat = t[2:4]
        cat = Categoria(*tcat)
        #tprod = t[:2],cat+t[4:]
        prod = Producto(t[0],t[1],cat,t[4],t[5])
        return prod

    def select(self, cat=None):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idprod, p.nombre as producto, c.id as idcat, c.nombre as categoria,
            p.precio, p.existencias from productos p inner join categorias c
            on p.idcategoria = c.id"""
            if cat != None:
                sql += " where c.nombre=?"
                cur.execute(sql, (cat,))
            else:
                cur.execute(sql)
            
            return [self.__getProducto(t) for t in cur.fetchall()]
                          
        except Exception as e:
            raise e
        finally:
            if cur: cur.close()

    def __ejecutar(self, sql, t):
        cur = None
        try:
            cur.execute(sql,t)
        except Exception as e:
            raise e
        finally:
            if cur: cur.close()

    def create(self, p):
        sql = "insert into productos(id, nombre, idcategoria, importe, existencias) values(?,?,?,?,?)"
        self.__ejecutar(sql, p.getTupla())

    def delete(self, id):
        sql = "delete from productos where id=?"
        self.__ejecutar(sql, (id,))

    def update(self, p):
        sql = "update productos set nombre=?, idcategoria=?, importe=?, existencias=? where id=?"
        self.__ejecutar(sql, p.getTupla2())

    def read(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idprod, p.nombre as producto, c.id as idcat, c.nombre as categoria,
            p.precio, p.existencias from productos p inner join categorias c
            on p.idcategoria = c.id
            where p.id = ?"""
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t == None:
                raise ValueError('No se encuentra el producto: ',str(id))
            else:
                return self.__getProducto(t)
        except Exception as e:
            raise e
        finally:
            if cur: cur.close()

    
    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()
            print('Base de datos cerrada!')

class Almacen:

    def __init__(self, productos):
        self.productos=productos

    def __len__(self):
        return len(self.productos)

def testAlmacen():
    try:
        bd = BaseDatos(path)       
        L = bd.select('bebidas')
        almacen = Almacen(L)
        print(f'Almacen con {len(almacen)} productos')

        for i in almacen:
            print(i)
            
    except Exception as e:
        print(e.__class__.__name__, e) 

def testBaseDeDatos():
    try:
        bd = BaseDatos(path)
        prod = bd.read(5)
        print(prod)
        L = bd.select('bebidas')
        print(L)
        print()
    except Exception as e:
        print(e.__class__.__name__, e)

def testCategoria():
    cat = Categoria(2,"Cine")
    L = [Categoria(nombre='Teatro'),Categoria(9,'Viajes'),cat]
    if L[0] == L[1]:
        print('iguales')
    else:
        print('No iguales')
    print(L)
    L.sort()
    print(L)
    L.sort(key=lambda x:x.nombre)
    print(L)
    print(cat, str(cat), cat.__str__())
    print(cat.__dict__)
    cat.__dict__['descripcion']='descripcion de la cat'
    cat.coste = 450
    print(cat.__dict__)
    print([obj.__dict__ for obj in L])

def testCategoriaStatic():
    print('NumCat:',Categoria.getNumInstancias())
    c1 = Categoria(1,'a')
    c2 = Categoria(2,'b')
    print('NumCat:',Categoria.getNumInstancias())
    print('NumCat:',c1.getNumInstancias())
    del(c1) # Llama al método __del__
    print('NumCat:',Categoria.getNumInstancias())
    c2.print()
    Categoria.print(c2)

if __name__ == '__main__':
    testAlmacen()
    


