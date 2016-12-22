from lxml import etree

NAMESPACE = "http://schemas.xmlsoap.org/soap/envelope/"
NSMAP = {'soap': "http://schemas.xmlsoap.org/soap/envelope/",
         'soap-enc': "http://schemas.xmlsoap.org/soap/encoding/",
         'cwmp': "urn:dslforum-org:cwmp-1-0",
         'xsi': "http://www.w3.org/2001/XMLSchema-instance",
         'xsd': "http://www.w3.org/2001/XMLSchema"}

SOAP = '{%s}' % NAMESPACE
CWMP = '{%s}' % NSMAP['cwmp']

my_soap = etree.Element(SOAP+'Envelope', nsmap=NSMAP)
header = etree.SubElement(my_soap, SOAP+"Header")
ID = etree.Element(CWMP+'ID')
ID.attrib[SOAP+'mustUnderstand'] = "1"
ID.text = 'bcd6266d'
header.append(ID)
body = etree.Element(SOAP+'body')
my_soap.append(body)
gpn = etree.SubElement(body, CWMP+"GetParameterNames")
etree.SubElement(gpn, "ParameterPath").text = "InternetGatewayDevice.WANDevice."
etree.SubElement(gpn, "NextLevel").text = "true"

print(etree.tostring(my_soap, pretty_print=True))
