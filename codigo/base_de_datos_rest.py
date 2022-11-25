"""
Servidor REST para implementar un API REST: con las operaciones CRUD 
"""

from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api, abort, reqparse
from base_datos import BaseDatos, path, Producto, Categoria, Empleado

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

parser_emp = reqparse.RequestParser()
parser_emp.add_argument("id", type=int)
parser_emp.add_argument("nombre", type=str)
parser_emp.add_argument("cargo", type=str)

class ProductoRest(Resource):

    def get(self, id):
        """
        Recupera un producto de la base de datos
        """
        try:
            bd = BaseDatos(path)
            producto = bd.read(id)
            return make_response(jsonify(producto.to_json()),200)        
        except Exception as e:
            abort(404, message=str(e))

    def delete(self, id):
        """
        Eliminar un recurso de la base de datos
        """
        try:
            bd = BaseDatos(path)
            producto = bd.read(id)           
            n = bd.delete(id)
            if n == 1:
                # Se ha podido borrar
                d = {"Producto eliminado":producto.nombre}
            else:
                d = {"Producto no eliminado":id}

            return d
        except Exception as e:
            abort(404, message=str(e))

class ProductosList(Resource):

    def get(self):
        """
        Recuperar todos los productos de la base de datos
        """
        bd = BaseDatos(path)
        productos = bd.select()
        L = [p.to_json() for p in productos]
        return make_response(jsonify(L),200)

    def post(self):
        try:
            args = parser.parse_args()
            producto = Producto.create(args)
            bd = BaseDatos(path)
            n = bd.create(producto)
            return {"create":n}

        except Exception as e:
            return {"error":str(e)}

    def put(self):
        try:
            args = parser.parse_args()
            producto = Producto.create(args)
            bd = BaseDatos(path)
            # Comprobar si existe el producto en la base de datos
            bd.read(producto.id)
            n = bd.update(producto)
            return {"update":n}

        except ValueError as e:
            abort(404, message=str(e))

        except Exception as e:
            return {"error":str(e)}
    
class ProductosCategoriasList(Resource):

    def get(self, cat):
        """
        Recuperar todos los productos de la base de datos
        """
        try:
            bd = BaseDatos(path)
            categoria = bd.readCategoria(cat)
            productos = bd.select(cat)
            L = [p.to_json() for p in productos]
            return make_response(jsonify(L),200)

        except ValueError as e:
            abort(404, message=str(e))

        except Exception as e:
            return {"error":str(e)}


class EmpleadoRest(Resource):

    def post(self):
        """Crea un nuevo empleado en la base de datos"""
        try:
            args = parser_emp.parse_args()
            empleado = Empleado.create(args)
            bd = BaseDatos(path)
            n = bd.createEmpleado(empleado)
            return {"create_empleado":n}

        except Exception as e:
            return {"error":str(e)}


# Mapeo de clases y recursos:
# GET: http://localhost:5000/productos/<id>
# DELETE: http://localhost:5000/productos/<id>
# GET: http://localhost:5000/productos
# POST: http://localhost:5000/productos
# PUT: http://localhost:5000/productos
# GET: http://localhost:5000/productos/categoria/<nombre_categoria>
# POST: http://localhost:5000/empleados
api.add_resource(ProductoRest, "/productos/<id>")
api.add_resource(ProductosList, "/productos","/productos/")
api.add_resource(ProductosCategoriasList, "/productos/categoria/<cat>")
api.add_resource(EmpleadoRest, "/empleados", "/empleados/")

if __name__ == "__main__":
    app.run(debug=True)
