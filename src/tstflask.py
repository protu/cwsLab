# -*- coding: utf-8 -*-

"""
Test flask application
"""

from flask import Flask
from flask import request, Response, session
from acs import response as acs_response
from soap.parse import Device
from device import cpe

app = Flask(__name__)
app.config["SECRET_KEY"] = cpe.sessionID(32)
app.secret_key = cpe.sessionID(32)


@app.route('/', methods=['GET', 'POST'])
@app.route('/acs/croatia/ULL', methods=['POST'])
def cwmp():
    """ Return response to Device
    and set session cookie
    """
    if request.method == 'GET':
        return "Go away, you don't exist\n"

    if request.headers.has_key('Soapaction') is True:
        dev = Device(request.data)
        rsp = acs_response.tostring(ID=dev.cwmp_id)
        session['sessionID'] = dev.cwmp_id
        return Response(rsp, mimetype="text/xml")
    else:
        return Response(request.data)


if __name__ == '__main__':
    app.run(port=10301)
