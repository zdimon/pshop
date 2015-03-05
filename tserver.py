#! /usr/bin/env python
import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import sys
import django.core.handlers.wsgi
from config.settings import BASE_DIR
sys.path.append(BASE_DIR)
def main():
        os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
        application = django.core.handlers.wsgi.WSGIHandler()
        container = tornado.wsgi.WSGIContainer(application)
        http_server = tornado.httpserver.HTTPServer(container)
        http_server.listen(8000)
        tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
                main()
