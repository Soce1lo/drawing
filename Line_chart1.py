import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
font = {'weight': 'normal',
        'size': 20,
        }
# x = list(range(3, 14))
# y1 = [0.92, 0.88, 0.89, 0.83, 0.80, 0.74, 0.75, 0.71, 0.70, 0.67, 0.64]
# y2 = [0.81, 0.78, 0.71, 0.66, 0.62, 0.60, 0.59, 0.54, 0.47, 0.44, 0.39]
# plt.plot(x, y1, 'r', marker='o', markersize=5, label='跨云协同模块数据推送模式')
# plt.plot(x, y2, 'g', marker='D', markersize=5, label='传统节点数据推送模式')
# plt.xlabel('参与协同的边缘云数量', font)  # x轴标题
# plt.ylabel('使用预先推送数据的比例', font)  # y轴标题
# plt.tick_params(labelsize=15)  # 坐标轴字号
#
# legend = plt.legend(['跨云协同模块数据推送模式', '传统节点数据推送模式'])
# plt.legend(fontsize=15)
# plt.tight_layout()
#
# plt.show()

import matplotlib.pyplot as plt

# 创建数据
training_epochs = list(range(1, 21, 2))
time_in_seconds = [5, 20, 40, 60, 80, 100, 120, 140, 160, 200]

# 创建折线图
plt.plot(time_in_seconds, training_epochs, marker='o', linestyle='-', color='b')

# 添加标题和标签
plt.title('训练轮次 vs. 时间')
plt.xlabel('时间 (秒)')
plt.ylabel('训练轮次')

# 显示网格线
plt.grid(True)

# 显示图形
plt.show()

