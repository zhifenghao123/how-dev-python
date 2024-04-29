import pandas as pd
import numpy as np


def generate_label_for_df_data3():
    """
    切分数据
    :return:
    """

    # 假设的DataFrame
    df = pd.DataFrame({
        'user_id': ['User1', 'User2', 'User3', 'User4', 'User5'],
        'score1': [0.8, 0.7, 0.6, 0.5, 0.4],
        'score2': [0.3, 0.4, 0.2, 0.5, 0.6],
        'total_amt': [200, 200, 300, 400, 500],
        'part_amt': [15, 25, 50, 150, 200]
    })

    # 规则列表
    rules = [
        {'label': 'Label_1', 'feature': 'score1', 'threshold': 0.1},
        {'label': 'Label_2', 'feature': 'score2', 'threshold': 0.4},
        {'label': 'Label_3', 'feature': 'score1', 'threshold': 0.6},
        {'label': 'Label_4', 'feature': 'score2', 'threshold': 0.8},
    ]

    # 初始化标签列
    df['label'] = 'Unknown'

    # 标记哪些行已经被处理过
    processed_rows = set()

    # 存储每个规则计算出的切分边界值
    cutoffs = []

    # 对每个规则进行处理
    for rule in rules:
        label = rule['label']
        feature = rule['feature']
        threshold = rule['threshold']

        # 排除之前已经处理过的行
        remaining_df = df[~df.index.isin(processed_rows)].copy()

        # 如果remaining_df为空，则跳过当前规则
        if remaining_df.empty:
            continue

        # 根据当前规则的特征对数据进行排序（降序）
        remaining_df.sort_values(by=feature, ascending=False, inplace=True)

        # 计算累积值
        cumulative_total_amt = remaining_df['total_amt'].cumsum()
        cumulative_part_amt = remaining_df['part_amt'].cumsum()
        ratio_series = cumulative_part_amt / cumulative_total_amt

        score_cutoff = None
        # 遍历 ratio_series，逐个检查是否大于阈值
        for index, ratio in ratio_series.items():
            if ratio > threshold:
                # 找到第一个大于 threshold 的记录，并结束处理
                break
            else:
                # 如果ratio_series中所有值都不大于threshold，则不执行break，继续到else块
                df.loc[index, 'label'] = label
                processed_rows.update({index})
                score_cutoff = remaining_df.loc[index, feature]
                if ratio == threshold:
                    break
        cutoffs.append({
            "label": label,
            "cutoff_var": feature,
            "cutoff_value": score_cutoff
        })

    print(df)

    # 显示切分边界值
    print("Cutoff values:")
    for cutoff in cutoffs:
        print(cutoff)


if __name__ == '__main__':
    # generate_label_for_df_data()
    # generate_label_for_df_data2()
    generate_label_for_df_data3()
