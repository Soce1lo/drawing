import matplotlib.pyplot as plt


# 本部分为5.3.2三张折线图的生成代码
def chart1():
    # 1.成功调度率与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    x = list(range(5, 21))
    # SMT
    y1 = [0.99, 0.99, 0.97, 0.96, 0.94, 0.94, 0.93, 0.92, 0.93, 0.92, 0.92, 0.91, 0.9, 0.89, 0.88, 0.87]
    # PAS
    y2 = [0.93, 0.92, 0.9, 0.9, 0.88, 0.86, 0.84, 0.85, 0.83, 0.83, 0.83, 0.82, 0.77, 0.8, 0.75, 0.74]
    # RFDS
    y3 = [0.96, 0.94, 0.93, 0.93, 0.93, 0.9, 0.92, 0.9, 0.88, 0.88, 0.87, 0.85, 0.84, 0.82, 0.8, 0.78]
    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='SMT')
    plt.plot(x, y2, 'g', marker='D', markersize=5, label='PAS')
    plt.plot(x, y3, 'b', marker='^', markersize=5, label='RFSD')
    # plt.title('The result of successful scheduling ratio')  # 折线图标题
    plt.xlabel('Number of Flows', font)  # x轴标题
    plt.ylabel('Successful Scheduling Ratio', font)  # y轴标题
    plt.tick_params(labelsize=20)  # 坐标轴字号
    # 绘制图例
    # legend = plt.legend(['SMT', 'PAS', 'RFSD'])
    plt.legend(fontsize=20)
    plt.tight_layout()
    plt.savefig("./figures/figure5-2.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart2():
    # 2.紧急流成功调度率与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    x = list(range(5, 21))
    # SMT
    y1 = [0.99, 1, 0.97, 0.96, 0.95, 0.94, 0.93, 0.94, 0.93, 0.93, 0.92, 0.91, 0.9, 0.9, 0.89, 0.88]
    # PAS
    y2 = [0.93, 0.92, 0.89, 0.9, 0.88, 0.88, 0.874, 0.865, 0.843, 0.841, 0.841, 0.832, 0.811, 0.792, 0.752, 0.753]
    # RFDS
    y3 = [0.99, 1.0, 1.0, 0.98, 0.98, 0.97, 0.98, 0.97, 0.97, 0.96, 0.96, 0.95, 0.95, 0.94, 0.93, 0.92]
    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='SMT')
    plt.plot(x, y2, 'g', marker='D', markersize=5, label='PAS')
    plt.plot(x, y3, 'b', marker='^', markersize=5, label='RFSD')
    # plt.title('The result of No delay flow successful scheduling ratio')  # 折线图标题
    plt.xlabel('Number of Flows', font)  # x轴标题
    plt.ylabel('No Delay Flow Successful \nScheduling Ratio', font)  # y轴标题
    plt.tick_params(labelsize=20)  # 坐标轴字号
    # 绘制图例
    # plt.legend(['SMT', 'PAS', 'RFSD'])
    plt.legend(fontsize=20)
    # 保存并显示
    # plt.show()
    plt.tight_layout()
    plt.savefig("./figures/figure5-3.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart3():
    # 3.算法运行时间与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    x = list(range(5, 21))
    # SMT
    y1 = [3.0, 4.0, 6.0, 7.0, 7.0, 9.0, 10.0, 11.0, 13.0, 13.0, 13.0, 15.0, 18.0, 20.0, 23.0, 25.0]
    # PAS
    y2 = [2.0, 2.5, 3.0, 4.8, 5.6, 6.0, 4.2, 4.6, 5.2, 5.0, 5.6, 6.3, 7.4, 8.0, 7.5, 8.0]
    # RFDS
    y3 = [1.0, 1.0, 2.1, 1.8, 2.8, 3.2, 3.2, 2.1, 2.1, 4.0, 3.2, 5.0, 4.6, 4.1, 5.0, 6.0]
    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='SMT')
    plt.plot(x, y2, 'g', marker='D', markersize=5, label='PAS')
    plt.plot(x, y3, 'b', marker='^', markersize=5, label='RFSD')
    # plt.title('The result of running time')  # 折线图标题
    plt.xlabel('Number of Flows', font)  # x轴标题
    plt.ylabel('Running Time', font)  # y轴标题
    plt.tick_params(labelsize=20)  # 坐标轴字号
    # 绘制图例
    # plt.legend(['SMT', 'PAS', 'RFSD'])
    plt.legend(fontsize=20)
    # 保存并显示
    # plt.show()
    plt.tight_layout()
    plt.savefig("./figures/figure5-4.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart8():
    # 8.平均延迟时间与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    x = list(range(7, 22))
    # RFSU
    y1 = [30.0, 50.0, 60.0, 120.0, 180.0, 190.0, 240.0, 304.0, 390.0, 420.0, 470.0, 510.0, 500.0, 590.0, 640.0]
    # TTA
    y2 = [60.0, 70.0, 70.0, 100.0, 160.0, 210.0, 430.0, 470.0, 490.0, 560.0, 630.0, 690.0, 750.0, 780.0, 820.0]

    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='RFSU')
    plt.plot(x, y2, 'b', marker='^', markersize=5, label='TTA')
    # plt.title('The result of Average delay time')  # 折线图标题
    plt.xlabel('Number of Flows', font)  # x轴标题
    plt.ylabel('Average Delay Time', font)  # y轴标题
    plt.tick_params(labelsize=20)  # 坐标轴字号
    # 绘制图例
    # plt.legend(['RFSU', 'TTA'])
    plt.legend(fontsize=20)
    # 保存并显示
    # plt.show()
    plt.tight_layout()
    plt.savefig("./figures/figure5-9.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart9():
    # 9.抖动与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    x = list(range(7, 22))
    # RFSU
    y1 = [45.0, 53.0, 71.0, 121.0, 200.0, 240.0, 270.0, 331.0, 399.0, 425.0, 492.0, 520.0, 550.0, 600.0, 650.0]
    # TTA
    y2 = [66.0, 73.0, 69.0, 130.0, 220.0, 330.0, 400.0, 473.0, 500.0, 574.0, 670.0, 700.0, 780.0, 774.0, 902.0]

    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='RFSU')
    plt.plot(x, y2, 'b', marker='^', markersize=5, label='TTA')
    # plt.title('The result of Jitter')  # 折线图标题
    plt.xlabel('Number of Flows', font)  # x轴标题
    plt.ylabel('Jitter', font)  # y轴标题
    plt.tick_params(labelsize=20)  # 坐标轴字号
    # 绘制图例
    # plt.legend(['RFSU', 'TTA'])
    plt.legend(fontsize=20)
    # 保存并显示
    # plt.show()
    plt.tight_layout()
    plt.savefig("./figures/figure5-10.pdf", bbox_inches='tight')
    plt.show()
    plt.close()


def chart10():
    # 10.延迟流比率与流数量关系图
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 20,
            }
    x = list(range(7, 22))
    # RFSU
    y1 = [0.29, 0.32, 0.35, 0.33, 0.35, 0.37, 0.39, 0.41, 0.39, 0.38, 0.44, 0.43, 0.46, 0.47, 0.48]
    # TTA
    y2 = [0.29, 0.35, 0.39, 0.44, 0.49, 0.47, 0.5, 0.53, 0.52, 0.56, 0.58, 0.62, 0.64, 0.65, 0.67]

    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='RFSU')
    plt.plot(x, y2, 'b', marker='^', markersize=5, label='TTA')
    # plt.title('The result of Delay flow ratio')  # 折线图标题
    plt.xlabel('Number of Flows', font)  # x轴标题
    plt.ylabel('Delay Flow Ratio', font)  # y轴标题
    plt.tick_params(labelsize=20)  # 坐标轴字号
    # 绘制图例
    # plt.legend(['RFSU', 'TTA'])
    plt.legend(fontsize=20)
    # 保存并显示
    # plt.show()
    plt.tight_layout()
    plt.savefig("./figures/figure5-11.pdf", bbox_inches='tight')
    plt.show()
    plt.close()