# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/8 15:18
#@Email    : 1712817197@qq.com
#@File     : city_read.py
#@Software : PyCharm
with open('city.json','r',encoding='utf8') as f:
    data = f.readlines()
    for i in data:
        print(i)
    #print(data)
    f.close()