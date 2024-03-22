import pandas as pd

def dynamic_construct_dataframe():
    """
    动态构造 DataFrame
    :return:
    """
    feature_binnings = [
        {'feature_name': 'feature1', 'feature_val': 'val1'},
        {'feature_name': 'feature2', 'feature_val': 'val2'},
        # ... 其他feature_binning项
    ]

    indicators = [
        {'indicator_code': 'code1', 'indicator_val': 'valA'},
        {'indicator_code': 'code2', 'indicator_val': 'valB'},
        # ... 其他biz_indicator项
    ]

    # 初始化结果列表
    result_list = []

    # 两层循环遍历所有的feature_binning和biz_indicator
    for feature_binning in feature_binnings:
        # 初始化一个字典来存储当前行的数据
        row_data = {
            'feature_name': feature_binning['feature_name'],
            'feature_val': feature_binning['feature_val']
        }

        # 遍历biz_indicators，将它们的indicator_code作为键，indicator_val作为值，添加到row_data中
        for indicator in indicators:
            row_data[indicator['indicator_code']] = indicator['indicator_val']

            # 将row_data添加到结果列表中
        result_list.append(row_data)

        # 打印结果列表查看内容
    print(result_list)

    print("____________________________")
    # 使用上面的result_list创建DataFrame
    df = pd.DataFrame(result_list)
    # 打印DataFrame查看内容
    print(df)

def dynamic_construct_dataframe2():
    # 假设这是你的feature_binnings数据
    feature_binnings = [
        [
            {'name': 'feature1', 'value': 'A'},
            {'name': 'feature2', 'value': 'B'},
            {'name': 'feature3', 'value': 2}
        ],
        [
            {'name': 'feature1', 'value': 'A'},
            {'name': 'feature4', 'value': 100},
            {'name': 'feature5', 'value': 'C'},
            {'name': 'feature7', 'value': 90000}
        ],
        [
            {'name': 'feature2', 'value': 'C'}
        ]
    ]

    indicators = [
        [
            {'indicator_name': "indicator1", 'indicator_val': 20},
            {'indicator_name': "indicator2", 'indicator_val': 0.9}
        ],[
            {'indicator_name': "indicator1", 'indicator_val': 80},
            {'indicator_name': "indicator2", 'indicator_val': 0.6}
        ],[
            {'indicator_name': "indicator1", 'indicator_val': 68},
            {'indicator_name': "indicator2", 'indicator_val': 0.5}
        ]
    ]

    # 初始化一个空的DataFrame，列数取决于最大的内部列表长度
    max_length = max(len(binning) for binning in feature_binnings)
    df = pd.DataFrame(index=range(len(feature_binnings)), columns=range(max_length + 2))

    # 遍历每个内部列表，填充DataFrame
    for i, binning in enumerate(feature_binnings):
        for j, item in enumerate(binning):
            # 填充非空值，忽略超出当前行长度的索引
            if j < max_length:
                df.iat[i, j] = f"{item['name']}={item['value']}"
        indicator = indicators[i]
        for k, item in enumerate(indicator):
            df.iat[i, max_length + k] = item['indicator_val']


    # 删除包含NaN的列，只保留有数据的列
    df = df.dropna(axis=1, how='all')

    # 重新命名列以符合您的要求（如果需要）
    # df.columns = [f"feature_{col + 1}" for col in df.columns]

    # 显示最终的DataFrame
    print(df)

def dynamic_filter_dataframe():
    """
    动态筛选 DataFrame
    :return:
    """
    # 假设这是你的DataFrame
    df = pd.DataFrame({
        'cmid': [1, 2, 3, 4, 5],
        'col1': ['A', 'B', 'A', 'C', 'A'],
        'col2': [10, 20, 30, 40, 50],
        'col3': ['X', 'Y', 'Z', 'X', 'Y']
    })

    # 这是你的条件集合
    conditions = [
        ('col1', ['A', 'C']),
        ('col2', [20, 40]),
        ('col3', ['X'])
    ]

    # 初始化一个空掩码
    mask = None

    # 遍历每个条件，累积掩码
    for col_name, values in conditions:
        condition_mask = df[col_name].isin(values)
        if mask is None:
            mask = condition_mask
        else:
            mask &= condition_mask

            # 使用累积的掩码来筛选出满足所有条件的cmid
    selected_cmids = df.loc[mask, 'cmid'].tolist()

    # 打印满足条件的cmid集合
    print(selected_cmids)

if __name__ == '__main__':

    # dynamic_construct_dataframe()
    dynamic_construct_dataframe2()
    #dynamic_filter_dataframe()
