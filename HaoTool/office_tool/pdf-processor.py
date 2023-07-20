import pandas as pd
import pdfplumber


def read_excel_data_list_from_pdf(pdf_path, start: int, end: int, excel_name=None):
    '''
    params:
        pdf_path：需要提取表格的pdf文件的绝对路径
        start：出现表格的起始页码
        end：表格结束页码
        excel_name：最后保存excel文件的文件名(默认为原始pdf文件名)
    '''
    pdf_2020 = pdfplumber.open(pdf_path)
    excel_data_list = []
    for i in range(start - 1, end):
        page = pdf_2020.pages[i]
        table = page.extract_table()
        print(table)
        print("\n")
        excel_data_list = excel_data_list + table
        print("第" + str(i) + "页完成\n")
    return excel_data_list


def clean_invalid_data_list_from_excel_file(data_list_, invalid_data_list_set):
    invalid_data_column_val_set = ['县市区']
    for data in data_list_:
        if data[0] in invalid_data_column_val_set:
            list(data_list_).remove(data)
            print('移除数据：' + str(data))
    new_data_list_ = [data for data in data_list_ if data[0] not in invalid_data_column_val_set]
    return new_data_list_


def save_data_list_to_excel_file(save_file_path, data_list_):
    columns = ['县市区', '总分', '人数', '累计人数']
    result_df = pd.DataFrame(data_list_, columns=columns)
    result_df.to_excel(save_file_path, index=False)


def pdf_to_excel(pdf_file_path, start: int, end: int, excel_file_path):
    data_list = read_excel_data_list_from_pdf(pdf_file_path, start=2, end=79)
    print(data_list)
    print('清理前数据条数：' + str(len(data_list)))
    new_data_list = clean_invalid_data_list_from_excel_file(data_list_=data_list, invalid_data_list_set=['县市区'])
    print('清理后数据条数：' + str(len(new_data_list)))
    save_data_list_to_excel_file(excel_file_path, data_list_=new_data_list)


def pdf_to_excel_v2(file_path, start: int, end: int, excel_name=None):
    '''
    params:
        file_path：需要提取表格的pdf文件的绝对路径
        start：出现表格的起始页码
        end：表格结束页码
        excel_name：最后保存excel文件的文件名(默认为原始pdf文件名)
    '''
    pdf = pdfplumber.open(file_path)
    if not excel_name:
        excel_name = file_path.split('\\')[-1].split('.')[0]
    df_result = pd.DataFrame()
    for i in range(start - 1, end):
        page = pdf.pages[i]
        table = page.extract_table()
        df_result = df_result.append(table)
    df_result = df_result.drop_duplicates(inplace=True)
    df_result.to_excel(excel_name + '.xlsx', index=False)


if __name__ == '__main__':
    pdf_to_excel(pdf_file_path=r'../dataset/ShowFile.pdf', start=2, end=79, excel_file_path=r'../dataset/ShowFile.xlsx')
    pdf_to_excel_v2(file_path=r'../dataset/ShowFile.pdf', start=2, end=79)
