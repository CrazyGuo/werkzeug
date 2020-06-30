#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import BytesIO

from ..wrappers import Request

def strict_eq(x, y):
    """Equality test bypassing the implicit string conversion in
    Python 2."""
    __tracebackhide__ = True
    assert x == y, (x, y)
    assert issubclass(type(x), type(y)) or issubclass(type(y), type(x))
    if isinstance(x, dict) and isinstance(y, dict):
        x = sorted(x.items())
        y = sorted(y.items())
    elif isinstance(x, set) and isinstance(y, set):
        x = sorted(x)
        y = sorted(y)
    assert repr(x) == repr(y), (x, y)

def test_request_part1():
    req = Request.from_values('/bar?foo=baz', 'http://example.com/test')
    strict_eq(req.path, u'/bar')
    strict_eq(req.full_path, u'/bar?foo=baz')
    strict_eq(req.script_root, u'/test')
    strict_eq(req.url, u'http://example.com/test/bar?foo=baz')
    strict_eq(req.base_url, u'http://example.com/test/bar')
    strict_eq(req.url_root, u'http://example.com/test/')
    strict_eq(req.host_url, u'http://example.com/')
    strict_eq(req.host, 'example.com')
    strict_eq(req.scheme, 'http')
    strict_eq(req.query_string.decode(), 'foo=baz')      
    assert list(req.args.items(multi=True)) == [
            ('foo', 'baz'),
        ]
    strict_eq(req.is_xhr, False)
    strict_eq(req.is_secure, False)
    strict_eq(req.is_multithread, False)
    strict_eq(req.is_multiprocess, False)
    strict_eq(req.is_run_once, False)

    req = Request.from_values(headers={
        'Cookie':   'foo=bar;session_id=1A'
    })
    assert req.cookies == {'foo': 'bar', 'session_id':'1A'}


def test_request_part2():
    data = (b'--foo\r\n'
            b'Content-Disposition: form-data; name="foo_name"; filename="foo.txt"\r\n'
            b'Content-Type: text/plain; charset=utf-8\r\n\r\n'
            b'file contents, just the contents\r\n'
            b'--foo--')
    req = Request.from_values(
        input_stream=BytesIO(data),
        content_length=len(data),
        content_type='multipart/form-data; boundary=foo',
        method='POST',
    )

    foo = req.files['foo_name']
    assert foo.mimetype == 'text/plain'
    assert foo.filename == 'foo.txt'

    assert foo.closed is False
    req.close()
    assert foo.closed is True


def test_request_part3():
    req = Request.from_values(headers={
        'X-Forwarded-For': '192.168.1.2, 192.168.1.1'
    })
    req.environ['REMOTE_ADDR'] = '192.168.1.3'
    assert req.access_route == ['192.168.1.2', '192.168.1.1']
    strict_eq(req.remote_addr, '192.168.1.3')

    req = Request.from_values()
    req.environ['REMOTE_ADDR'] = '192.168.1.3'
    strict_eq(list(req.access_route), ['192.168.1.3'])

def start_base_request():
    test_request_part1()
    test_request_part2()
    test_request_part3()