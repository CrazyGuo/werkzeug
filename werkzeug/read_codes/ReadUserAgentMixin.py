#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..wrappers import Request


def test_request_user_agent():
    user_agents = [
        ('Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.11) '
         'Gecko/20071127 Firefox/2.0.0.11', 'firefox', 'macos', '2.0.0.11',
         'en-US')]
    for ua, browser, platform, version, lang in user_agents:
        request = Request({'HTTP_USER_AGENT': ua})
        assert request.user_agent.browser == browser
        assert request.user_agent.platform ==  platform
        assert request.user_agent.version == version
        assert request.user_agent.language == lang
        assert bool(request.user_agent)
        assert request.user_agent.to_header() == ua 
        assert str(request.user_agent) ==  ua

def start_request_user_agent():
    test_request_user_agent()