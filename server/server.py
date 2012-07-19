#!/usr/bin/env python3
from pyolymp import http_server
from mako.lookup import TemplateLookup
from configparser import ConfigParser


class Site:
    def __init__(self, template_dir=None):
        self.template_lookup = \
                TemplateLookup(directories=[template_dir])
        self.config = ConfigParser().read("conf/site.conf")

    def index(self):
        return self.template_lookup.get_template("page.html").render(\
                title="Hello", \
                page="Hello, world!")
    index.exposed = True

def main():
    config = ConfigParser()
    config.read("conf/server.conf")
    site = Site(template_dir = config["paths"]["template_dir"])
    http_server.start_http_server(site, "conf/http_server.conf")

if __name__ == "__main__":
    main()
