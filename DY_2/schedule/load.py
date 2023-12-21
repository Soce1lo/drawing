import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
# plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

# 设置X轴的值
x_values = [1, 2, 3, 4, 5]

# 设置固定的随机数种子
np.random.seed(0)

# 生成红蓝柱的高度，范围在0.2到1之间
heights_red = [0.88, 0.34, 0.67, 0.12, 0.89]
heights_blue = [0.58, 0.66, 0.55, 0.61, 0.74]

# 设置柱的宽度
bar_width = 0.6

# 创建柱状图
plt.bar(x_values, heights_red, bar_width, label='不使用负载均衡', color='r', alpha=0.5)
plt.bar(x_values, heights_blue, bar_width, label='使用负载均衡', color='b', alpha=0.5)

# 给红柱画上折线图
plt.plot(x_values, heights_red, 'r--', marker='o')
plt.plot(x_values, heights_blue, 'b--', marker='^')

# 设置X轴的刻度
plt.xticks(x_values)

# 添加图例
plt.legend()

# 设置轴标签和标题
plt.xlabel('节点id')
plt.ylabel('节点负载（%）')
plt.title('节点负载情况')

# 显示图表
plt.show()
