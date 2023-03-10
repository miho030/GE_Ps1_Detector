# -*- coding: utf-8 -*-

# import libs <python libs>
from clint.textui import puts, colored, indent
from pyuac import main_requires_admin

from ge_Const.ge_PrintUI import _printUi
from ge_getXML._ge_load_Api import _runCleaner
from ge_getXML._ge_load_Api import _runCollector
from ge_Algorithm.ge_mug import _ScanPs1_Mug


@main_requires_admin(return_output=True)
def _initToAdmin():

    __runAlgorithmLoop()

def __runAlgorithmLoop():
    bRet, strCleanLogBuf = _runCleaner()
    bRes, strColecLogBuf = _runCollector()

    if (bRet != True) & (bRes != True):
        puts(colored.red('Failure load external file') + str("FAILED to Execute Clearner.bat, Collector.bat"))
    else:
        puts(colored.green('Load external file') + str("Successfully and run Cleaner.bat, Collector.bat"))
        print("\n")

        MugarrMal, MugarrBign = [], []
        print("[*] Starting Algorithm name: ", str("Algorithm.Mug"))
        strMalDir = "../malicious"
        MugarrMal, MugarrBign = _ScanPs1_Mug(strMalDir)

        print("#", "=" * 40, "#")
        print(">>> Complete analyse with Algorithm.Mug")
        print("\t>>> Count of detection ps1: ", str(len(MugarrMal)))
        print("\t>>> Count of benign ps1: ", str(len(MugarrBign)))
        print("#", "=" * 40, "#")



if __name__ == "__main__":
    _printUi()
    rv = _initToAdmin()
    with indent(4, quote=">>>"):
        if not rv:
            puts(colored.red('Current UAC Status: ') + str("Need to grant UAC<Administrator>"))
        else:
            puts(colored.yellow('\nCurrent UAC Status: ') + str("Administrator"))
            admin_stdout_str, admin_stderr_str, *_ = rv




