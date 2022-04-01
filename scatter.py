import os
import numpy as np
import matplotlib.pyplot as plt

def scatter(s):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # matplotlib画图中中文显示会有问题，需要这两行设置默认字体

    plt.xlabel('重量')
    plt.ylabel('价值')
    plt.xlim(xmax=200, xmin=0)
    plt.ylim(ymax=150, ymin=0)
    daten = open('./data/' + s, "r")
    lines = daten.readlines()
    list = []
    for i in lines:
        list.append(i.strip().split(' '))
    daten.close()
    # print(list)
    f = []
    w = []
    v = []
    x = []
    y = []
    for i in list:
        for b in i:
            f.append(b)
    # print(f)
    for i in range(len(f)):
        if i == 0:
            c = int(f[i])
        elif i == 1:
            n = int(f[i])
        elif i > 1 and i % 2 == 0:
            w.append(int(f[i]))
        elif i > 1 and i % 2 == 1:
            v.append(int(f[i]))
    # vw(c,n,w,v,x,y)
    colors = 'blue'  #  点的颜色
    area = np.pi * 3**2 # 点面积
    # for i in range(len(w)):
    plt.scatter(w, v, s=area, c=colors, alpha=0.1, label=' ')
    plt.legend()
    plt.yticks(())
    plt.title('散点图')
    plt.savefig('./picture/'+ s +'.jpg')  # 保存图片
    plt.show()
