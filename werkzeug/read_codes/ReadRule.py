
from ..routing import Map, Rule, parse_rule,parse_converter_args

def test_pattern():
    url = "/Files/<path(1,m=3,n=4):param1>"
    result_tuple = parse_rule(url)
    for result in result_tuple:
        print(result)

def test_args_kwargs():
    params = "12, m=3"
    result_tuple = parse_converter_args(params)
    for result in result_tuple:
        print(result)

def test_whole():
    rule2 = Rule('/foo/<string(length=2):flag>/show', endpoint='process_len2')
    rule3 = Rule('/foo/<string(length=3):flag>/show', endpoint='process_len3')
    m = Map([ rule2, rule3 ])   
    reg = m.bind('127.0.0.1') 
    match2 = reg.match("/foo/ab/show")
    print(match2)
    match3 = reg.match("/foo/abc/show")
    print(match3)


def start_rule():
    #test_pattern()
    #test_args_kwargs()
    test_whole()