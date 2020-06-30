
from werkzeug.read_codes.ReadSesseion import start_session_app
from werkzeug.read_codes.ReadServing import start_server
from werkzeug.read_codes.ReadRouting import start_app_with_routing
from werkzeug.read_codes.ReadRule import start_rule
from werkzeug.read_codes.ReadCacheProperty import start_cache
from werkzeug.read_codes.ReadBaseRequest import start_base_request

if __name__ == '__main__':
    #start_session_app()

    #启动server,测试请求流程
    #start_server()
    
    #测试routing
    #start_app_with_routing()

    #测试路由规则
    #start_rule()

    #测试property缓存
    #start_cache()

    #测试BaseRequest
    start_base_request()
