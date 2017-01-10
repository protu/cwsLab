# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from acs import response
from soap.parse import Device


@view_config(route_name='cwmp', renderer='string')
def cwmp(request):
    request.response.content_type = 'text/xml; charset=UTF-8'
    dev = Device(request.body)
    rsp = response.tostring(ID=dev.cwmpID())
    return rsp

if __name__ == '__main__':
    config = Configurator()
    config.add_route('cwmp', '/')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
