import pandas as pd
import numpy as np

if __name__ == '__main__':
    # 示例数据
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-02-01', '2023-02-15', '2023-02-28', '2023-03-01'],
        'product': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
        'amount': [100, 150, 200, 50, 75, 125, 80]
    }

    # 创建DataFrame
    df = pd.DataFrame(data)

    print(df)
    print('----------------------')

    # 将'date'列转换为日期时间类型
    df['date'] = pd.to_datetime(df['date'])

    # 按照月份（月份的开始）分组，并计算每月的总金额、最大金额和最小金额
    monthly_grouped = df.groupby(pd.Grouper(key='date', freq='MS')).agg(
        total_amount=('amount', 'sum'),
        max_amount=('amount', 'max'),
        min_amount=('amount', 'min')
    ).reset_index()

    # 打印结果
    print(monthly_grouped)