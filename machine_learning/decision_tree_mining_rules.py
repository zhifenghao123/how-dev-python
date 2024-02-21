import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import tree


# 参考 https://zhuanlan.zhihu.com/p/561099398?utm_id=0
"""
    测试数据集说明（decision_tree_train_dataset.csv）：    
    测试数据集包含：个人基本信息、个人住房公积金缴存、贷款等数据信息，来预测用户是否会逾期还款。数据集包含40000带标签训练集样本，共有19个基本特征，无缺失值。
    标签：label是否逾期（是 = 1，否 = 0）。
    特征：包含以下19个特征，对应名称和含义如下：
    
    特征名	类型	特征含义
    id	String	主键
    XINGBIE	int	性别
    CSNY	int	出生年月
    HYZK	int	婚姻状况
    ZHIYE	int	职业
    ZHICHEN	int	职称
    ZHIWU	int	职务
    XUELI	int	学历
    DWJJLX	int	单位经济类型
    DWSSHY	int	单位所属行业
    GRJCJS	float	个人缴存基数
    GRZHZT	int	个人账户状态
    GRZHYE	float	个人账户余额
    GRZHSNJZYE	float	个人账户上年结转余额
    GRZHDNGJYE	float	个人账户当年归集余额
    GRYICE	float	个人月缴存额
    DWYICE	float	单位月缴存额
    DKFFE	int	贷款发放额
    DKYE	float	贷款余额
    DKLL	float	贷款利率
    label	int	是否逾期 (0代表没逾期1代表逾期)
"""

def print_decision_tree_help():
    help(tree._tree.Tree)


def decision_tree_train():
    # 显示所有的列
    pd.set_option('display.max_columns', None)
    train = pd.read_csv('./res/decision_tree_train_dataset.csv').fillna(-1)

    # 构建训练集
    X = train.loc[:, '性别':'贷款利率']
    Y = train['label']

    # 构造决策树

    clf = tree.DecisionTreeClassifier(
        max_depth=3,
        min_samples_leaf=50
    )
    clf = clf.fit(X, Y)
    return clf, X, Y


def print_decision_tree(clf, X):
    """
    决策树打印出来
    :param clf:
    :return:
    """
    print(tree.export_text(clf, feature_names=X.columns.tolist()))


def show_decision_tree(clf):
    """
    可视化展示决策树
    :param clf:
    :return:
    """
    tree.plot_tree(clf)
    plt.show()

def show_decision_tree_with_graphviz(clf, X):
    """
    使用graphviz可视化绘制决策
    :param clf:
    :param X:
    :return:
    """
    import graphviz
    dot_data = tree.export_graphviz(
        clf,
        out_file=None,
        feature_names=X.columns,
        class_names=['good', 'bad'],
        filled=True, rounded=True,
        special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.view()



if __name__ == '__main__':
    clf, X, Y = decision_tree_train()
    # print_decision_tree(clf, X)
    show_decision_tree(clf)
    # show_decision_tree_with_graphviz(clf, X)

    result = clf.score(X, Y)
    print(result)
