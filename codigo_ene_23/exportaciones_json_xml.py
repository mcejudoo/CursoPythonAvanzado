"""
Exportar registros de la BD a json / xml
"""

import json
from base_datos import BaseDatos, Producto, Categoria, path
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree

def testJSON():
    bd = BaseDatos(path)
    L = bd.select()    
    d = [p.to_json() for p in L]   

    # Convertir la lista de objetos a un formato json y pasarlo a un str. (visualizarlo con indentación)
    cad = json.dumps(d, indent=4)
    print(cad)    

    d2 = json.loads(cad)
    print(d2[0], type(d2[0]))
    obj = Producto.create(d2[0])
    print(obj, type(obj))

    # Grabar en un fichero:
    fich = None
    fich2 = None
    try:
        fich = open("productos.json","w")
        fich2 = open("productos.json","r")
        json.dump(d, fich)
        d2 = json.load(fich2)
        print([p for p in d2 if p.id==80])
        

    except Exception as e:        
        print(e)
        raise e

    finally:
        if fich: fich.close()
        if fich2: fich2.close()


def testXML():
    """
    Exportar a un fichero XML todos los productos
    """
    bd = BaseDatos(path)
    L = bd.select()    
    
    try:
        top = Element('productos')
        top.set("version","1.0")
        comentario = Comment('Productos de la base de datos')
        top.append(comentario)
        for p in L:
            producto = SubElement(top, 'producto')
            producto.attrib['id'] = str(p.id)

            nombre = SubElement(producto, 'nombre')
            nombre.text = p.nombre

            categoria = SubElement(producto, 'categoria')
            categoria.attrib['idcat'] = str(p.cat.id)
            categoria.text = p.cat.nombre

            precio = SubElement(producto, 'precio')
            precio.text = "%.2f" % (p.precio, )

            existencias = SubElement(producto, 'existencias')
            existencias.text = str(p.exis)

        #print(tostring(top))

        # Grabar el XML generado a un fichero:
        tree = ElementTree()
        tree._setroot(top)
        tree.write("productos.xml")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    #testJSON()
    testXML()