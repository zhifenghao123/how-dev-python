import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import tree
from sklearn.datasets import make_classification


def read_data_set():
    """
    读取数据集
    :return:
    """
    # data_x, data_y = make_classification(n_samples=10000, n_classes=4, n_features=10, n_informative=8, random_state=0)

    df_data = pd.read_csv('res/decision_tree_train_dataset.csv')
    data_X = df_data.loc[:, 'personalMonthlyDepositAmount':'personalMonthlyDepositAmount']
    data_Y = df_data['label']
    # data_x, data_y = make_classification(n_samples=10000, n_classes=4, n_features=10, n_informative=8, random_state=0)
    return data_X, data_Y

def read_data_set2():
    """
    读取数据集
    :return:
    """
    data = {
        'id': np.arange(1, 101),
        'gender': np.random.choice(['Male', 'Female'], size=100),
        'age': np.random.randint(0, 101, size=100),
        'career': np.random.choice(['教师', '医生', '警察', '软件开发工程师', '会计', '公务员', '工人'], size=100),
        'incomeAmt': np.random.uniform(100, 100000, size=100),
        'label': np.random.randint(0, 2, size=100)
    }
    df_data = pd.DataFrame(data)
    data_X = df_data.loc[:, 'career':'career']
    data_Y = df_data['label']
    # data_x, data_y = make_classification(n_samples=10000, n_classes=4, n_features=10, n_informative=8, random_state=0)
    return data_X, data_Y


def decision_tree_tranning(data_X, data_Y, max_leaf_nodes_val):
    """
    训练决策树
    :param data_X:
    :param data_Y:
    :param max_leaf_nodes_val:
    :return:
    """
    decision_tree = tree.DecisionTreeClassifier(
        criterion='entropy',  # “信息熵”最小化准则划分
        max_leaf_nodes=max_leaf_nodes_val,  # 最大叶子节点数
        min_samples_leaf=0.05)  # 叶子节点样本数量最小占比
    decision_tree.fit(data_X, data_Y)  # 训练决策树
    return decision_tree


def show_decision_tree(decision_tree):
    """
    可视化展示决策树
    :param decision_tree:
    :return:
    """
    tree.plot_tree(decision_tree)
    plt.show()


def decision_tree_binning(decision_tree, max_bin, x_value, y_value):
    """
    根据决策树进行分箱
    :param decision_tree:
    :param max_bin:
    :param x_value:
    :param y_value:
    :return:
    """
    n_nodes = decision_tree.tree_.node_count  # 决策树节点
    children_left = decision_tree.tree_.children_left
    children_right = decision_tree.tree_.children_right
    threshold = decision_tree.tree_.threshold

    min_x = x_value.min()[0]
    max_x = x_value.max()[0]
    # 开始分箱
    boundary = []
    for i in range(n_nodes):
        if children_left[i] != children_right[i]:  # 获得决策树节点上的划分边界值
            boundary.append(threshold[i])

    boundary.sort()

    # max_x = x_value.max() + 0.1  # +0.1是为了考虑后续groupby操作时，能包含特征最大值的样本
    boundary = [min_x] + boundary + [max_x]
    return boundary


def binning_result_view(data_X, bin_result):
    """
    分箱结果展示
    :param data_X:
    :param bin_result:
    :return:
    """
    bin_value = pd.cut(data_X['personalMonthlyDepositAmount'], bins=bin_result)  # 分箱的结果
    # print(bin_value)
    # 打印出每个分箱及其包含的数据
    for bin_label, group in data_X.groupby(bin_value):
        print(f"分箱: {bin_label}, 分箱个数: {len(group['personalMonthlyDepositAmount'].tolist())}")
        # print("数据:", group['personalMonthlyDepositAmount'].tolist())
        print()  # 打印一个空行以便于区分不同的分箱


if __name__ == '__main__':
    max_bin = 4
    data_X, data_Y = read_data_set()
    decision_tree = decision_tree_tranning(data_X, data_Y, max_bin)
    show_decision_tree(decision_tree)
    bin_result = decision_tree_binning(decision_tree, max_bin, data_X, data_Y)
    binning_result_view(data_X, bin_result)
