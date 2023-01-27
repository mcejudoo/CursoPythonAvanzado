"""
Servicio Rest con Flask para la gestión de los productos
"""

from base_datos import BaseDatos, Producto, Categoria, path
from flask import Flask, make_response, jsonify, abort
from flask_restful import Api, Resource

# Crear la aplicación y el API: __name__ nombre del módulo
app = Flask(__name__)
api = Api(app)

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







