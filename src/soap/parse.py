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
        try:
            root = etree.fromstring(self.__soapResponse)
            return root
        except():
            return None

    @property
    def namespace(self):
        """
        Return namespace of the xml response
        """
        root = self.root
        if root is not None:
            return root.nsmap
        else:
            return None

    @property
    def cwmp_id(self):
        """
        Parse and return soap session id
        """
        try:
            nms = self.namespace
            cwmp = '{'+nms['cwmp']+'}'
            head = None
            for elem in self.root:
                if 'Header' in elem.tag:
                    head = elem

            sess_id = head.find(cwmp+'ID')
            return sess_id.text
        except():
            return "noSessionID"
