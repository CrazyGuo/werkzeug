#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..wrappers import Request
from ..datastructures import MIMEAccept, LanguageAccept, CharsetAccept, Accept


def test_accept():
    request = Request({
        'HTTP_ACCEPT':  'text/xml,application/xml,application/xhtml+xml,'
                        'text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
        'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'HTTP_ACCEPT_ENCODING': 'gzip,deflate',
        'HTTP_ACCEPT_LANGUAGE': 'en-us,en;q=0.5'
    })

    assert request.accept_mimetypes == MIMEAccept([
        ('text/xml', 1), ('image/png', 1), ('application/xml', 1),
        ('application/xhtml+xml', 1), ('text/html', 0.9),
        ('text/plain', 0.8), ('*/*', 0.5)
    ])
    assert request.accept_charsets == CharsetAccept([
        ('ISO-8859-1', 1), ('utf-8', 0.7), ('*', 0.7)
    ])
    assert request.accept_encodings == Accept([
        ('gzip', 1), ('deflate', 1)])
    assert request.accept_languages == LanguageAccept([
        ('en-us', 1), ('en', 0.5)]) 


def start_accept():
    test_accept()