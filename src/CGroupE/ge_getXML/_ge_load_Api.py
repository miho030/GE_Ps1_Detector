# -*- coding: utf-8 -*-

"""
* description : find & load the all of bat/ps1 script
    due to "Scriptblock_Logging"
"""

# import libs
import os

GE_CLEARNER_DIR = "./resources/clear_psevent.bat"
GE_COLLECTOR_DIR = "./resources/collect_psevent.bat"
GE_ENABLE_POWERSHELL_LOGGING_DIR = "./resources/enable_powershell_logging.reg"
#GE_PARSE_MWP_PY = "./resources/parse_mwpsopevent.py"
#GE_PARSE_WIN_PY = "./resources/parse_winpsevent.py"

def _runCleaner():
    bRet = False

    strCmd = GE_CLEARNER_DIR + " && pause"
    print(strCmd)
    os.system(strCmd)
    strLog = os.popen(strCmd).read()

    if str(strLog) is None:
        return bRet
    else:
        bRet = True
        return bRet, str(strLog)

def _runCollector():
    bRet = False

    strCmd = GE_COLLECTOR_DIR
    os.system(strCmd)
    strLog = os.popen(strCmd).read()

    if str(strLog) is None:
        return bRet
    else:
        bRet = True
        return bRet, strLog

def _runPs1Logging():
    bRet = False

    strCmd = GE_COLLECTOR_DIR
    os.system(strCmd)
    strLog = os.popen(strCmd).read()

    if str(strLog) is None:
        return bRet
    else:
        bRet = True
        return bRet, strLog