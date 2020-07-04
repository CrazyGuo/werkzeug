
from werkzeug.read_codes.ReadSesseion import start_session_app
from werkzeug.read_codes.ReadServing import start_server
from werkzeug.read_codes.ReadRouting import start_app_with_routing
from werkzeug.read_codes.ReadRule import start_rule
from werkzeug.read_codes.ReadCacheProperty import start_cache
from werkzeug.read_codes.ReadBaseRequest import start_base_request
from werkzeug.read_codes.ReadBaseRequestFormFiles import start_base_request_form_file
from werkzeug.read_codes.ReadAcceptMixin import start_accept
from werkzeug.read_codes.ReadRequestEtagMixin import start_request_etag

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
    #start_base_request()

    #测试form表单中有文件
    #start_base_request_form_file()

    #测试接收编码等
    #start_accept()

    #测试Request ETag
    start_request_etag()
