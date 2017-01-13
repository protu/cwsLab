# -*- coding: utf-8 -*-
"""
Define ACS methonds
"""

from lxml import etree
from soap.cwmp import NAMESPACE, NSMAP, SOAP, SOAP_ENC   # NOQA  @UnusedImport
from soap.cwmp import CWMP, XSI, XSD                     # NOQA  @UnusedImport
from soap.cwmp import soap_envelope, soap_header         # NOQA  @UnusedImport
from soap.cwmp import soap_body                          # NOQA  @UnusedImport


class GenericMethods:

    def __init__(self):
        pass

    def GetRPCMethods(self):
        pass


class CPEMethods:

    def __init__(self, sessionID):
        self.__sesID = sessionID

    def SetParameterValues(self):
        pass

    def GetParameterValues(self):
        pass

    def SetParameterNames(self):
        pass

    def GetParameterNames(self):
        message = soap_envelope()
        message.append(soap_header(self.__sesID))
        body = soap_body()
        gpn = etree.SubElement(body, CWMP + "GetParameterNames")
        etree.SubElement(
            gpn, "ParameterPath").text = "InternetGatewayDevice.WANDevice."
        etree.SubElement(gpn, "NextLevel").text = "true"
        message.append(body)

        return message

    def SetParameterAttributes(self):
        pass

    def GetParameterAttributes(self):
        pass

    def AddObject(self):
        pass

    def DeleteObject(self):
        pass

    def Download(self):
        pass

    def Reboot(self):
        pass

    def GetQueuedTransfers(self):
        pass

    def ScheduleInform(self):
        pass

    def SetVouchers(self):
        pass

    def GetOptions(self):
        pass

    def Upload(self):
        pass

    def FactoryReset(self):
        pass

    def GetAllQueuedTransfers(self):
        pass

    def ScheduleDownload(self):
        pass

    def CancelTransfer(self):
        pass

    def ChangeDUState(self):
        pass


class ACSMethods:

    def __init__(self, sessionID="testSession"):
        self.__sesID = sessionID

    def Inform(self):

        message = soap_envelope()
        message.append(soap_header(self.__sesID))
        body = soap_body()
        etree.SubElement(body, CWMP + "Inform")
        message.append(body)
        return message

    def InformResponse(self):
        pass

    def TransferComplete(self):
        pass

    def AutonomousTransferComplete(self):
        pass

    def Kicked(self):
        pass

    def RequestDownload(self):
        pass

    def DUStateChangeComplete(self):
        pass

    def AutonomousDUStateChangeComplete(self):
        pass
