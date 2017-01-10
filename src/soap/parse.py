# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:16:59 2017

@author: dario
"""

from lxml import etree


class Device:

    def __init__(self, soapResponse):

        self.soapResponse = soapResponse

    def getroot(self):
        root = etree.fromstring(self.soapResponse)
        return root

    def getnamespace(self):
        root = self.getroot()
        return root.nsmap

    def cwmpID(self):
        ns = self.getnamespace()
        cwmp = '{'+ns['cwmp']+'}'
        head = None
        for el in self.getroot():
            if 'Header' in el.tag:
                head = el

        ID = head.find(cwmp+'ID')
        return ID.text
