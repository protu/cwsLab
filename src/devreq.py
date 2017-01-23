# -*- coding: utf-8 -*-
"""
Test function for sending connectio request
"""
import requests
from device import cpe


ACSURL = 'http://localhost:10301'

def send_request():
    """
    Send connection request to ACS server
    """
    req = requests.Session().post(ACSURL, cpe.tostring(),
                                  headers={'Content-Type': 'text/xml; charset=ISO-8859-1',
                                           'SOAPAction': ''})
    for key in req.headers:
        print(key + ': ' + req.headers[key])
    print(req.text)

if __name__ == '__main__':
    send_request()
