import os
import pandas as pd
from typing import List, Dict, Union


def simple_append_merge_mutil_csv_file(
        source_file_dir: str,
        merge_output_file: str,
        sort_config: List[Dict[str, bool]] = None
) -> None:
    """
    简单追加合并多个CSV文件到一个文件

    :param source_file_dir: 多个csv源文件所在的目录
    :param merge_output_file: 合并输出的csv文件
    :param sort_config: 排序配置列表，格式为[{"field": "field1", "ascending": True},{"field": "field2", "ascending": False}]
    :return: None
    """
    # 检查源文件目录是否存在
    if not os.path.exists(source_file_dir):
        print(f"源文件目录不存在: {source_file_dir}")
        raise FileNotFoundError(f"源文件目录不存在: {source_file_dir}")

    # 检查设定的输出文件名是不是以 .csv 结尾
    if not merge_output_file.endswith(".csv"):
        raise ValueError("合并输出文件名必须以 .csv 结尾")

    # 检查输出文件所在的目录是否存在，如果不存在，则创建
    output_dir = os.path.dirname(merge_output_file)
    if not os.path.exists(output_dir):
        print(f"输出目录不存在，创建输出目录: {output_dir}")
        os.makedirs(output_dir)

    # 获取源文件目录下所有 CSV 文件，并按文件名排序
    csv_files = sorted([f for f in os.listdir(source_file_dir) if f.endswith(".csv")])
    if not csv_files:
        raise FileNotFoundError(f"源文件目录中没有找到 CSV 文件: {source_file_dir}")

    # 读取并合并所有 CSV 文件
    data_frames = []
    for file in csv_files:
        file_path = os.path.join(source_file_dir, file)
        df = pd.read_csv(file_path)
        data_frames.append(df)

    # 合并数据
    merged_df = pd.concat(data_frames, ignore_index=True)

    # 处理排序配置
    if sort_config:
        # 验证sort_config格式
        for item in sort_config:
            if "field" not in item or "ascending" not in item:
                raise ValueError("sort_config中的每一项必须包含'field'和'ascending'字段")
            if not isinstance(item["ascending"], bool):
                raise ValueError("'ascending'字段必须为布尔值")
        by = [item["field"] for item in sort_config]
        ascending = [item["ascending"] for item in sort_config]
        merged_df = merged_df.sort_values(by=by, ascending=ascending)
    else:
        # 如果没有指定，则按照原始的列名依次升序排序
        merged_df = merged_df.sort_values(by=merged_df.columns.tolist(), ascending=True)

    # 输出到文件
    merged_df.to_csv(merge_output_file, index=False)

    print(f"合并和排序完成，结果已保存到 {merge_output_file}")


def simple_append_merge_mutil_csv_file_with_selected_columns(
        source_file_dir: str,
        merge_output_file: str,
        selected_columns: List[str],
        sort_config: List[Dict[str, bool]] = None
) -> None:
    """
    合并多个CSV文件中指定的列到一个文件

    :param source_file_dir: 多个csv源文件所在的目录
    :param merge_output_file: 合并输出的csv文件
    :param selected_columns: 需要读取的列名列表
    :param sort_config: 排序配置列表，格式为[{"field": "field1", "ascending": True},
                       {"field": "field2", "ascending": False}]
    :return: None
    """
    # 检查源文件目录是否存在
    if not os.path.exists(source_file_dir):
        raise FileNotFoundError(f"源文件目录不存在: {source_file_dir}")

    # 检查输出文件名是否以.csv结尾
    if not merge_output_file.endswith(".csv"):
        raise ValueError("合并输出文件名必须以 .csv 结尾")

    # 创建输出目录（如果不存在）
    output_dir = os.path.dirname(merge_output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取源文件目录下所有CSV文件，并按文件名排序
    csv_files = sorted([f for f in os.listdir(source_file_dir) if f.endswith(".csv")])
    if not csv_files:
        raise FileNotFoundError(f"源文件目录中没有找到CSV文件: {source_file_dir}")

    # 检查指定的列名是否为空
    if not selected_columns:
        raise ValueError("指定的列名列表不能为空")

    # 读取并合并所有CSV文件的指定列
    data_frames = []
    for file in csv_files:
        file_path = os.path.join(source_file_dir, file)
        try:
            # 只读取指定列
            df = pd.read_csv(file_path, usecols=selected_columns)
            data_frames.append(df)
        except ValueError as e:
            print(f"警告: 文件 {file} 中缺少某些指定列，跳过该文件。错误: {str(e)}")
            continue

    if not data_frames:
        raise ValueError("没有找到包含所有指定列的文件")

    # 合并数据
    merged_df = pd.concat(data_frames, ignore_index=True)

    # 处理排序配置
    if sort_config:
        # 验证sort_config格式
        for item in sort_config:
            if "field" not in item or "ascending" not in item:
                raise ValueError("sort_config中的每一项必须包含'field'和'ascending'字段")
            if not isinstance(item["ascending"], bool):
                raise ValueError("'ascending'字段必须为布尔值")
        by = [item["field"] for item in sort_config]
        ascending = [item["ascending"] for item in sort_config]
        merged_df = merged_df.sort_values(by=by, ascending=ascending)
    else:
        # 如果没有指定排序，则按照选定的列名升序排序
        merged_df = merged_df.sort_values(by=selected_columns, ascending=True)

    # 输出到文件
    merged_df.to_csv(merge_output_file, index=False)
    print(f"指定列合并完成，结果已保存到 {merge_output_file}")


def aggregate_merge_multi_csv_files(
        source_dir: str,
        output_file: str,
        key_columns: List[str],
        sum_columns: List[str]
) -> None:
    """
    合并目录下的CSV文件，并按指定列合并相同记录，统计列相加

    :param source_dir: 源文件目录
    :param output_file: 输出文件路径
    :param key_columns: 用于判断记录是否相同的列名列表（强制作为字符串处理）
    :param sum_columns: 需要相加的统计列名列表
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"目录不存在: {source_dir}")

    csv_files = sorted([f for f in os.listdir(source_dir) if f.endswith(".csv")])
    if not csv_files:
        raise FileNotFoundError(f"目录中没有CSV文件: {source_dir}")

    # 构建类型字典：key_columns作为字符串，sum_columns作为数值
    dtype_dict = {col: 'str' for col in key_columns}
    dtype_dict.update({col: 'int64' for col in sum_columns})

    dfs = []
    for file in csv_files:
        file_path = os.path.join(source_dir, file)
        df = pd.read_csv(file_path, dtype=dtype_dict)  # 明确指定列类型
        dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)

    # 分组时确保key_columns保持字符串类型
    result_df = merged_df.groupby(key_columns, as_index=False)[sum_columns].sum()

    # 恢复key_columns的字符串类型（groupby可能改变dtype）
    for col in key_columns:
        result_df[col] = result_df[col].astype('str')

    result_df = result_df.sort_values(by=sum_columns, ascending=False)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    result_df.to_csv(output_file, index=False)
    print(f"合并完成，结果保存至: {output_file}")


if __name__ == '__main__':
    simple_append_merge_mutil_csv_file(
        "res/split",
        "res/temp/split-simple_append_merge_mutil_csv_file-merged.csv")
