# -*- coding: utf-8 -*-
from device import cpe
import requests

url = 'http://localhost:5000'
req = requests.Session().post(url, cpe.tostring(), headers={'Content-Type': 'text/xml; charset=ISO-8859-1', 'SOAPAction': ''})
for key in req.headers:
    print(key + ': ' + req.headers[key])
print(req.text)
