# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.session import SignedCookieSessionFactory
from pyramid.response import Response
from acs import response
from soap.parse import Device
from device import cpe


@view_config(route_name='cwmp', renderer='string')
def cwmp(request):
    dev = Device(request.body)
    body = response.tostring(ID=dev.cwmpID)
    return Response(body=body, content_type='text/xml; charset=UTF-8')

if __name__ == '__main__':
    config = Configurator()
    config.set_session_factory(SignedCookieSessionFactory(
        cpe.sessionID(64),
        cookie_name='CWSSESSID'))
    config.add_route('cwmp', '/')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
