# -*- coding: utf-8 -*-
"""
Test function for sending connectio request
"""
import requests
from device import cpe


ACSURL = 'http://localhost:10301/acs/croatia/ULL'


def send_request():
    """
    Send connection request to ACS server
    """
    tr_session = requests.Session()
    dev_request = tr_session.post(ACSURL, cpe.tostring(),
                                  headers={'Content-Type': 'text/xml; charset=ISO-8859-1',
                                           'SOAPAction': ''})
    print_request(dev_request)
    # dev_request = tr_session.post(ACSURL)
    # print_request(dev_request)
    tr_session.close()
    dev_request.close()


def print_request(dev_request):
    """
    Print request data
    dev_request - request object
    """
    print("\nClient(our) headers:\n")
    for key in dev_request.request.headers:
        print(key + ': ' + dev_request.request.headers[key])

    print("\nServer headers:\n")
    for key in dev_request.headers:
        print(key + ': ' + dev_request.headers[key])

    print("\nResponse message:\n")
    print(dev_request.text)


if __name__ == '__main__':
    send_request()
