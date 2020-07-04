#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from ..wrappers import Request

def test_common_request_descriptors_mixin():
    request = Request.from_values(
        content_type='text/html; charset=utf-8',
        content_length='23',
        headers={
            'Referer':          'http://www.example.com/',
            'Date':             'Sat, 28 Feb 2009 19:04:35 GMT',
            'Max-Forwards':     '10',
            'Pragma':           'no-cache',
            'Content-Encoding': 'gzip',
            'Content-MD5':      '9a3bc6dbc47a70db25b84c6e5867a072'
        }
    )

    assert request.content_type == 'text/html; charset=utf-8'
    assert request.mimetype == 'text/html'
    assert request.mimetype_params == {'charset': 'utf-8'}
    assert request.content_length == 23
    assert request.referrer == 'http://www.example.com/'
    assert request.date == datetime(2009, 2, 28, 19, 4, 35)
    assert request.max_forwards == 10
    assert 'no-cache' in request.pragma
    assert request.content_encoding == 'gzip'
    assert request.content_md5 == '9a3bc6dbc47a70db25b84c6e5867a072'

def start_common_request_descriptors_mixin():
    test_common_request_descriptors_mixin()