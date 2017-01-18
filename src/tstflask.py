# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def cwmp():
    rsp = ''
    if request.method == 'GET':
        rsp = 'GET method\n'
    else:
        rsp = 'POST method\n'

    return rsp
