#-*- coding: utf-8 -*-
'''
Created on 2016年10月10日

@author: 武明辉
'''
def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    import os
    pipe = os.popen('' + cmd + '', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None: sts = 0
    if text[-1:] == '\n': text = text[:-1]
    return sts, text