# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/27 17:10
#@Email    : 1712817197@qq.com
#@File     : Fibonacci.py
#@Software : PyCharm
def fib(max):
    n,before,after = 0,0,1
    while n < max:
        yield before
        after,before = before,after+before
        n = n + 1
Fib = []
for i in fib(10):
        Fib.append(i)
print(Fib)