# -*- coding: utf-8 -*-
import requests
from device import cpe


acsurl = 'http://localhost:10301'
req = requests.Session().post(acsurl, cpe.tostring(), headers={'Content-Type': 'text/xml; charset=ISO-8859-1', 'SOAPAction': ''})
for key in req.headers:
    print(key + ': ' + req.headers[key])
print(req.text)
