import pandas as pd

# 读取CSV文件
csv_file = 'data1_modified.csv'
df = pd.read_csv(csv_file)

# 将StartDate列转换为日期时间格式（yyyy-m-d hh:mm:ss）
# df['StartDate'] = pd.to_datetime(df['StartDate'], format='%Y-%m-%d %H:%M:%S')
# print(df['StartDate'])
# 将ACC列的值（秒数）添加到StartDate列
# df['EndDate'] = df['StartDate'] + pd.to_timedelta(df['TrainingTime'], unit='S')
# df['EndDate'] = pd.to_datetime(df['EndDate'], format='%Y-%m-%d %H:%M:%S')
# print('df[EndDate]:', df['EndDate'])
# 将数据写入Excel文件
excel_file = 'data1_modified.xlsx'
df.to_excel(excel_file, index=False)

print(f'CSV文件 {csv_file} 已成功转换为Excel文件 {excel_file}')
