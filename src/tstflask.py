# -*- coding: utf-8 -*-

"""
Test flask application
"""

import logging
from flask import Flask, after_this_request
from flask import request, Response, session
from acs import response as acs_response
from soap.parse import Device
from device import cpe

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

app = Flask(__name__)
app.config["SECRET_KEY"] = cpe.sessionID(32)
app.secret_key = cpe.sessionID(32)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
@app.route('/acs/croatia/ULL', methods=['POST'])
def cwmp():
    """ Return response to Device
    and set session cookie
    """
    logging.info(request)
    logging.info(request.headers)
    logging.info(request.data)
    if request.method == 'GET':
        return "Go away, you don't exist\n"

    if 'Transfer-Encoding' in request.headers:
        if request.headers['Transfer-Encoding'] == 'chunked':
#           return Response(request.data)

            def chunked_respond():
                chunk_size = 4096
                yield "chunked output\n"
                logging.info(request.data)
                for chunk in request.iter_content(chunk_size):
                    yield chunk
            return Response(chunked_respond())

#            chunk_data = ""
#            chunk_size = 4096
#            while True:
#                chunk = request.stream.read(chunk_size)
#                print (chunk)
#                if len(chunk) == 0:
#                    chunk_size = str(len(chunk_data))
#                    chunk_response = "chunk data " + chunk_size + "\n"
#                    chunk_response += chunk_data
#                    return Response(chunk_response)
#                chunk_data += chunk

    elif 'Soapaction' in request.headers:
        dev = Device(request.data)
        rsp = acs_response.tostring(ID=dev.cwmp_id)
        session['sessionID'] = dev.cwmp_id
        return Response(rsp, mimetype="text/xml")
    else:
        return Response(request.data)


if __name__ == '__main__':
    app.run(port=10301, host="0.0.0.0")
