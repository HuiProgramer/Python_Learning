# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/29 17:12
#@Email    : 1712817197@qq.com
#@File     : Random_modern.py
#@Software : PyCharm
import  random

print(random.random())#返回随机浮点数
print(random.randrange(1,30))#返回整型数，不包括30
print(random.randint(1,30))#返回整型数
print(random.choice("hello world!"))#返回随机的字符或元组