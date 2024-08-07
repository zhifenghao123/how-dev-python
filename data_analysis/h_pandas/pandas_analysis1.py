import pandas as pd
import numpy as np

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

def dynamic_construct_dataframe3(feature_num, indicator_num):

    # 初始化一个空的DataFrame
    df = pd.DataFrame()

    # 构造特征列
    for i in range(1, feature_num + 1):
        df[f'feature_{i}_name'] = [f'Feature{i}_Name'] * len(df)  # 假设每个特征名都是一样的
        df[f'feature_{i}_val'] = [f'Feature{i}_Value'] * len(df)  # 假设每个特征值都是一样的
        # 如果需要不同的值，可以用其他逻辑生成，例如随机数等

    # 构造指标列
    for i in range(1, indicator_num + 1):
        df[f'indicator{i}'] = [f'Indicator{i}'] * len(df)  # 假设每个指标值都是一样的
        # 如果需要不同的值，可以用其他逻辑生成，例如随机数等

    # 定义特征名的码值列表
    feature_1_names = ['Feature1_NameA', 'Feature1_NameB', 'Feature1_NameC']
    feature_2_names = ['Feature2_NameD', 'Feature2_NameE']
    feature_3_names = ['Feature3_NameF', 'Feature3_NameG', 'Feature3_NameH']

    # 假设DataFrame的行数
    num_rows = 10

    # 构造特征列
    for i in range(1, feature_num + 1):
        if i == 1:
            # 对于feature_1_name，随机选择三个码值中的一个
            df[f'feature_{i}_name'] = np.random.choice(feature_1_names, size=num_rows)
        elif i == 2:
            # 对于feature_2_name，随机选择两个码值中的一个
            df[f'feature_{i}_name'] = np.random.choice(feature_2_names, size=num_rows)
        else:
            # 对于feature_3_name，随机选择三个码值中的一个
            df[f'feature_{i}_name'] = np.random.choice(feature_3_names, size=num_rows)

            # 生成不同的特征值，这里使用随机数作为示例
        df[f'feature_{i}_val'] = np.random.rand(num_rows)

        # 构造指标列，这里也使用随机数作为示例
    for i in range(1, indicator_num + 1):
        df[f'indicator{i}'] = np.random.rand(num_rows)

        # 显示最终的DataFrame
    print(df)
    return df


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

def merge_dataframe():
    import pandas as pd
    import numpy as np

    # 假设特征列数为feature_num，指标列数为indicator_num
    feature_num = 3  # 特征列数
    indicator_num = 2  # 指标列数

    # 构造df1和df2
    np.random.seed(0)  # 设置随机种子以便结果可复现

    # 特征列
    features = [f'feature{i}' for i in range(1, feature_num + 1)]
    # 指标列
    indicators = [f'biz_indicator{i}' for i in range(1, indicator_num + 1)]

    # 构造df1
    df1_data = {col: np.random.rand(10) for col in features + indicators}
    df1 = pd.DataFrame(df1_data)

    # 构造df2
    df2_data = {col: np.random.rand(10) for col in features + indicators}
    df2 = pd.DataFrame(df2_data)

    # 合并df1和df2
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # 提取特征列
    feature_cols = features

    # 提取指标列
    indicator_cols = indicators

    # 给指标列添加前缀，区分来自df1还是df2
    merged_df = merged_df.join(df1[indicator_cols].add_prefix('df1_'), on=merged_df.index)
    merged_df = merged_df.join(df2[indicator_cols].add_prefix('df2_'), on=merged_df.index)

    # 删除原始指标列，因为它们现在已经被重命名了
    merged_df.drop(indicator_cols, axis=1, inplace=True)

    # 计算指标值的diff并添加到DataFrame中
    diff_cols = [f'df1_df2_{col}' for col in indicator_cols]
    for col, diff_col in zip(indicator_cols, diff_cols):
        df1_col = f'df1_{col}'
        df2_col = f'df2_{col}'
        merged_df[diff_col] = merged_df[df1_col] - merged_df[df2_col]

        # 重新排序列，保持特征列顺序不变，然后是指标列，最后是diff列
    all_cols = feature_cols + [f'df1_{col}' for col in indicator_cols] + [f'df2_{col}' for col in
                                                                          indicator_cols] + diff_cols
    merged_df = merged_df[all_cols]

    # 打印合并后的DataFrame
    print(merged_df)

def merge_dataframe_new(df_data1, df_data2, feature_num):
    # 获取特征列名
    feature_columns = df_data1.columns[:2 * feature_num]

    # 获取指标列名，即除了特征列之外的所有列
    indicator_columns = df_data1.columns[2 * feature_num:]
    # 创建一个空的字典，用于存储新DataFrame的列
    new_data = {}
    for feature_column in feature_columns:
        new_data[feature_column] = df_data1[feature_column]

    # 遍历指标列，计算差值，并将新列名和新值添加到新字典中
    for indicator_column in indicator_columns:
        new_data[f'df1_{indicator_column}'] = df_data1[indicator_column]
        new_data[f'df2_{indicator_column}'] = df_data2[indicator_column]
        indicator_diff_column = f'df1_df2_{indicator_column}'
        temp1 = df_data1[indicator_column]
        temp2 = df_data2[indicator_column]
        temp3 = temp1 - temp2
        new_data[indicator_diff_column] = df_data1[indicator_column] - df_data2[indicator_column]  # 计算差值

    merged_df = pd.DataFrame(new_data)

    return merged_df

if __name__ == '__main__':
    feature_num = 3
    indicator_num = 2
    # dynamic_construct_dataframe()
    # dynamic_construct_dataframe2()
    df_data1 = dynamic_construct_dataframe3(feature_num, indicator_num)
    df_data2 = dynamic_construct_dataframe3(feature_num, indicator_num)
    merged_df = merge_dataframe_new(df_data1, df_data2, feature_num)
    print(merged_df)


    #dynamic_filter_dataframe()
    #merge_dataframe()
