# -*- coding: utf-8 -*-
'''
Client for quick tests to the server

'''

from lxml import etree
import string
import random
from soap.cwmp import NAMESPACE, NSMAP, SOAP, SOAP_ENC   # NOQA  @UnusedImport
from soap.cwmp import CWMP, XSI, XSD                     # NOQA  @UnusedImport
from soap.cwmp import soap_envelope, soap_header         # NOQA  @UnusedImport
from soap.cwmp import soap_body                          # NOQA  @UnusedImport


def sessionID(length=8):

    """ Returns arbitrary string of length 'length' which
    can be used as session ID

    Keyword arguments:
    length - length of the arbitrary string
    """

    return ''.join([random.choice(string.ascii_letters)
                    for i in range(length)])                   # @UnusedVariable


def deviceID(oui="06DA41", manufacturer="Device and co.",
             product_class="IAD X-2", serial_number="06DA4101ABCD"):

    """ Create device ID element """

    device = etree.Element("DeviceID")
    etree.SubElement(device, 'OUI').text = oui
    etree.SubElement(device, 'Manufacturer').text = manufacturer
    etree.SubElement(device, 'ProductClassI').text = product_class
    etree.SubElement(device, 'SerialNumber').text = serial_number

    return device


def inform(events=['0 BOOTSTRAP', '1 BOOT']):

    """ Create inform request and return etree element

    Keyword arguments:
    events - list of event codes (strings)
    """

    cwmp_inform = etree.Element(CWMP+"Inform")
    event = etree.Element("Event")
    event.attrib[SOAP+"arrayType"] = "cwmp:EventStruct[" \
        + str(len(events)).zfill(2) + "]"
    for e in events:
        event_struct = etree.Element("EventStruct")
        etree.SubElement(event_struct, "EventCode").text = e
        etree.SubElement(event_struct, "CommandKey")
        event.append(event_struct)

    cwmp_inform.append(deviceID())
    cwmp_inform.append(event)

    return cwmp_inform


def soap_message():

    """ Returns sample TR-069 inform message as etree """

    message = soap_envelope()
    message.append(soap_header(sessionID()))
    body = soap_body()
    body.append(inform())
    message.append(body)

    return message


def tostring():
    return (etree.tostring(soap_message(), pretty_print=True))
