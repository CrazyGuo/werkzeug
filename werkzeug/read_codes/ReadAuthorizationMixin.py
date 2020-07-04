#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from ..wrappers import Request


def test_encrypt_user_pass():
    username = 'Aladdin'
    password = 'open sesame'
    auth = '%s:%s' % (username, password)
    auth_result = base64.b64encode(auth.encode())
    assert auth_result.decode() == 'QWxhZGRpbjpvcGVuIHNlc2FtZQ=='


def test_authorization_mixin():
    request = Request.from_values(headers={
        'Authorization': 'Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=='
    })
    a = request.authorization
    assert a.type == 'basic'
    assert a.username == 'Aladdin'
    assert a.password == 'open sesame'

def start_request_authorization():
    test_encrypt_user_pass()
    test_authorization_mixin()