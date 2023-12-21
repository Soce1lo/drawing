import pandas as pd

# 读取CSV文件
df = pd.read_csv('data1.csv', header=None)

# 将第一列的字符串切割，仅保留最后的8位
df[0] = df[0].apply(lambda x: str(x)[-8:])
# 删除第二列
df = df.drop(columns=[1])

# 将结果保存到新的CSV文件中
df.to_csv('data1_modified.csv', index=False, header=False)


