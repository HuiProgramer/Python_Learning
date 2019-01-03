# !/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author   : HuiProgramer
#@DateTime : 2018/7/7 17:35
#@Email    : 1712817197@qq.com
#@File     : 3menu_short.py
#@Software : PyCharm
menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                '渣打银行':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                'apple':{},
            },
        },
        '昌平': {
             "沙河":{
                 '老男孩':{},
                 '阿泰包子':{},
             },
            "大通宛":{
                "链家":{},
                "我爱我家":{},
            },
            "回龙观":{},
        },
        '海淀':{
            "五道口":{
                '谷歌':{},
                '网易':{},
                'Sohu':{},
                'Sogo':{},
                '快手':{},
            },
        '中关村':{
                "youku":{},
                "Iqiyi":{},
                "汽车之家":{},
                "新东方":{},
                "QQ":{},
        },
        },
    },
    '上海':{
      '浦东':{
          "陆家嘴":{
              "CICC":{},
              "高盛":{},
              "摩根":{}
          },
          "外滩":{},
      },
    "闵行":{},
    "静安":{},
    },
    '山东':{
        "济南":{},
        "德州":{
            "乐陵":{
              "丁务镇":{},
            },
            "平原":{},
        },
        "青岛":{},
    },

}
current_layer = menu
parent_layers = []
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if len(parent_layers) == 0:
            print("last layer")
        else:
            current_layer = parent_layers.pop()
    elif choice == 'q':
        current_layer = menu
    else:
        print("无此项")

