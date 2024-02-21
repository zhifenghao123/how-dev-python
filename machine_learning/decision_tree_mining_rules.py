import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import tree


# 参考 https://zhuanlan.zhihu.com/p/561099398?utm_id=0

def print_decision_tree_help():
    help(tree._tree.Tree)


def decision_tree_train():
    # 显示所有的列
    pd.set_option('display.max_columns', None)
    train = pd.read_csv('./res/decision_tree_train_dataset.csv').fillna(-1)

    # 构建训练集
    X = train.loc[:, 'XINGBIE':'DKLL']
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


if __name__ == '__main__':
    clf, X, Y = decision_tree_train()
    # print_decision_tree(clf, X)
    show_decision_tree(clf)
