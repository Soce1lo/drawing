import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题

# 读取CSV文件
df = pd.read_csv('data1_modified.csv',header=None)

# 删除包含缺失值的行
df = df.dropna()

# 设置X轴，Y轴1，Y轴2
x = df[0]
y1 = df[1]
y2 = df[2]

# 绘制折线图
plt.plot(x, y1, label='协同')
plt.plot(x, y2, label='不协同')

# 设置图例
plt.legend()
# plt.title('训练方式对比')
# plt.xlabel('时间 (秒)')
plt.ylabel('资源利用率 (%)')

# 调整X轴标签的显示方式
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()

# 显示图形
plt.show()