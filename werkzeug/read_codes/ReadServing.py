# -*- coding: utf-8 -*-

from ..serving import run_simple, make_ssl_devcert
from ..wrappers import Request, Response
from ..wsgi import SharedDataMiddleware
 
class Shortly(object):
    #框架可以根据request做具体的路由，比如odoo,flask
    def dispatch_request(self, request):
        return Response('Hello Werkzeug!')
 
    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)
 
    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
 
def create_app():
    app = Shortly()
    return app

def get_ssl_file():
    certificate, private_key = make_ssl_devcert(str("C://Works//doc//thinkdata//ssl_file"))
    return (certificate, private_key)
 
def start_server():
    app = create_app()
    is_ssl = True
    if is_ssl:
        ssl_context = get_ssl_file()
        run_simple('localhost', 443, app, use_debugger=False, use_reloader=False, ssl_context=ssl_context)
    else:
        run_simple('localhost', 5000, app, use_debugger=False, use_reloader=False)