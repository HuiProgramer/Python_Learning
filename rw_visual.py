import matplotlib.pyplot as plt
from random_walk import RandomWalk

#创建一个RandomWalk实例，并将其包含的点都绘制出来
#只要程序处于活动状态，就不断模拟漫步
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置绘图窗口大小
    plt.figure(dpi = 128, figsize = (10, 6))
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_number, cmap = plt.cm.Blues, edgecolor = 'none', s=1)
    #突出起点和终点
    plt.scatter(0, 0, c = 'green', edgecolor = 'none',s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolor = 'none', s = 100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #保存图片
    plt.savefig('randomwalk.png',bbox_inches = 'tight')
    plt.show()
    keep_running = input("Make another walk?(Y/n):")
    if keep_running == 'n':
        break