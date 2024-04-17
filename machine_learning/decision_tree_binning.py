import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import tree
from sklearn.datasets import make_classification


def read_data_set(care_X_feature_name):
    """
    读取数据集
    :return:
    """
    # data_x, data_y = make_classification(n_samples=10000, n_classes=4, n_features=10, n_informative=8, random_state=0)

    df_data = pd.read_csv('res/decision_tree_train_dataset.csv')
    data_X = df_data.loc[:, care_X_feature_name:care_X_feature_name]
    data_Y = df_data['label']
    # data_x, data_y = make_classification(n_samples=10000, n_classes=4, n_features=10, n_informative=8, random_state=0)
    return data_X, data_Y

def read_data_set2(binning_feature):
    """
    读取数据集
    :return:
    """
    data = {
        'id': np.arange(1, 101),
        'gender': np.random.choice(['Male', 'Female'], size=100),
        'age': np.random.randint(0, 101, size=100),
        'career': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=100),
        'careerStr': np.random.choice(['1', '2', '3', '4', '5', '6', '7'], size=100),
        'careerDesc': np.random.choice(['教师', '医生', '警察', '软件开发工程师', '会计', '公务员', '工人'], size=100),
        'incomeAmt': np.random.uniform(100, 100000, size=100),
        'label': np.random.randint(0, 2, size=100)
    }
    df_data = pd.DataFrame(data)
    data_X = df_data.loc[:, binning_feature:binning_feature]
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


def decision_tree_binning(decision_tree, x_value, binning_feature):
    """
    根据决策树进行分箱
    :param decision_tree:
    :param max_bin:
    :param x_value:
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

    print("boundary is:" + str(boundary))

    # 初始化分箱结果的列表
    bin_results = []
    bin_value = pd.cut(data_X[binning_feature], bins=boundary)  # 分箱的结果
    # print(bin_value)
    # 打印出每个分箱及其包含的数据
    for bin_label, group in data_X.groupby(bin_value):
        bin_left = bin_label.left
        bin_right = bin_label.right
        bin_result = {
            "bin_label": f"({bin_left},{bin_right}]",
            "bin_data_set": group[binning_feature].tolist(),
            "bin_data_set_num": len(group[binning_feature].tolist())
        }

        bin_results.append(bin_result)
        print(bin_result)
        # print("---")
        # print(f"分箱: {bin_label}, 分箱个数: {len(group[binning_feature].tolist())}")
        # print("数据:", group[binning_feature].tolist())
        # print()

    return bin_results

if __name__ == '__main__':
    max_bin = 4
    # care_X_feature_name = 'personalMonthlyDepositAmount'
    # binning_feature = 'careerStr'
    binning_feature = 'career'
    data_X, data_Y = read_data_set2(binning_feature)
    decision_tree = decision_tree_tranning(data_X, data_Y, max_bin)
    show_decision_tree(decision_tree)
    bin_result = decision_tree_binning(decision_tree, data_X, binning_feature)
