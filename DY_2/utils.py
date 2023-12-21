
import numpy as np
import pandas as pd

# # 创建x轴上的点（例如：从1到100）
# x = np.linspace(1, 100, 400)
#
# # 定义一个函数，使其从5开始逐渐逼近200
# # 使用对数函数并调整参数以符合需求
# y = 195 / np.log(100) * np.log(x) + 5
# 读取data.csv文件
# data = np.loadtxt('data.csv', delimiter=',')

# 设置x轴，y轴
# x = data[:, 0]
# y = data[:, 1]

# 设置X每一行的数据，Y每一行的数据在小数点后5位
# x = np.around(x, 5)
# y = np.around(y, 5)

# 保存数据
# np.savetxt('data1.csv', np.c_[x, y], delimiter=',')

# 读取CSV文件 第一行为列名
df = pd.read_csv('../data.csv', header=None)  # 替换'your_file.csv'为你的文件名

# 将每列的数据格式化为小数点后五位
for column in df.columns:
    df[column] = df[column].apply(lambda x: round(x, 5))

# 保存修改后的数据到新的CSV文件
df.to_csv('data1.csv', index=False)  # 'modified_file.csv'是新文件的名字


