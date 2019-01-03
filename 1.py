# !/usr/bin/env python
# -*-  coding:utf-8  -*-
# version: Python 3.6.3 on win32
# author:  Suranyi    time:  2018/1/16

import numpy as np
import matplotlib.pyplot as plt

# 创建测试数据
x = np.random.randn(20)
y = np.random.randn(20)

# 绘制点
plt.scatter(x, y, s=200, label = '$like$', c = 'blue', marker='.', alpha = None, edgecolors= 'white')
# 用scatter绘制散点图,可调用marker修改点型, label图例用$$包起来，edgecolors边缘颜色，只有前两个是必备参数

# 显示图例
plt.legend()
plt.show()