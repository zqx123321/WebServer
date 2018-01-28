#!usr/bin/python
# -*- coding: utf-8 -*-

import sys

# 取参数
try:
    paramStr = sys.argv[1]
    # 分离参数
    paramArr = paramStr.split('&')
    paramDic = {}

    # 取出每个参数的值
    for param in paramArr:
        key, value = param.split('=')
        paramDic[key] = value

    if paramDic["username"] == "abc" and paramDic["password"] == "123":
        print '''{"Status":"ok","Text":"登陆成功<br /><br />欢迎您，''' + paramDic["username"] + '''"} '''
    else:
        print '''{"Status":"Erro","Erro":"账号名或密码有误"}'''
except:
    print "No Params!"
