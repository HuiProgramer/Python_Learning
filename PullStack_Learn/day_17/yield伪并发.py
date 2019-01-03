# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/27 18:39
#@Email    : 1712817197@qq.com
#@File     : yield伪并发.py
#@Software : PyCharm
#_*_coding:utf-8_*_

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    next(c)
    next(c2)
    print("%s开始准备做包子啦!"%name)
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")
