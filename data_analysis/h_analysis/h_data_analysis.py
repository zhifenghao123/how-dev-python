"""
   使用到的数据集：https://www.kaggle.com/datasets/zhijinzhai/loandata
   数据分析代码学习参考：https://zhuanlan.zhihu.com/p/122428571?utm_id=0

   数据集使用说明：
    Loan_ID：贷款ID
    loan_status：贷款状态
    Principal：贷款金额
    terms：贷款期限
    effective_date：开始时间
    due_date：到期时间
    paid_off_time：还款时间
    past_due_days：逾期天数
    age：年龄
    education：教育水平
    gender：性别
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 防止中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

def process_value_mapping(pd_data):
    """
    将数值映射
    将'loan_status'还款状态的'PAIDOFF': 1, 'COLLECTION': 2, 'COLLECTION_PAIDOFF': 3
    'education'受教育程度'High School or Below': 1, 'college': 2, 'Bechalor': 3, 'Master or Above': 4
    'Gender'性别'male': 1, 'female': 0
    :param pd_data:
    :return:
    """
    loan_status_dict = {'PAIDOFF': 1, 'COLLECTION': 2, 'COLLECTION_PAIDOFF': 3}
    pd_data['还款状态'] = pd_data['loan_status'].map(loan_status_dict)
    pd_data.drop('loan_status', inplace=True, axis=1)  # 删除loan_status字段

    # print(data.groupby('学历').agg('count'))  #  统计各学历的人数
    education_dict = {'High School or Below': 1, 'college': 2, 'Bechalor': 3, 'Master or Above': 4}
    pd_data['受教育程度'] = pd_data['education'].map(education_dict)
    pd_data.drop('education', inplace=True, axis=1)

    gender_dict = {'male': 1, 'female': 0}
    pd_data['性别'] = pd_data['Gender'].map(gender_dict)
    pd_data.drop('Gender', inplace=True, axis=1)

    col = {'Loan_ID': '贷款人ID', 'Principal': '贷款金额', 'terms': '期限', 'effective_date': '起始时间',
           'due_date': '到期时间', 'paid_off_time': '偿还时间', 'past_due_days': '逾期天数', 'age': '年龄'
           }  # 定义列名list
    pd_data.rename(columns=col, inplace=True)

def build_feature_value(pd_data):
    """
    将年龄以年龄段[青年(age<=30)、中年(31<=age<=46)、老年(age>46)]的形式分开，方面我们后面的分析。返回处理完的DataFrame数据。
    :param pd_data:
    :return:
    """
    pd_data['年龄段'] = pd_data['年龄'].apply(lambda x: '青年' if x <= 30 else ('中年' if 31 <= x <= 46 else '老年'))
    data_out = pd_data.copy()
    return data_out  # 返回data_out

def process_missing_value(pd_data):
    """
    缺失值处理
    可以看到还款时间和逾期天数分别有100条和300条的缺失值；
    根据数据，我们可以看还款时间为缺失值的是逾期客户，就是到统计时间时，还没有还款的客户，在这里我们不用去管它；
    而逾期天数缺失值是正常还款的客户，在这里我们用零去补全缺失值，方便统计
    :param pd_data:
    :return:
    """
    pd_data['past_due_days'].fillna(0, inplace=True)


def print_missing_value_statistics(pd_data):
    """
    打印缺失值统计信息
    :param pd_data:
    :return:
    """
    print(pd_data.isnull().sum())  # 查看缺失值

def print_pd_data(pd_data):
    """
    打印pd数据
    :param pd_data:
    :return:
    """
    print(pd_data)


def past_due_days_analyze(pd_data):
    zero = 0
    one = 0
    seven = 0
    fifty = 0
    thirty = 0
    for _, i in pd_data.iterrows():
        if i['逾期天数'] == 0:
            zero += 1
        elif 1 <= i['逾期天数'] <= 7:
            one += 1
        elif 8 <= i['逾期天数'] <= 14:
            seven += 1
        elif 15 <= i['逾期天数'] <= 30:
            fifty += 1
        else:
            thirty += 1
    dict_day = {'C': zero, '1+': one, '7+': seven, '15+': fifty, '30+': thirty}

    col_bar = list(dict_day.keys())
    data_bar = list(dict_day.values())
    plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 防止中文乱码
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    plt.pie(data_bar, labels=col_bar, autopct='%1.1f%%', startangle=90)
    plt.title('逾期详情')
    plt.show()
    # 从可视化图上，我们可以看到有60%的客户还是正常还款的，而有20.2%的客户逾期天数达到30+以上

def education_analyze(pd_data):
    # print(pd_data['贷款金额'].describe())
    # 学历逾期
    total_overdue_education = len(pd_data[pd_data['逾期天数'] > 0])
    below_peoples = pd_data[(pd_data['受教育程度'] == 1) & (pd_data['逾期天数'] > 0)]
    college_peoples = pd_data[(pd_data['受教育程度'] == 2) & (pd_data['逾期天数'] > 0)]
    bechalor_peoples = pd_data[(pd_data['受教育程度'] == 3) & (pd_data['逾期天数'] > 0)]
    master_peoples = pd_data[(pd_data['受教育程度'] == 4) & (pd_data['逾期天数'] > 0)]

    education_dict = {'高中逾期占比': len(below_peoples) / total_overdue_education,
                      '大专逾期占比': len(college_peoples) / total_overdue_education,
                      '本科逾期占比': len(bechalor_peoples) / total_overdue_education,
                      '硕士逾期占比': len(master_peoples) / total_overdue_education
                      }
    print('学历逾期：', education_dict)

    education_col = education_dict.keys()
    education_data = education_dict.values()
    plt.pie(education_data, labels=education_col, autopct='%1.1f%%', startangle=90)
    plt.title('学历逾期图')
    plt.show()
    # 从图上可看到，高中和大专学历逾期占了86.5%之多，而本科学历有13%的客户，而硕士学历只有0.5%的逾期客户，可以看到学历越高还款欲望会越高。

def age_analyze(pd_data):
    # 年龄段逾期
    total_age = len(pd_data[pd_data['逾期天数'] > 0])
    youth = pd_data[(pd_data['年龄段'] == '青年') & (pd_data['逾期天数'] > 0)]
    midlife = pd_data[(pd_data['年龄段'] == '中年') & (pd_data['逾期天数'] > 0)]
    agedness = pd_data[(pd_data['年龄段'] == '老年') & (pd_data['逾期天数'] > 0)]
    age_dict = {'青年逾期占比': len(youth) / total_age,
                '中年逾期占比': len(midlife) / total_age,
                '老年逾期占比': len(agedness) / total_age}

    age_col = age_dict.keys()
    age_data = age_dict.values()
    plt.pie(age_data, labels=age_col, autopct='%1.1f%%', startangle=90)
    plt.title('年龄段逾期图')
    plt.show()
    # 从图上可看到青年逾期56%，中年逾期42%,而老年逾期占比只有2%，可以得出年龄段越高，还款欲望越高。

def gender_analyze(pd_data):
    # 年龄段逾期
    two_state = pd_data[pd_data['还款状态'] == 2]
    man_two = pd_data[pd_data['性别'] == 1][pd_data[pd_data['性别'] == 1]['还款状态'] == 2]
    print(f'男性逾期比率：{len(man_two) / len(two_state) * 100}%')
    print(f'女性逾期比率：{round((1 - (len(man_two) / len(two_state))) * 100, 2)}%')


if __name__ == '__main__':
    pd_data = pd.read_csv("dataset/Loan_payments_data.csv")
    process_missing_value(pd_data)
    process_value_mapping(pd_data)
    pd_data_2 = build_feature_value(pd_data)
    # past_due_days_analyze(pd_data_2)
    # education_analyze(pd_data_2)
    # age_analyze(pd_data_2)
    gender_analyze(pd_data_2)



