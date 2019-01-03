# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/29 16:58
#@Email    : 1712817197@qq.com
#@File     : time_modern.py
#@Software : PyCharm
import datetime
import time

print(datetime.datetime.now())#返回字符串格式化时间
print(time.time())#返回时间戳
print(time.clock())#返回CPU运行时间
Time = time.localtime()#返回元组
print(Time)
print(time.strftime("%Y-%m-%d %H:%M:%S",Time))#返回格式化时间
print(time.strptime("2000-10-30 10:30:10","%Y-%m-%d %H:%M:%S"))#返回元组
print(time.ctime())#返回当前时间的另一种形式