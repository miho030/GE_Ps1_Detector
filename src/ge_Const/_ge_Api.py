# -*- coding: utf-8 -*-
"""
* Description : Functions are used to common purpose.
    ex) check UAC(admin), calculator, check hashs etc...
"""

import os
from pyuac import isUserAdmin

# check windows os system
def __isAmIWindows():
    if os.name == 'nt':
        bRet = True
    else:
        bRet = False
    return bRet

# check UAC permission
def __isAmIAdmin():
    if not isUserAdmin():
        bRet = False
    else:
        bRet = True
    return bRet