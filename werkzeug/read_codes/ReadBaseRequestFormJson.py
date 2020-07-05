#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from ..wrappers import Request, Response
from ..routing import Map, Rule
from ..exceptions import HTTPException, NotFound
from ..utils import redirect
from ..serving import run_simple


class Shortly(object):
    
    def __init__(self):
        self.url_map = Map([
            Rule('/process_form', endpoint='process_form', methods=['POST']),
            Rule('/process_json', endpoint='process_json', methods=['POST']),
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

    #具体处理form表单数据
    def on_process_form(self, request):
        #1. form属性
        assert request.form['name'] == 'Matthew'
        assert request.form['sex'] == 'M'
        assert request.form['age'] == '25'        

        #2.values属性
        assert request.values['name'] == 'Matthew'
        assert request.values['sex'] == 'M'
        assert request.values['age'] == '25' 

        #4.stream属性
        st = request.stream

        #5.data属性
        data =  request.data

        return Response('on_process_form')

    #具体处理json数据
    def on_process_json(self, request):
        byte_data = request.get_data()
        str_data = byte_data.decode()
        json_data = json.loads(str_data)

        assert json_data['name'] == 'Matthew'
        assert json_data['sex'] == 'M'
        assert json_data['age'] == 25

        return Response('on_process_json')


def create_app():
    app = Shortly()
    return app


def start_base_request_form_json():
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=False, use_reloader=False)  