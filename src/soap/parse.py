# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:16:59 2017

@author: dario
"""

from lxml import etree


class Device(object):
    """
    Handle device properties
    """

    def __init__(self, soapResponse):

        self.__soapResponse = soapResponse

    @property
    def root(self):
        """
        Return root of the xml response
        """
        root = etree.fromstring(self.__soapResponse)
        return root

    @property
    def namespace(self):
        """
        Return namespace of the xml response
        """
        root = self.root
        return root.nsmap

    @property
    def cwmpID(self):
        """
        Parse and return soap session id
        """
        try:
            ns = self.namespace
            cwmp = '{'+ns['cwmp']+'}'
            head = None
            for el in self.root:
                if 'Header' in el.tag:
                    head = el

            ID = head.find(cwmp+'ID')
            return ID.text
        except():
            return "noSessionID"
