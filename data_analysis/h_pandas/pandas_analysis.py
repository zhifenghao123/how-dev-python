import pandas as pd

# 创建一个包含分类数据的DataFrame对象
df = pd.DataFrame({'Dept': ['Sales', 'IT', 'Admin', 'Sales', 'Admin'], 'Salary': [5000, 6000, 7000, 5500, 7500]})

# 将Dept列转换为category类型
df['Dept'] = df['Dept'].astype('category')

# 使用groupby函数将DataFrame按Dept列分组，并对Salary列进行平均值聚合操作
grouped = df.groupby(['Dept']).mean()
print(grouped)