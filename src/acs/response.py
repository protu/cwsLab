# -*- coding: utf-8 -*-
from lxml import etree
from soap.cwmp import NAMESPACE, NSMAP, SOAP, SOAP_ENC, CWMP, XSI, XSD # @UnusedImport
from soap.cwmp import soap_envelope, soap_header, soap_body # @UnusedImport

def soap_message():
    
    """ Returns sample TR-069 request message as etree """
    
    message = soap_envelope()
    message.append(soap_header("sessionID"))
    body = soap_body()
    gpn = etree.SubElement(body, CWMP + "GetParameterNames")
    etree.SubElement(gpn, "ParameterPath").text = "InternetGatewayDevice.WANDevice."
    etree.SubElement(gpn, "NextLevel").text = "true"
    message.append(body)
    
    return message

def tostring():
    return etree.tostring(soap_message(), pretty_print=True)
    
if __name__ == "__main__":
    print (tostring())
