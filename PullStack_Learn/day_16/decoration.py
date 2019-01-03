# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/25 19:30
#@Email    : 1712817197@qq.com
#@File     : decoration.py
#@Software : PyCharm
import time

def show_time(func):

    def wrapper(*index):
        start_time = time.time()
        func(*index)
        end_time = time.time()
        print('spend %s'%(end_time-start_time))

    return wrapper

@show_time #foo = show_time(foo)
def foo():
    print("hello foo")
    time.sleep(3)
@show_time #add = show_time(add)
def add(*index):
    sum = 0
    for i in index:
        sum += i
    print(sum)
    time.sleep(3)
foo()
add(1,3,5,6.7)
