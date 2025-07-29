import pandas as pd
import os


def convert_csv_to_excel(csv_file_path, excel_file_path=None, convert_to_str=False):
    """
    将CSV文件转换为Excel文件
    :param csv_file_path: 输入CSV文件路径
    :param excel_file_path: 输出Excel文件路径（可选）
    :param convert_to_str: 是否将所有列转换为字符串类型（避免科学计数法）
    :return: 生成的Excel文件路径
    """
    # 读取CSV文件
    if convert_to_str:
        df = pd.read_csv(csv_file_path, dtype=str)
    else:
        df = pd.read_csv(csv_file_path)

    # 将nan值替换为空字符串
    df = df.fillna("")


    # 自动生成输出路径（如果未提供）
    if excel_file_path is None:
        dirname = os.path.dirname(csv_file_path)
        basename = os.path.basename(csv_file_path)
        filename, _ = os.path.splitext(basename)
        excel_file_path = os.path.join(dirname, f"{filename}.xlsx")

    # 保存为Excel文件
    df.to_excel(excel_file_path, index=False)

    print(f"转换完成，Excel文件已保存到: {excel_file_path}")
    return excel_file_path


if __name__ == "__main__":
    # 示例使用
    input_csv = "res/temp/split-aggregate_merge_multi_csv_files-merged.csv"
    output_path = None
    convert_csv_to_excel(input_csv, output_path, convert_to_str=True)
