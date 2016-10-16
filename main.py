#-*- coding: utf-8 -*-
'''
Created on 2016年10月8日

@author: 武明辉
'''
import os

import mycommands

binpathabs=os.path.abspath('UnRar.exe')
binpath=os.path.splitext(binpathabs)[0]
print binpath
targetDir='D:/111'
outputPath='D:/'
cmd_base=binpath+' x -hp'

for pwd in range(999):
    cmd_result=mycommands.getstatusoutput(cmd_base+str(pwd)+' '+targetDir+' '+outputPath)
    result=cmd_result[1].decode('gbk')
    
    if u'全部完成' in result:
        print '提取成功！\n密码是：',pwd
        break;
    else:
        print '正在尝试密码：',pwd,'失败！'




