import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题


def sync_time():
    x = list(range(1, 16))
    # 异步更新
    y1 = [30.0, 60.0, 70.0, 100.0, 160.0, 200.0, 240.0, 304.0, 390.0, 420.0, 470.0, 510.0, 560.0, 590.0, 640.0]
    # 同步更新
    y2 = [60.0, 70.0, 94.0, 150.0, 230.0, 270.0, 430.0, 470.0, 490.0, 560.0, 630.0, 690.0, 750.0, 780.0, 820.0]
    # 混合更新
    y3 = [40.0, 50.0, 66.0, 84.0, 120.0, 148.0, 188.0, 220.0, 250.0, 290.0, 320.0, 361.0, 390.0, 417.0, 452.0]
    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='异步更新')
    plt.plot(x, y2, 'b', marker='^', markersize=5, label='同步更新')
    plt.plot(x, y3, 'g', marker='D', markersize=5, label='混合更新')
    # plt.title('The result of Average delay time')  # 折线图标题
    plt.xlabel('节点数量')  # x轴标题
    plt.ylabel('计算时间（秒）')  # y轴标题
    plt.tick_params()  # 坐标轴字号
    # 绘制图例
    # plt.legend(['RFSU', 'TTA'])
    plt.legend()
    plt.show()


def sync_network():
    x = list(range(1, 16))
    # 异步更新
    y1 = [30.0, 60.0, 70.0, 100.0, 160.0, 200.0, 240.0, 304.0, 390.0, 420.0, 470.0, 510.0, 560.0, 590.0, 640.0]
    # 同步更新
    y2 = [60.0, 70.0, 94.0, 150.0, 230.0, 270.0, 430.0, 470.0, 490.0, 560.0, 630.0, 690.0, 750.0, 780.0, 820.0]
    # 混合更新
    y3 = [40.0, 50.0, 66.0, 84.0, 120.0, 148.0, 188.0, 220.0, 250.0, 290.0, 320.0, 361.0, 390.0, 417.0, 452.0]
    # 绘制折线图，添加数据点，设置点的大小
    # * 表示绘制五角星；此处也可以不设置线条颜色，matplotlib会自动为线条添加不同的颜色
    plt.plot(x, y1, 'r', marker='o', markersize=5, label='同步更新')
    plt.plot(x, y2, 'b', marker='^', markersize=5, label='异步更新')
    plt.plot(x, y3, 'g', marker='D', markersize=5, label='混合更新')
    plt.title('不同更新模式节点数量对总计算时间的影响')  # 折线图标题
    plt.xlabel('节点数量')  # x轴标题
    plt.ylabel('计算时间')  # y轴标题
    plt.tick_params()  # 坐标轴字号
    plt.legend()
    plt.show()


sync_time()
