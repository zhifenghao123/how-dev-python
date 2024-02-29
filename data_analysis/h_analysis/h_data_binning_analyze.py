import pandas as pd

def equal_distance_binning(df_data):
    """
    等距分箱
    :param df_data:
    :return:
    """
    # 定义分箱的边界
    bins = [0, 20, 30, 40, 50, 60, 70, 80]

    # 使用pandas.cut()进行分箱
    # 注意：bins参数定义了分箱的边界，right参数决定了区间是否包含边界值（默认为True）
    df_data['age_bin'] = pd.cut(df_data['age'], bins=bins, right=False)

    # 统计每个分箱中的数据数量
    bin_counts = df_data['age_bin'].value_counts()

    print("等距分箱结果如下----------")
    print("（1）等距分箱概览：")
    # 打印结果
    print(bin_counts)
    print("（2）等距分箱明细：")
    for bin, group in df_data.groupby('age_bin'):
        print(f"Bin: {bin}, Data: {group['age'].tolist()}")

def equal_frequency_binning(df_data):
    """
    等频分箱
    :param df_data:
    :return:
    """
    # 使用pandas.qcut()进行等频分箱
    # q参数定义了分箱的数量
    df_data['age_qbin'] = pd.qcut(df_data['age'], q=4, labels=False)

    # 统计每个分箱中的数据数量
    qbin_counts = df_data['age_qbin'].value_counts()

    print("等频分箱结果如下----------")
    print("（1）等频分箱概览：")
    # 打印结果
    print(qbin_counts)
    print("（2）等频分箱明细：")
    for bin, group in df_data.groupby('age_qbin'):
        print(f"Bin: {bin}, Data: {group['age'].tolist()}")


if __name__ == '__main__':
    data = {
        'age': [23, 45, 56, 22, 34, 67, 22, 33, 55, 44]
    }
    df_data = pd.DataFrame(data)

    equal_distance_binning(df_data)

    equal_frequency_binning(df_data)


