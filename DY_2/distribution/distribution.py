import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取CSV文件
df = pd.read_csv('class_counts_by_client.csv')

# 将每一列保存为一个数组
data = [df[col].values for col in df.columns[1:]]

# 创建一个y轴的位置数组
y = np.arange(len(df.columns[1:]))

# 设置柱状图的高度
bar_height = 0.1

# 绘制每个客户的柱状图
for i in range(len(df['Client'])):
    plt.barh(y + i*bar_height, data[i], height=bar_height, label=df['Client'][i])

# 设置y轴的标签
plt.yticks(y + bar_height, df.columns[1:])

# 添加图例
plt.legend()

# 显示图形
plt.show()