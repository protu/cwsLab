# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:16:59 2017

@author: dario
"""

from lxml import etree


class Device(object):

    def __init__(self, soapResponse):

        self.__soapResponse = soapResponse

    @property
    def root(self):
        root = etree.fromstring(self.__soapResponse)
        return root

    @property
    def namespace(self):
        root = self.root
        return root.nsmap

    @property
    def cwmpID(self):
        ns = self.namespace
        cwmp = '{'+ns['cwmp']+'}'
        head = None
        for el in self.root:
            if 'Header' in el.tag:
                head = el

        ID = head.find(cwmp+'ID')
        return ID.text
