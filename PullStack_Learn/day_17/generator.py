# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/26 15:50
#@Email    : 1712817197@qq.com
#@File     : generator.py
#@Software : PyCharm
num = (x*2 for x in range(20))
print(next(num))
for i in num:
    print(i)