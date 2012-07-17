#!/usr/bin/env python3
"This module is simple HTTP server"
import cherrypy
import sys


def start_http_server(handler, config):
    """Starts HTTP server.

    handler
        A class, which describes functions to serve HTTP queries in
        cherrypy style.
    config
        A path to config file in cherrypy style.
    """
    cherrypy.tree.mount(handler)
    cherrypy.config.update(config)
    engine = cherrypy.engine
    try:
        engine.start()
    except:
        sys.exit(1)
    else:
        engine.block()
