import random

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
font = {'weight': 'normal',
        'size': 20,
        }


def chart1():
    x = list(range(1, 16))
    # x.sort()
    # random_list = [random.randint(60, 900) for _ in range(15)]
    # random_list.sort()
    # print(random_list)
    # start_value = random.randint(10, 100)  # 生成一个1到100之间的随机整数
    # increment_range = (40, 80)  # 递增的随机范围
    #
    # # 生成包含15个随机整数的列表，逐次增大，间隔在20到60之间随机
    # random_list = [start_value + i * random.randint(*increment_range) for i in range(15)]
    # random_list.sort()
    # # 打印生成的随机整数列表
    # print(random_list)
    y1 = [17, 39, 75, 129, 171, 239, 257, 269, 359, 425, 437, 479, 511, 589, 617]  # 多云
    y2 = [29, 85, 123, 161, 229, 293, 425, 449, 546, 614, 669, 705, 749, 769, 827]  # 单体
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='多云训练模式')
    plt.plot(x, y2, 'g', marker='D', markersize=5, label='单机训练模式')
    plt.xlabel('训练轮次', font)  # x轴标题
    plt.ylabel('模型训练时间', font)  # y轴标题
    plt.tick_params(labelsize=15)  # 坐标轴字号
    plt.legend(['多云训练模式', '单机训练模式'])
    plt.legend(fontsize=15)
    plt.tight_layout()
    plt.show()


def chart2():
    x = list(range(1, 16))
    # x.sort()
    # random_list = [random.randint(60, 900) for _ in range(15)]
    # random_list.sort()
    # print(random_list)
    # start_value = random.randint(10, 100)  # 生成一个1到100之间的随机整数
    # increment_range = (40, 80)  # 递增的随机范围
    #
    # # 生成包含15个随机整数的列表，逐次增大，间隔在20到60之间随机
    # random_list = [start_value + i * random.randint(*increment_range) for i in range(15)]
    # random_list.sort()
    # # 打印生成的随机整数列表
    # print(random_list)
    y1 = [0.114, 0.217, 0.265, 0.317, 0.341, 0.398, 0.452, 0.499, 0.548, 0.589, 0.620, 0.657, 0.689, 0.710, 0.747]  # 多云
    y2 = [0.089, 0.148, 0.184, 0.232, 0.279, 0.339, 0.376, 0.399, 0.428, 0.479, 0.503, 0.538, 0.579, 0.599, 0.636]  # 单体
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='多云训练模式')
    plt.plot(x, y2, 'g', marker='D', markersize=5, label='单机训练模式')
    plt.xlabel('训练轮次', font)  # x轴标题
    plt.ylabel('模型精度', font)  # y轴标题
    plt.tick_params(labelsize=15)  # 坐标轴字号
    plt.legend(['多云训练模式', '单机训练模式'])
    plt.legend(fontsize=15)
    plt.tight_layout()
    plt.show()


chart2()
