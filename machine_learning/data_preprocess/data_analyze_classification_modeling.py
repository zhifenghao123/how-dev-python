import pandas as pd
import numpy as np

# 1、基于plotly
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots  # 多子图

# 2、基于matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# 中文显示问题
#设置字体
plt.rcParams["font.sans-serif"]=["SimHei"]
#正常显示负号
plt.rcParams["axes.unicode_minus"]=False

# 3、基于seaborn
import seaborn as sns
# plt.style.use("fivethirtyeight")
plt.style.use('ggplot')

# 数据标准化、分割、交叉验证
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split,cross_val_score

# 模型
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# 模型评价
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, precision_score, f1_score


def print_df_data(df_data):
    """
    打印pd数据
    :param pd_data:
    :return:
    """
    print(df_data.head())
    print("-----------------")
    print("df_data.head() is as below:")
    print(df_data.shape)
    print("-----------------")
    print("df_data.dtypes is as below:")
    print(df_data.dtypes)
    print("-----------------")
    print("不同字段类型统计:")
    # print(df_data.dtypes.values)
    print(pd.value_counts(df_data.dtypes.values))
    print("-----------------")
    print("df.isnull().sum():")
    print(df_data.isnull().sum())

def basic_analyze(df_data):
    """
    不同字段下的取值统计
    :param df_data:
    :return:
    """
    # print(df_data.columns)

    # 1、针对字符类型字段的取值情况统计
    string_columns = df_data.select_dtypes(include="object").columns
    # 两个基本参数：设置行、列
    fig = make_subplots(rows=3, cols=5)
    for i, v in enumerate(string_columns):
        r = i // 5 + 1
        c = (i + 1) % 5
        data = df_data[v].value_counts().reset_index()
        if c == 0:
            fig.add_trace(go.Bar(x=data["index"], y=data[v],text=data[v], name=v),
                          row=r, col=5)
        else:
            fig.add_trace(go.Bar(x=data["index"], y=data[v],
                                 text=data[v], name=v),
                          row=r, col=c)
    fig.update_layout(width=1000, height=900)
    fig.show()

    # 2、针对数值型字段的分布情况：
    number_columns = df_data.select_dtypes(exclude="object").columns.tolist()
    # 两个基本参数：设置行、列
    fig = make_subplots(rows=2, cols=4)  # 2行4列
    for i, v in enumerate(number_columns):  # number_columns 长度是8
        r = i // 4 + 1
        c = (i + 1) % 4
        if c == 0:
            fig.add_trace(go.Box(y=df_data[v].tolist(), name=v),
                          row=r, col=4)
        else:
            fig.add_trace(go.Box(y=df_data[v].tolist(), name=v),
                          row=r, col=c)
    fig.update_layout(width=1000, height=900)
    fig.show()

def feature_process(df_data):
    """
    特征处理
    :param df_data:
    :return:
    """
    # 可视化展示统计信息
    #checking_account_status_statistic_view(df_data)

    # 在这里我们根据每个人的支票账户金额的大小进行硬编码：
    # A11：<0 DM，A12：0 <= x <200 DM，A13：> = 200 DM /至少一年的薪水分配，A14：无支票帐户
    cas = {"A11": 1, "A12": 2, "A13": 3, "A14": 0}
    df_data["checking_account_status"] = df_data["checking_account_status"].map(cas)
    #print(df_data)

    # 可视化展示统计信息
    # duration_statistic_view(df_data)
    # credit_history_statistic_view(df_data)

    # 对分类变量进行独热编码
    df_credit_history = pd.get_dummies(df_data["credit_history"])
    df_data = df_data.join(df_credit_history)
    df_data.drop("credit_history", inplace=True, axis=1)

    # 统计每个目的下的人数，根据人数的多少来实施硬编码
    purpose = df_data["purpose"].value_counts().sort_values(ascending=True).reset_index()
    purpose.columns = ["purpose", "number"]
    df_data["purpose"] = df_data["purpose"].map(dict(zip(purpose.purpose, purpose.index)))

    savings = {"A61": 1, "A62": 2, "A63": 3, "A64": 4, "A65": 0}
    df_data["savings"] = df_data["savings"].map(savings)

    df_present_employment = pd.get_dummies(df_data["present_employment"])
    df_data = df_data.join(df_present_employment)
    df_data.drop("present_employment", inplace=True, axis=1)

    df_personal = pd.get_dummies(df_data["personal"])
    df_data = df_data.join(df_personal)
    df_data.drop("personal", inplace=True, axis=1)

    df_other_debtors = pd.get_dummies(df_data["other_debtors"])
    df_data = df_data.join(df_other_debtors)
    df_data.drop("other_debtors", inplace=True, axis=1)

    df_property = pd.get_dummies(df_data["property"])
    df_data = df_data.join(df_property)
    df_data.drop("property", inplace=True, axis=1)

    df_housing = pd.get_dummies(df_data["housing"])
    df_data = df_data.join(df_housing)
    df_data.drop("housing", inplace=True, axis=1)

    df_other_installment_plans = pd.get_dummies(df_data["other_installment_plans"])
    df_data = df_data.join(df_other_installment_plans)
    df_data.drop("other_installment_plans", inplace=True, axis=1)

    #job_statistic_view(df_data)
    df_job = pd.get_dummies(df_data["job"])
    df_data = df_data.join(df_job)
    df_data.drop("job", inplace=True, axis=1)

    df_telephone = pd.get_dummies(df_data["telephone"])
    df_data = df_data.join(df_telephone)
    df_data.drop("telephone", inplace=True, axis=1)

    df_foreign_worker = pd.get_dummies(df_data["foreign_worker"])
    df_data = df_data.join(df_foreign_worker)
    df_data.drop("foreign_worker", inplace=True, axis=1)
    return df_data


def sample_process_for_modeling(df_data):
    from sklearn.utils import shuffle
    df_data = shuffle(df_data).reset_index(drop=True)
    # 选取特征
    X = df_data.drop("customer_type", axis=1)
    # 目标变量
    y = df_data['customer_type']
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)
    ss = StandardScaler()
    X_train = ss.fit_transform(X_train)

    # 分别求出训练集的均值和标准差
    mean_ = ss.mean_  # 均值
    var_ = np.sqrt(ss.var_)  # 标准差

    # 归一化之后的测试集中的特征数据
    X_test = (X_test - mean_) / var_

    return X_train, y_train, X_test, y_test

def view_confusion_matrix(confusion_mat):
    # 混淆矩阵可视化
    classes = ["良好", "不良"]
    disp = ConfusionMatrixDisplay(confusion_matrix=confusion_mat, display_labels=classes)
    disp.plot(
        include_values=True,  # 混淆矩阵每个单元格上显示具体数值
        cmap="GnBu",  # matplotlib识别的颜色图
        ax=None,
        xticks_rotation="horizontal",
        values_format="d"
    )
    plt.show()


def build_model_with_decision_tree(X_train, y_train, X_test, y_test):
    dt = DecisionTreeClassifier(max_depth=5)
    dt.fit(X_train, y_train)

    y_pred = dt.predict(X_test)

    # 混淆矩阵
    confusion_mat = metrics.confusion_matrix(y_test, y_pred)
    print(confusion_mat)
    #view_confusion_matrix(confusion_mat)

    ## auc-roc
    auc_roc = metrics.roc_auc_score(y_test, y_pred)  # 测试值和预测值
    print(auc_roc)

def build_model_with_random_forest(X_train, y_train, X_test, y_test):
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    # 混淆矩阵
    confusion_mat = metrics.confusion_matrix(y_test, y_pred)
    print(confusion_mat)
    #view_confusion_matrix(confusion_mat)

    ## auc-roc
    auc_roc = metrics.roc_auc_score(y_test, y_pred)  # 测试值和预测值
    print(auc_roc)

def build_model_with_xgb(X_train, y_train, X_test, y_test):
    from xgboost.sklearn import XGBClassifier

    # 类列必须从 0 开始（自 1.3.2 版以来要求）。解决这个问题的一种简单方法是使用sklearn.preprocssing 库中的LabelEncoder。 将y数据进行转换之后，就可以正常运行。
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)

    # 先转成数组再传进来
    X_test = X_test.values

    ## 定义 XGBoost模型
    clf = XGBClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    # 混淆矩阵
    confusion_mat = metrics.confusion_matrix(y_test, y_pred)
    print(confusion_mat)
    #view_confusion_matrix(confusion_mat)

    ## auc-roc
    auc_roc = metrics.roc_auc_score(y_test, y_pred)  # 测试值和预测值
    print(auc_roc)


def checking_account_status_statistic_view(df_data):
    print(df_data["checking_account_status"].value_counts())
    fig, ax = plt.subplots(figsize=(12, 8), dpi=80)
    sns.countplot(x="checking_account_status", data=df_data)
    plt.title("number of checking_account_status")
    for p in ax.patches:
        ax.annotate(f'\n{p.get_height()}', (p.get_x(), p.get_height() + 5), color='black', size=20)
    plt.show()

def duration_statistic_view(df_data):
    duration = df_data["duration"].value_counts()
    fig = px.violin(df_data, y="duration")
    fig.show()

def credit_history_statistic_view(df_data):
    ch = df_data["credit_history"].value_counts().reset_index()
    fig = px.pie(ch, names="index", values="credit_history")
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label'
    )
    fig.show()

def job_statistic_view(df_data):
    fig, ax = plt.subplots(figsize=(12, 8), dpi=80)
    sns.countplot(x="job", data=df_data)
    plt.title("number of job")
    for p in ax.patches:
        ax.annotate(f'\n{p.get_height()}', (p.get_x(), p.get_height() + 5), color='black', size=20)
    plt.show()

def build_model_with_optimization(df_data):
    """
    模型优化
    :return:
    """
    X = df_data.drop("customer_type", axis=1)
    # 目标变量
    y = df_data['customer_type']
    # y：customer_type是目标变量
    # 1、计算每个特征和目标变量的相关系数
    data = pd.concat([X, y], axis=1)
    corr = data.corr()
    print(corr)
    #view_heat_map(corr)

    # 根据相关系数筛选前20个变量
    top_k = 20
    cols = corr.nlargest(top_k, "customer_type")["customer_type"].index
    # cm = np.corrcoef(data[cols].values.T)
    # hm = plt.subplots(figsize=(10, 10))  # 调整画布大小
    # hm = sns.heatmap(data[cols].corr(),  # 前10个属性的相关系数
    #                  annot=True,
    #                  square=True)
    # plt.show()

    # 2、筛选相关系数绝对值大于0.1的变量
    threshold = 0.1
    corrmat = data.corr()
    top_corr_features = corrmat.index[abs(corrmat["customer_type"]) > threshold]
    # plt.figure(figsize=(10, 10))
    #
    # g = sns.heatmap(data[top_corr_features].corr(),  # 大于0.5的特征构成的DF的相关系数矩阵
    #                 annot=True,
    #                 square=True,
    #                 cmap="nipy_spectral_r"
    #                 )
    # plt.show()

    # 新数据建模、数据切分、标准化、建模
    # 筛选出为True的特征
    useful_col = corrmat.index[abs(corrmat["customer_type"]) > threshold].tolist()

    new_df = df_data[useful_col]
    new_df.head()
    print(new_df.head())





def view_heat_map(corr):
    ax = plt.subplots(figsize=(20, 16))
    ax = sns.heatmap(corr,
                     vmax=0.8,
                     square=True,
                     annot=True,  # 显示数据
                     cmap="YlGnBu")
    plt.show()



if __name__ == '__main__':
    df_data = pd.read_csv("res/german_credit_data_dataset.csv")
    #print_df_data(df_data)
    #basic_analyze(df_data)
    df_data = feature_process(df_data)
    # X_train, y_train, X_test, y_test = sample_process_for_modeling(df_data)
    # print("build model with decision tree....")
    # build_model_with_decision_tree(X_train, y_train, X_test, y_test)
    # print("build model with random forest....")
    # build_model_with_random_forest(X_train, y_train, X_test, y_test)
    # print("build model with xgb....")
    # build_model_with_xgb(X_train, y_train, X_test, y_test)
    build_model_with_optimization(df_data)

