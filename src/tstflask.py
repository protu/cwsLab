# -*- coding: utf-8 -*-

"""
Test flask application
"""

from flask import Flask
from flask import request, Response, session
from acs import response as acs_response
from soap.parse import Device
from device import cpe

_app = Flask(__name__)
_app.config["SECRET_KEY"] = cpe.sessionID(32)
_app.secret_key = cpe.sessionID(32)


@_app.route('/', methods=['GET', 'POST'])
@_app.route('/acs/croatia/ULL', methods=['POST'])
def cwmp():
    """ Return response to Device
    and set session cookie
    """
    dev = Device(request.data)
    rsp = acs_response.tostring(ID=dev.cwmpID)
    session['sessionID'] = dev.cwmpID
    return Response(rsp, mimetype="text/xml")


if __name__ == '__main__':
    _app.run(port=10301)
