# -*- coding: utf-8 -*-
"""
* Description : making a class and initailizing it,
    - also have managing all detection algorithms.
    - run as administrator permission

* requirements :
    - figlet, clint
    - pyuac

"""

# import libs <python libs>
import os
import sys
import pyuac as hUac
from clint.textui import puts, colored, indent
from pyuac import main_requires_admin

# import libs <Group E methods>
import ge_Const._ge_Const as bScanReport
from ge_Const._ge_PrintUI import __printUi
from ge_Const._ge_Api import __isAmIAdmin
from ge_getXML._ge_load_Api import _runCleaner
from ge_getXML._ge_load_Api import _runCollector


def _mainEngineLoop():
    __printUi()

@main_requires_admin(return_output=True)
def _initToAdmin():
    print("\t->[DEBUG] ", "initToAdmin() test")
    __runAlgorithmLoop()

def __runAlgorithmLoop():
    with indent(4, quote=">>>"):
        print("\t->[DEBUG] ", "__runAlgorithmLoop test")
        bRet, strCleanLogBuf = _runCleaner()
        bRes, strColecLogBuf = _runCollector()
        if (bRet != True) & (bRes != True):
            puts(colored.red('[ERROR] Failure load external file') + str("FAILED to Execute Clearner.bat, Collector.bat"))
        else:
            puts(colored.green('Load external file') + str("Successfully and run Cleaner.bat, Collector.bat"))

            fp1 = open("cleanLog.txt", 'w')
            fp1.write(strCleanLogBuf)
            fp1.close()

            print("\t->[DEBUG] ", "runCleaner test(bool) : ", bRet)
            #print("\t->[DEBUG] ", "strLogBuf value : ", strCleanLogBuf)
            print("\t->[DEBUG] ", "runCollector test(bool) : ", bRes)
            #print("\t->[DEBUG] ", "strLogBuf value : ", strColecLogBuf)


if __name__ == "__main__":
    _mainEngineLoop()
    rv = _initToAdmin()
    with indent(4, quote=">>>"):
        if not rv:
            puts(colored.red('Current UAC Status: ') + str("Need to grant UAC<Administrator>"))
        else:
            puts(colored.yellow('\nCurrent UAC Status: ') + str("Administrator"))
            admin_stdout_str, admin_stderr_str, *_ = rv
            """ Do something like search or scan or detect or delete.. <call functions>"""




