# _*_ coding:utf-8 _*_
from pyfiglet import Figlet
from clint.textui import puts, colored, indent

GE_VERSION = '0.0.1.1'
GE_GROUPNUM = "Group E, GCC"
GE_BUILDDATA = '2023'
GE_NAME = "GE_Ps1_Detector %s" %GE_VERSION

def _printUi():
    hFig = Figlet(font='slant')
    print(hFig.renderText('GROUP E'))

    strVer = GE_VERSION
    strName = GE_NAME
    strGroupNo = GE_GROUPNUM

    with indent(4, quote='>>>'):
        puts(colored.blue('Detector name  \t: ') + strName)
        puts(colored.blue('Detector version\t: ') + strVer)
        puts(colored.green('group Num  \t\t: ') + strGroupNo)
    print("\n")



