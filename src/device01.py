# -*- coding: utf-8 -*-
'''
Client for quick tests to the server

'''

# import urllib2
from lxml import etree
import string
import random

NAMESPACE = "http://schemas.xmlsoap.org/soap/envelope/"
NSMAP = {'soap': "http://schemas.xmlsoap.org/soap/envelope/",
         'soap-enc': "http://schemas.xmlsoap.org/soap/encoding/",
         'cwmp': "urn:dslforum-org:cwmp-1-0",
         'xsi': "http://www.w3.org/2001/XMLSchema-instance",
         'xsd': "http://www.w3.org/2001/XMLSchema"}

SOAP = '{%s}' % NAMESPACE
SOAP_ENC = '{%s]' % NSMAP['soap-enc']
CWMP = '{%s}' % NSMAP['cwmp']
XSI = '{%s]' % NSMAP['xsi']
XSD = '{%s]' % NSMAP['xsd']

def sessionID(length=8):
    
    """ Returns arbitrary string of length 'length' which can be used as session ID
    
    Keyword arguments:
    length - length of the arbitrary string
    """
    
    return ''.join([random.choice(string.ascii_letters) for i in range(length)])  # @UnusedVariable

def soap_envelope():
    
    """ Create SOAP envelpe and return etree element """
    
    return etree.Element(SOAP + 'Envelope', nsmap=NSMAP)


def soap_header(text=sessionID()):
    
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

def deviceID(oui="06DA41", manufacturer="Device and co.", product_class="IAD X-2", serial_number="06DA4101ABCD"):
    
    """ Create device ID element """
    
    device = etree.Element("DeviceID")
    etree.SubElement(device, 'OUI').text=oui
    etree.SubElement(device, 'Manufacturer').text=manufacturer
    etree.SubElement(device, 'ProductClassI').text=product_class
    etree.SubElement(device, 'SerialNumber').text=serial_number
    
    return device


def soap_message():
    
    """ Returns sample TR-069 inform message as etree """
    
    message = soap_envelope()
    message.append(soap_header())
    body = soap_body()
    body.append(deviceID())
    message.append(body)
    
    return message
    
if __name__ == "__main__":
    print(etree.tostring(soap_message(), pretty_print=True))
