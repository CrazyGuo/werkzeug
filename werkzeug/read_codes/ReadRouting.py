from ..wrappers import Request, Response
from ..routing import Map, Rule
from ..exceptions import HTTPException, NotFound
from ..utils import redirect
from ..serving import run_simple

class Shortly(object):
    
    def __init__(self):
        self.url_map = Map([
            Rule('/', endpoint='new_url'),
            Rule('/<short_id>', endpoint='follow_short_link'),
            Rule('/<short_id>+', endpoint='short_link_details')
        ])

    #请求分发到具体处理函数
    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except NotFound as e:
            return self.error_404()
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


    #以下都是具体路由到的目标处理函数
    def on_new_url(self, request):
        return Response('on_new_url')

    def on_follow_short_link(self, request, short_id):
        return Response('on_follow_short_link')

    def on_short_link_details(self, request, short_id):
        return Response('on_short_link_details')

def create_app():
    app = Shortly()
    return app


def start_app_with_routing():
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)        

