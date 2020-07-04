#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from ..wrappers import Request


def test_request_etag():
    request = Request({
        'HTTP_CACHE_CONTROL':       'no-store, no-cache',
        'HTTP_IF_MATCH':            'W/"foo", bar, "baz"',
        'HTTP_IF_NONE_MATCH':       'W/"foo", bar, "baz"',
        'HTTP_IF_MODIFIED_SINCE':   'Tue, 22 Jan 2008 11:18:44 GMT',
        'HTTP_IF_UNMODIFIED_SINCE': 'Tue, 22 Jan 2008 11:18:44 GMT'
    })
    assert request.cache_control.no_store
    assert request.cache_control.no_cache

    for etags in request.if_match, request.if_none_match:
        assert etags('bar')
        assert etags.contains_raw('W/"foo"')
        assert etags.contains_weak('foo')
        assert not etags.contains('foo')

    assert request.if_modified_since == datetime(2008, 1, 22, 11, 18, 44)
    assert request.if_unmodified_since == datetime(2008, 1, 22, 11, 18, 44)

def test_ranges():
    req = Request.from_values()
    assert req.range is None
    req = Request.from_values(headers={'Range': 'bytes=0-499'})
    assert req.range.ranges == [(0, 500)]
    assert req.range.range_for_length(500) == (0, 500)
    assert req.range.to_header() == 'bytes=0-499'
    assert req.range.to_content_range_header(500) == 'bytes 0-499/500'

def start_request_etag():
    test_request_etag()
    test_ranges()