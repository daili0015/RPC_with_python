#!/usr/bin/env python
# coding: utf-8
# pip install python-jsonrpc

import pyjsonrpc
from time import sleep

class RequestHandler(pyjsonrpc.HttpRequestHandler):

    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        return a + b

# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = ('127.0.0.1', 2725),
    RequestHandlerClass = RequestHandler
)
print "Starting HTTP server ..."
print "URL: http://140.143.232.165:34222"
http_server.serve_forever()