# -*- coding: utf-8 -*-

"""
# Group : E
# description : -
# requirement :
    - pyfiglet
    - clint

"""

# import UI libs
from pyfiglet import Figlet
from clint.textui import puts, colored, indent

# import libs
import os
import sys
import pyuac as hUac
from pyuac import main_requires_admin


def __printUi():
    hFig = Figlet(font='slant')
    print(hFig.renderText('GROUP E'))

    strVer = '0.0.0.1'
    strName = "PowerShell_Scaner"
    strGroupNo = "Group. E"

    with indent(4, quote='>>>'):
        puts(colored.blue('Detector name  \t: ') + strName)
        puts(colored.blue('Detector version: ') + strVer)
        puts(colored.green('group Num  \t\t: ') + strGroupNo)
    print("\n")

def __isAmIAdmin():
    if not hUac.isUserAdmin():
        bRet = False
    else:
        bRet = True
    return bRet



@main_requires_admin(return_output=True)
def _executeAlgorithmLoop():
    print("TEST")

def _mainEngineLoop():
    __printUi()


if __name__ == "__main__":
    _mainEngineLoop()
    rv = _executeAlgorithmLoop()

    with indent(4, quote=">>>"):
        if not rv:
            puts(colored.red('Current UAC status: ') + "Need to grant UAC<Administrator>")

        else:
            puts(colored.yellow('Current UAC status: ') + "Administrator")
            admin_stdout_str, admin_stderr_str, *_ = rv