"""
Servicio Rest con Flask para la gestión de los productos
"""

from base_datos import BaseDatos, Producto, Categoria, path
from flask import Flask, make_response, jsonify, abort
from flask_restful import Api, Resource, reqparse

# Crear la aplicación y el API: __name__ nombre del módulo
app = Flask(__name__)
api = Api(app)

# Definir parseadores para recuperar los parametros:
parser_cat = reqparse.RequestParser()
parser_cat.add_argument("id", type=int)
parser_cat.add_argument("nombre", type=str)

parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("nombre", type=str)
parser.add_argument("cat", type=dict)
parser.add_argument("precio", type=float)
parser.add_argument("exis", type=int)

# Operaciones: GET -> id, DELETE -> id

class Productos(Resource):

    def get(self):
        """
        Devuelve todos los productos
        """
        bd = BaseDatos(path)
        # Devuelve una lista de objetos.
        productos = bd.select()
        # Convertirlos a json:
        L = [p.to_json() for p in productos]
        return make_response(jsonify(L), 200)

    def post(self):
        """Crea un nuevo recurso: producto"""
        try:
            args = parser.parse_args()
            #print('args:', args)
            nombreCat = args['cat']['nombre']
            bd = BaseDatos(path)
            categoria = bd.readCategoria(nombreCat)
            producto = Producto.create(args)
            producto.cat = categoria
            #print('producto: ', producto)           
            n = bd.create(producto)
            return {"create":n}

        except Exception as e:
            return {"error":str(e)}


class ProductosCategorias(Resource):

    def get(self, cat):
        """
        Devuelve todos los productos
        """
        try:
            bd = BaseDatos(path)
            # Antes intentamos recuperar la categoria:
            categoria = bd.readCategoria(cat)
            # Devuelve una lista de objetos.
            productos = bd.select(cat)
            # Convertirlos a json:
            L = [p.to_json() for p in productos]
            return make_response(jsonify(L), 200)

        except ValueError as e:
            abort(404, description=str(e))

        except Exception as e:
            return {"error":str(e)}

# Mapeo de recursos y URLs:
api.add_resource(Productos, "/productos","/productos/")
api.add_resource(ProductosCategorias, "/productos/categoria/<cat>")

if __name__=="__main__":
    app.run(debug=True)







