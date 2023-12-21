import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 生成一个10x10的随机数组，数值范围在0.1到0.9之间
data = np.random.uniform(0.1, 0.9, (10, 10))

# 生成一个随机的乘法因子，范围在0.5到0.9之间
factor = np.random.uniform(0.7, 0.95)



# 解决中文编码等问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决无法显示符号的问题

# 使用Seaborn绘制第一张热力图（原始数据）
plt.plot(1, 2, 1)  # 一行两列，第一张图
sns.heatmap(data, annot=True, cmap='coolwarm', linewidths=0.5, vmin=0.1, vmax=0.9)
plt.title("传统区域协同需求")

plt.show()

# 使用Seaborn绘制第二张热力图（经过随机放缩的数据）
plt.plot(1, 2, 2)  # 一行两列，第二张图
sns.heatmap(data * factor, annot=True, cmap='coolwarm', linewidths=0.5, vmin=0.1, vmax=0.9)
plt.title("云端跨域模块参与下区域协同需求")

# 显示图形
plt.show()
