from pysimplesoap.server import SoapDispatcher, SOAPHandler
from http.server import HTTPServer

def hello(name):
    # Esta es la funcionalidad para publicar con el WS
    return {'mensaje':'hello %s' % name}

# Crear el dispatcher
dispatcher = SoapDispatcher('mi_dispatcher', location='http://localhost:8008/', \
action = 'http://localhost:8008/', namespace = 'http://example.com/sample.wsdl', \
    prefix='ns0', trace=True, ns = True)

dispatcher.register_function('Hello', hello, returns={'mensaje':str}, args={'name':str})
if __name__ == '__main__':
    server = HTTPServer(("", 8008), SOAPHandler)
    server.dispatcher = dispatcher
    server.serve_forever()