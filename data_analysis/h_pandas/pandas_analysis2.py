import pandas as pd
import numpy as np


def generate_df_data():
    """"
    生成Dataframe
    """
    # 假设这是你的DataFrame
    df = pd.DataFrame({
        'cmid': [1, 2, 3, 4, 5],
        'col1': ['A', 'B', 'A', 'C', 'A'],
        'col2': [10, 20, 30, 40, 50],
        'col3': ['X', 'Y', 'Z', 'X', 'Y']
    })
    return df


def generate_label_for_df_data(df_data):
    """
    未指定的Dataframe数据的 每一行打上标签
    :param df_data:
    :return:
    """
    # condition_expr1 = "col1 == 'A'"
    # condition_expr2 = "col1 ！= 'A' and col2 <= 30"
    # condition_expr3 = "col3 == 'Y' or col3 == 'Z'"

    condition_exprs = [
        "col1 == 'A'",
        "col1 != 'A' and col2 <= 30",
        "col3 == 'Y' or col3 == 'Z'"
        # ... 可能还有其他条件表达式
    ]
    labels = [
        'Label_1',
        'Label_2',
        'Label_3'
        # ... 对应每个条件表达式的标签
    ]

    # 确保条件表达式和标签的数量匹配
    assert len(condition_exprs) == len(labels), "条件表达式和标签的数量必须匹配"

    # 使用列表推导式来创建lambda函数列表
    conditions = [lambda row, expr=expr: eval(expr, {'__builtins__': None}, row.to_dict())
                  for expr in condition_exprs]

    # 使用np.select来设置condition_result列
    df_data['condition_result'] = np.select(
        [df_data.apply(cond, axis=1) for cond in conditions],
        labels,
        default='Unknown'  # 如果都不满足，则使用默认值
    )


if __name__ == '__main__':
    df_data = generate_df_data()
    generate_label_for_df_data(df_data=df_data)
    print(df_data)
