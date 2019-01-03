# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/6/29 14:33
#@Email    : 1712817197@qq.com
#@File     : shopping.py
#@Software : PyCharm
product_list = [
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000)
]
shopping_car = [

]
saving = input('please input your saving:')
if saving.isdigit():
    saving = int(saving)
    while True:
        for i,j in enumerate(product_list):
            print(i,'>>>>>',j[0],':',j[1])
        choice = input('选择要购买的商品编号【退出：q】：')
        if choice.isdigit():
            choice = int(choice)
            if choice >=0 and choice <= len(product_list)-1:
                p_item = product_list[choice]
                if p_item[1] < saving:
                    saving -= p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，还剩%s'%saving)
                print(p_item[0],':',p_item[1])
            else:
                print('没有这个商品')
            pass
        elif choice == 'q':
            print('------------您已经购买如下商品------------')
            for i in shopping_car:
                print(i[0],':',i[1])
            print('您还剩%s元钱'%saving)
            break
        else:
            print('input invalid')
