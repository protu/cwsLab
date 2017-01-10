# coding: utf-8
import sys
sys.path
get_ipython().magic(u'pwd')
get_ipython().magic(u'cd projects/cwsLab/')
runfile('devreq.py')
get_ipython().magic(u'run ./devreq.py')
get_ipython().magic(u'pwd')
get_ipython().magic(u'cd src')
get_ipython().magic(u'run ./devreq.py')
from device import cpe
cpe.tostring()
from lxml import etree
tree = etree.parse(cpe.tostring())
tree = etree.fromstring(cpe.tostring())
etree.tostring(tree)
etree.parse(tree)
parser = etree.XMLParser()
tree.getroottree()
type(tree)
tree.getparent()
tree.getchildren()
etree.tostring(tree.getchildren())
print(etree.tostring(tree.getchildren()))
tree.nsmap
nm = tree.nsmap
nm['cwmp']
tree.find('ID', namespaces=nm['cwmp'])
tree.find('ID', namespaces='cwmp')
tree.find('ID', namespaces=nm)
tree.getnext()
tree.tag
tree.getnext()
tree.tag
tree.getnext().tag
envelope = tree.getnext()
type(envelope)
print(envelope)
get_ipython().magic(u'who ')
get_ipython().magic(u'clear envelope')
get_ipython().magic(u'who ')
envelope = None
get_ipython().magic(u'who ')
get_ipython().magic(u'who')
tree.find('Envelope')
tree.findall('ID')
tree.xpath('ID')
tree.xpath('/ID')
etree.tostring(tree)
tree.xpath('DeviceID')
print(tree.tag)
tree.find("ID").tag
tree.find(".//ID")
tree.find(".//ID").tag
tree.find(".//Body").tag
tree.find("Body").tag
tree.find("Element").tag
tree.find("Envelope").tag
nm
type(nm)
sc = etree.XMLSchema(etree=tree)
from io import StringIO
tree.text
etree.tostring(tree.nsmap)
etree.tostring(tree)
tree.getnext
tree.getnext()
tree.getiterator()
nm
get_ipython().magic(u'run devreq.py')
get_ipython().magic(u'who ')
from requests import Request, Session
req = Request('POST', url='http:localhost:8080', data=cpe.tostring())
req
req.headers
req.headers()
prepreq = req.prepare
prepreq
print(prepreq)
prepreq.daa
prepreq.data
del
del prepreq.headers('Content-Type')
del prepreq.headers['Content-Type']
get_ipython().magic(u'history')
req = Request('POST', url='http:localhost:8080', data=cpe.tostring(), headers=headers)
get_ipython().magic(u'reset')
get_ipython().magic(u'reset')
get_ipython().magic(u'who ')
import sys
sys.path
get_ipython().magic(u'run devreq.py')
get_ipython().magic(u'who ')
type(req)
req.headers
get_ipython().magic(u'run devreq.py')
from lxml import etree
from device import cpe
devreq = etree.fromstring(cpe.tostring())
print(etree.tostring(devreq, pretty_print=True)
)
for e in devreq.iter():
    print e
    
nm =devreq.nsmap
nm
root.find(nm['cwmp']+'ID')
devreq.find(nm['cwmp']+'ID')
nm['cwmp']
cwmp = '{'+nm['cwmp']+'}'
cwmp
cwmp+'ID'
devreq.find(cwmp+'ID')
devreq
devreq.tag
devreq.find('ID', cwmp)
devreq.find('ID', namespaces=cwmp)
cwmp
devreq.find("ID", namespaces=None)
devreq.find("ID", namespaces=cwmp)
devreq.find("ID", namespaces=nm)
devreq.find("ID", namespaces=nm[0])
nm[0]
nm{0}
nm
nm(0)
slice(nm, 'cwmp')
print(slice(nm, 'cwmp'))
help slice
slice
get_ipython().magic(u'pinfo slice')
nm
nm_cwmp = {'cwmp': nm['cwmp']}
nm_cwmp
devreq.find('ID', namespaces=nm_cwmp)
list(devreq)
devreq.find('{http://schemas.xmlsoap.org/soap/envelope/}Header')
dr_head = devreq.find('{http://schemas.xmlsoap.org/soap/envelope/}Header')
dr_head
dr_head.text
dr_head.find('ID')
dr_head.find(cwmp+'ID')
dr_head.find(cwmp+'ID').text
for el in devreq:
    print el
    
for el in devreq:
    if 'Header' in el.tag:
        print el.tag
        
get_ipython().magic(u'save')
get_ipython().magic(u'pwd')
get_ipython().magic(u'save isession1.py')
help(save)
get_ipython().magic(u'pinfo %save')
get_ipython().magic(u'save isession1.py ...')
get_ipython().magic(u'save isession1.py 1-149')
