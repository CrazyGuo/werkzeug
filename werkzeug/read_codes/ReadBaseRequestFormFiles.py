#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import BytesIO

from ..wrappers import Request, Response
from ..routing import Map, Rule
from ..exceptions import HTTPException, NotFound
from ..utils import redirect
from ..serving import run_simple


class Shortly(object):
    
    def __init__(self):
        self.url_map = Map([Rule('/process_form_file', endpoint='process_form_file', methods=['POST'])])

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

    #具体处理form与file的函数
    def on_process_form_file(self, request):
        #1. form属性
        assert request.form['name'] == 'Matthew'
        assert request.form['sex'] == 'M'
        assert request.form['age'] == '25'        

        #2.values属性
        assert request.values['name'] == 'Matthew'
        assert request.values['sex'] == 'M'
        assert request.values['age'] == '25'

        #3.files属性
        myfile = request.files['myfile']
        assert myfile.mimetype == 'application/vnd.ms-excel'
        assert myfile.filename == 'report.xls'

        myimages = request.files['myimages']
        assert myimages.mimetype == 'image/png'
        assert myimages.filename == 'bar.png'   

        #4.stream属性
        st = request.stream

        #5.data属性
        data =  request.data

        return Response('on_process_form_file')


def create_app():
    app = Shortly()
    return app


def start_base_request_form_file():
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=False, use_reloader=False)  