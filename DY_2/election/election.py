import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题

# 读取CSV文件
df = pd.read_csv('data1.csv')
df = df.dropna()
# 读取第一列
x = df.iloc[:, 0]
# 读取第二列
y = df.iloc[:, 1]

# 绘制曲线
plt.plot(x, y)
plt.xlabel('节点数量')
plt.ylabel('选举用时（秒）')
plt.title('可用节点数量与选举用时的关系图')
plt.ylim(0, 210)  # 设置y轴范围，确保可以看到逼近200的效果
plt.show()
