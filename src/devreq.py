# -*- coding: utf-8 -*-
from device import cpe
import requests

url = 'http://localhost:8080'
req = requests.post(url, cpe.tostring(),
                    headers={'Content-Type': 'text/xml; charset=ISO-8859-1',
                             'SOAPAction': ''})
for key in req.headers:
    print(key+': '+req.headers[key])
print(req.text)
