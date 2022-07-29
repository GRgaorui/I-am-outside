from tornado.wsgi import WSGIContainer 
from tornado.httpserver import HTTPServer 
from tornado.ioloop import IOLoop 
from app import app  # 这里导入的是flsk项目的运行模块

http_server = HTTPServer(WSGIContainer(app)) 
http_server.listen(9900) 
IOLoop.instance().start()