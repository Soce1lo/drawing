import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
# plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

# 设置x轴的范围从0到100
x = np.linspace(0, 100, 100)

# 使用一个指数衰减函数，使得曲线从95开始减小到5
y = 90 * np.exp(-0.05 * x) + 5

# 绘制曲线
plt.plot(x, y, label='节点资源利用率', color='g')

# 绘制y=95和y=5的虚线
plt.axhline(y=95, color='r', linestyle='--', label='利用率95%')
plt.axhline(y=5, color='b', linestyle='--', label='利用率5%')

# 添加图例
plt.legend()

# 设置轴标签和标题
plt.xlabel('节点数')
plt.ylabel('资源利用率(%)')
plt.title('节点数与资源利用率的关系图')

# 显示图表
plt.show()
