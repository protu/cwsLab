# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, Response
from acs import response as acs_response
from soap.parse import Device
from device import cpe

app = Flask(__name__)
app.config["SECRET_KEY"] = cpe.sessionID(32) 


@app.route('/', methods=['GET', 'POST'])
def cwmp():
    dev = Device(request.data)
    rsp = acs_response.tostring(ID=dev.cwmpID)

    return Response(rsp, mimetype="text/xml")


if __name__ == '__main__':
      app.run(port=10301)