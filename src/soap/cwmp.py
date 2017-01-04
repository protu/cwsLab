# -*- coding: utf-8 -*-

""" SOAP headers for CWMP protocol
"""

from lxml import etree

NAMESPACE = "http://schemas.xmlsoap.org/soap/envelope/"
NSMAP = {'soap-env': "http://schemas.xmlsoap.org/soap/envelope/",
         'soap-enc': "http://schemas.xmlsoap.org/soap/encoding/",
         'cwmp': "urn:dslforum-org:cwmp-1-0",
         'xsi': "http://www.w3.org/2001/XMLSchema-instance",
         'xsd': "http://www.w3.org/2001/XMLSchema"}

SOAP = '{%s}' % NAMESPACE
SOAP_ENC = '{%s]' % NSMAP['soap-enc']
CWMP = '{%s}' % NSMAP['cwmp']
XSI = '{%s]' % NSMAP['xsi']
XSD = '{%s]' % NSMAP['xsd']


def soap_envelope():

    """ Create SOAP envelpe and return etree element """

    return etree.Element(SOAP + 'Envelope', nsmap=NSMAP)


def soap_header(text):

    """  Create SOAP header with ID tag as specified in TR-069

    Keyword arguments:
    text - session ID, usualy generated wiht sessionID function
    """

    header = etree.Element(SOAP + 'Header')
    ID = etree.Element(CWMP + 'ID')
    ID.attrib[SOAP + 'mustUnderstand'] = "1"
    ID.text = text

    header.append(ID)

    return header


def soap_body():

    """ Return SOAP body element """

    return etree.Element(SOAP+'Body')
