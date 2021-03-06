# -*- coding: utf-8 -*-
from lxml import etree
from soap.cwmp import NAMESPACE, NSMAP, SOAP, SOAP_ENC   # NOQA  @UnusedImport
from soap.cwmp import CWMP, XSI, XSD                     # NOQA  @UnusedImport
from soap.cwmp import soap_envelope, soap_header         # NOQA  @UnusedImport
from soap.cwmp import soap_body                          # NOQA  @UnusedImport


def soap_message(sessionID):

    """ Returns sample TR-069 request message as etree """
    try:
        message = soap_envelope()
        message.append(soap_header(sessionID))
        body = soap_body()
        gpn = etree.SubElement(body, CWMP + "GetParameterNames")
        etree.SubElement(gpn,
                        "ParameterPath").text = "InternetGatewayDevice.WANDevice."
        etree.SubElement(gpn, "NextLevel").text = "true"
        message.append(body)

        return message
    except():
        return None

def tostring(ID="sessionID"):
    try:
        output = etree.tostring(soap_message(ID), pretty_print=True)
    except():
        output = "No input xml message"
    return output


if __name__ == "__main__":
    print(tostring())
