#!/usr/bin/env python3
from pyolymp import http_server

class Test:
    def index(self):
        return "Hello, world"
    index.exposed = True

http_server.start_http_server(Test(), "http_server.conf")
