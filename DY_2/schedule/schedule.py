import matplotlib.pyplot as plt
import numpy as np
import pandas

# 设置x轴的范围从1到100
# x = np.linspace(1, 100, 100)
# 使用一个指数衰减函数来表示y值从95开始逐渐逼近5
# y = 95 - 90 * np.exp(-0.05 * (x - 1))
# # 让y中的数倒序排列
# y = y[::-1]
# # 将x，y写入csv文件
# np.savetxt("schedule.csv", np.column_stack((x, y)), delimiter=",", fmt='%f')

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题

df = pandas.read_csv("schedule.csv", header=None)
x = df.iloc[:, 0]
y = df.iloc[:, 1]
# 绘制曲线
plt.plot(x, y, label='资源利用率')

# 绘制y=95和y=5的虚线
plt.axhline(y=95, color='r', linestyle='--', label='95%')
plt.axhline(y=5, color='b', linestyle='--', label='5%')

# 添加图例
plt.legend()

# 设置轴标签和标题
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Curve Decaying from y=95 to y=5 as x increases from 1 to 100')

# 显示图表
plt.show()
