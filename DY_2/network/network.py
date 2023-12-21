import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def loss():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题
    x = [0.0, 0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2]

    # 异步更新
    y1 = [0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1]
    y1.reverse()
    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='网络质量')
    # plt.title('The result of Average delay time')  # 折线图标题
    plt.xlabel('丢包率')  # x轴标题
    plt.ylabel('网络环境质量（%）')  # y轴标题
    # 设置x轴和y轴的范围
    plt.xlim([0, 1.2])
    plt.ylim([0, 1.1])
    # 绘制图例
    # plt.legend(['RFSU', 'TTA'])
    plt.legend()
    plt.show()


loss()
