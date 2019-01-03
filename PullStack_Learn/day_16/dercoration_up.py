# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/25 20:20
#@Email    : 1712817197@qq.com
#@File     : dercoration_up.py
#@Software : PyCharm
import time

def logger(flag = ''):
    def show_time(func):
        def wrapper(*index):
            start_time = time.time()
            func(*index)
            end_time = time.time()
            print('spend %s'%(end_time-start_time))
            if flag == 'true':
                print('打印日志文件')
        return wrapper
    return show_time

@logger() #@show_time
def foo():
    print("hello foo")
    time.sleep(3)
@logger() #@show_time
def add(*index):
    sum = 0
    for i in index:
        sum += i
    print(sum)
    time.sleep(3)
foo()
add(1,3,5,6.7)
