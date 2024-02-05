"""
1. 分箱的意义
这里首先简单介绍一下分箱的定义，变量的分箱分为两种，一种是对连续变量进行离散化处理形成类别变量。比如将年龄划分为[10,20]，[20,30]，[30以上]等。
而对于离散变量而言，其本身就是一种类别变量，所以这里的分箱主要的是将那些取值过多的离散变量进行合理的合并，从而减少变量的取值数量。

对数据进行分箱，做这么一番这折腾的意义是什么，我们来梳理一下分箱的作用。

（1）对变量进行分箱有助于提升模型对于异常值的鲁棒性。
    比如，对于月收入这个变量，如果整体样本的月收入中位数为10000，那么当一个样本的月收入这个变量取值为100时则显然是一个离群值，但如果将其分箱后归到一个较为合理的月收入分箱，如[低于2000]，那么这个异常值对于整体模型的影响基本上就不存在了。
（2）对变量分箱能够将缺失值单独作为一箱，以保留那些有实际业务意义的缺失值。
（3）对变量进行分箱有助于提升模型的稳定性。
    随着时间的变化，模型的目标客群会发生一些细微的变化，比如月收入增长或降低，年龄增长等，但这种细微的差别不应当引起模型的评分出现较大的波动。像月收入由8000上涨到8500，在其他特征没有显著变化的情况下，该样本的评分应当是基本保持不变的。这时候通过分箱处理，得到一个分箱范围是[7000，9000]，那么8000和8500都会落在这个区间内，即该特征的取值（该分箱对应的编码）不会发生改变。
（4）风控常用的LR模型是线性模型，对于非线性关系的表达能力很差。
    引入分箱后可以生成一些非线性特征（特征交叉，重组等），从而提高模型的非线性能力。
（5）分箱本质上也可以理解成数据的标准化处理。
    对于LR这类模型，不同变量的取值空间若差异很大，则容易使得模型偏向于那些取值更大的特征。数据的标准化处理能够将这些特征缩放到同一尺度上，避免这些影响。分箱后每一个特征的取值范围就变成了分箱的编码取值，能够在同一尺度下去衡量。
总结一下，分箱的核心目标就是为了提升模型整体的稳定性。对于LR这种线性模型，分箱也能够使得特征带有一些非线性的特性，从而提升模型的非线性表达能力。这里需要再说明一下，所谓分箱引入非线性是指对于原始的特征，其于目标变量之间是一种非线性关系，比如y=sinx。线性模型的只会拟合出一条直线，这条直线显然无法表达这种非线性关系。通过分箱后，x在一个区间范围内的所有取值都会被同一个值即分箱的编码代替，那么模型对于这个x在这个取值范围内的预测值是一样的。相当于线性模型也能拟合出一条符合数据分布的曲线（图1）

2. 常用的分箱方法
了解了分箱的意义之后，我们再来看一下常见的分箱方法。总体上，分箱的方法有两类，一种是有监督分箱，一种是无监督分箱。
有监督分箱顾名思义就是分箱过程中需要使用到目标变量。这种方式在分箱的过程中更好地将目标变量的信息融合在特征中，分箱的结果也会更加合理一些，但相对来讲计算也更加复杂一些。
无监督分箱不需要利用目标变量的信息，可以理解为按照某种简单的规则来划分样本。这种方式计算简单，但带有很大的随机性，所以分箱效果相对较差。
1） 无监督分箱：等频分箱，等距分箱，聚类分箱
2） 有监督分箱：卡方分箱，Best-KS分箱，决策树分箱

分箱需要遵守一定的原则，无论采取哪种方式，分箱的原则基本是一致的。这里先罗列出来，后续进行各个分箱方法的实现时都是需要考虑的。
其中第一、二条主要是保障分箱内的样本数足够大满足统计意义。第三、四条是为了后续避免对建模产生影响，比如过拟合（分箱内全是正样本）
1） 分箱后箱内样本不能少于总样本的5%
2） 分箱的数量不能太大，一般是5~10箱
3） 对于类别变量，如果其取值不多可以不考虑分箱，比如学历这种变量
4）分箱后每一箱的中不能仅有正样本或者负样本，并且尽可能使得每一箱的正负样本分布差异较大
"""

import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from scipy.stats import chi2_contingency


def equal_span():
    """
    等距分箱就是按照特征的取值进行排序后切分成多个区间，并且每个区间的大小是一样的，样本按照其特征的取值归类到不同的区间里。
    :return:
    """
    data = pd.read_csv("./res/germancredit.csv")
    data['creditability'] = data['creditability'].apply(lambda x: 1 if x == 'bad' else 0)
    # 等距分成5个箱
    df = pd.cut(data['duration'], bins=5).reset_index() \
        .rename(columns={'index': 'sample', 'duration': 'bins'})

    df['target'] = data['creditability'].astype(int)
    # 每一分箱内坏客户的占比
    bad_rate = (df.groupby('bins').agg({'target': 'sum'}) / df.groupby('bins').agg({'target': 'count'})) \
        .reset_index().rename(columns={'target': 'bad_rate'})
    df_counts = pd.DataFrame(data=df['bins'].value_counts()).reset_index() \
        .rename(columns={'index': 'bins', 'bins': 'sample_num'})

    # 形成用于绘图的数据，包括分箱区间，箱内样本数以及箱内坏客户占比
    plot_df = pd.merge(df_counts, bad_rate, on='bins').sort_values(by='bins')
    plot_df['bins'] = plot_df['bins'].apply(lambda x: str(x))

    plot_bins(bad_rate=plot_df.loc[:, ['bins', 'bad_rate']]
              , samples_num=plot_df.loc[:, ['bins', 'sample_num']])


def equal_freq():
    """
    等频分箱是在划分区间时考虑各个区间内的样本数，保障每个区间内的样本占比大致相同，比如分成5个箱，则每箱的样本数要接近总样本数的20%，这时每个区间的距离不一定是一样的。
    :return:
    """
    data = pd.read_csv("./res/germancredit.csv")
    data['creditability'] = data['creditability'].apply(lambda x: 1 if x == 'bad' else 0)

    df = pd.qcut(data['duration'], q=5, duplicates='drop').reset_index() \
        .rename(columns={'index': 'sample', 'duration': 'bins'})

    df['target'] = data['creditability'].astype(int)
    # 每一分箱内坏客户的占比
    bad_rate = (df.groupby('bins').agg({'target': 'sum'}) / df.groupby('bins').agg({'target': 'count'})) \
        .reset_index().rename(columns={'target': 'bad_rate'})
    df_counts = pd.DataFrame(data=df['bins'].value_counts()).reset_index() \
        .rename(columns={'index': 'bins', 'bins': 'sample_num'})

    # 形成用于绘图的数据，包括分箱区间，箱内样本数以及箱内坏客户占比
    plot_df = pd.merge(df_counts, bad_rate, on='bins').sort_values(by='bins')
    plot_df['bins'] = plot_df['bins'].apply(lambda x: str(x))

    plot_bins(bad_rate=plot_df.loc[:, ['bins', 'bad_rate']]
              , samples_num=plot_df.loc[:, ['bins', 'sample_num']])


def kmeans_bin():
    """
    这是一种利用样本之间的相似度进行分箱的方法。通常使用Kmeans作为分箱的算法。
    一般的做法是按照特征的取值进行聚类，按照需要分的箱的数量来设置聚类的簇的数量（比如5）。
    得到每个簇的聚类中心后，有很多的方式可以用来选择分箱的边界点。比如对数据进行归类，然后把属于同一个簇的数据的最大值和最小值作为该簇对应的分箱的边界点。
    另一种方式是选择相邻两个聚类中心的中点作为分箱的边界。之所以选择相邻两个聚类中心的中点作为边界点是为了使得聚类中心左（取值小于聚类中心）右（取值大于聚类中心）的数据都能归到这个分箱中，符合聚类后的数据分布特点，即该聚类中心左右靠近这个聚类中心的数据是属于同一个簇。
    下面的代码使用的第二种方式。
    :return:
    """
    data = pd.read_csv("./res/germancredit.csv")
    data['creditability'] = data['creditability'].apply(lambda x: 1 if x == 'bad' else 0)
    kmodel = KMeans(n_clusters=5, random_state=0)
    kmodel.fit(X=data['duration'].values.reshape([len(data), 1]))
    # 聚类中心按升序排序
    centers = pd.DataFrame(kmodel.cluster_centers_).sort_values(by=0, ascending=True)

    # 计算相邻聚类中心的中点，生成切分的边界点
    cut_point = centers.rolling(2).mean().iloc[1:, 0].tolist()
    cut_point = [data['duration'].min()] + cut_point + [data['duration'].max()]

    # 按边界点分箱
    df = pd.DataFrame(data=pd.cut(x=data['duration'], bins=cut_point)).reset_index() \
        .rename(columns={'index': 'sample', 'duration': 'bins'})
    df['target'] = data['creditability'].astype(int)
    # 每一分箱内坏客户的占比
    bad_rate = (df.groupby('bins').agg({'target': 'sum'}) / df.groupby('bins').agg({'target': 'count'})) \
        .reset_index().rename(columns={'target': 'bad_rate'})
    df_counts = pd.DataFrame(data=df['bins'].value_counts()).reset_index() \
        .rename(columns={'index': 'bins', 'bins': 'sample_num'})

    # 形成用于绘图的数据，包括分箱区间，箱内样本数以及箱内坏客户占比
    plot_df = pd.merge(df_counts, bad_rate, on='bins').sort_values(by='bins')
    plot_df['bins'] = plot_df['bins'].apply(lambda x: str(x))

    plot_bins(bad_rate=plot_df.loc[:, ['bins', 'bad_rate']]
              , samples_num=plot_df.loc[:, ['bins', 'sample_num']])


def merge_bin(bin_a, bin_b, ori_buckets):
    '''合并分箱，返回新的边界点'''
    new_bin = pd.Interval(left=bin_a.left, right=bin_b.right, closed='right')
    # 将原先的分箱删除并生成新合并的分箱
    new_buckets = ori_buckets.remove_categories([bin_a, bin_b]).dropna()
    new_buckets = new_buckets.add_categories([new_bin])
    new_buckets = pd.CategoricalIndex(new_buckets.categories).sort_values()

    new_cut = np.unique(np.array([[i.left, i.right] for i in new_buckets]).flatten()).tolist()

    # 返回合并后新的边界点重新分箱以及合并后的分箱数用于终止合并
    return new_cut, len(new_buckets)


def chi_bins():
    """
    卡方分箱是利用卡方检验来观察两个分类变量之间的独立性。
    在分箱过程中，特征的每一个分箱看作是一个分类变量，那么这个分箱里的的样本就是一个分布，如果两个分箱之间的分布无显著差异，则认为这两个分箱可以合并。

    卡方值就是期望频次与实际观测频次之间的差异，其计算公式如下：
    卡方值=（O1-E1)/E1 +（O2-E2)/E2 + ...... +（On-En)/En
    其中O是实际观测频数，E是期望观测频数。

    卡方分箱是基于卡方检验的，其基本的步骤如下：
    （1）将特征取值按升序排序，构建初始化的分箱，即每一个值作为一个分箱看待
    （2）两两计算相邻两个分箱的卡方值
    （3）选择2中计算的卡方值中的最小值所对应的分箱进行合并
    （4）重复2、3直到满足终止条件（计算的卡方值均大于某一阈值或达到预设的分箱数）
    :return:
    """
    data = pd.read_csv("./res/germancredit.csv")
    data['creditability'] = data['creditability'].apply(lambda x: 1 if x == 'bad' else 0)
    bins = 5
    init_bins = data['duration'].unique()
    cut_points = sorted(init_bins)
    # 由于pandas.cut分箱区间是左开右闭，所以将切分点的最小值和最大值都减小或增加一个值以使区间包含最大值和最小值，
    # 避免某些样本无法被分箱
    cut_points[0], cut_points[-1] = cut_points[0] - 0.1, cut_points[-1] + 0.1
    while True:
        # cut_points = [cut_points[i] for i in range(1, len(cut_points) - 1, 2)]
        df = pd.DataFrame(data=pd.cut(x=data['duration'], bins=cut_points)).reset_index() \
            .rename(columns={'index': 'sample', 'duration': 'bins'})
        df['target'] = data['creditability'].astype(int)
        buckets = df['bins'].value_counts().index.sort_values()
        chi_values = []
        for i in range(len(buckets) - 1):
            # print(buckets[i],buckets[i+1])
            bin_a = df[df['bins'] == buckets[i]]
            bin_b = df[df['bins'] == buckets[i + 1]]

            # 获取两个bin中的分布，即好人数，坏人数以及bin中的样本数
            bin_a_dist = [bin_a['target'].sum(), bin_a['target'].count() - bin_a['target'].sum()
                , bin_a['target'].count()]
            bin_b_dist = [bin_b['target'].sum(), bin_b['target'].count() - bin_b['target'].sum()
                , bin_b['target'].count()]
            # 合并后的分布
            d = np.array([bin_a_dist, bin_b_dist])

            chi_values.append(chi2_contingency(d)[0])

        # 获取最小卡方值的索引，相邻两个分箱合并
        min_chi_index = np.argmin(chi_values)
        bin_a = buckets[min_chi_index]
        bin_b = buckets[min_chi_index + 1]
        cut_points, b_num = merge_bin(bin_a, bin_b, buckets)

        if b_num == bins:
            break

    bad_rate = (df.groupby('bins').agg({'target': 'sum'}) / df.groupby('bins').agg({'target': 'count'})) \
        .reset_index().rename(columns={'target': 'bad_rate'})
    df_counts = pd.DataFrame(data=df['bins'].value_counts()).reset_index() \
        .rename(columns={'index': 'bins', 'bins': 'sample_num'})

    # 形成用于绘图的数据，包括分箱区间，箱内样本数以及箱内坏客户占比
    plot_df = pd.merge(df_counts, bad_rate, on='bins').sort_values(by='bins')
    plot_df['bins'] = plot_df['bins'].apply(lambda x: str(x))

    plot_bins(bad_rate=plot_df.loc[:, ['bins', 'bad_rate']]
              , samples_num=plot_df.loc[:, ['bins', 'sample_num']])


def cal_KS(df):
    '''计算分箱的KS值并求出KS最大值所对应的分箱（阈值），返回该值用于最终划分数据'''
    bins = df['bins'].unique()
    bins.sort()
    # 计算每一个分箱的KS值并返回
    bin_lst = []
    # 数据集中总的好人数和坏人数
    bad_num_total = df['target'].sum()
    good_num_total = df['target'].count() - df['target'].sum()
    for i in bins:
        temp = df[df['bins'] == i]
        bin_lst.append([i, temp['target'].sum(), temp['target'].count() - temp['target'].sum()])
    ks_df = pd.DataFrame(columns=['bin', 'bad_num', 'good_num'], data=bin_lst)

    # 求好人与坏人的累计占比
    ks_df['cum_bad_rate'] = ks_df['bad_num'].cumsum() / bad_num_total
    ks_df['cum_good_rate'] = ks_df['good_num'].cumsum() / good_num_total
    # 防止当数据中只有好人或坏人时bad_num_total，good_num_total为0，此时累计占比为计算出NaN
    ks_df.fillna(0, inplace=True)
    ks_df['ks'] = (ks_df['cum_bad_rate'] - ks_df['cum_good_rate']).abs()
    cut_point = ks_df.loc[np.argmax(ks_df['ks']), 'bin']
    left = df[df['bins'] < cut_point]
    right = df[df['bins'] > cut_point]
    return left, right, cut_point


def KS_bin():
    """
    KS（Kolmogorov-Smirnov）是一个用于衡量模型对样本区分能力的指标。当模型训练完成后，我们可以通过绘制KS曲线并计算KS值来评估模型的样本区分能力。
    我们首先将模型的评分进行分箱，然后计算每个分箱内的样本占比情况，这里KS值是根据每一箱中的好坏客户的累计占比之差来计算的，即 KS = | 坏客户累计占比 - 好客户累计占比|
    最终模型的KS值的每一个分箱KS值的最大值，即0.48。KS的最大值表明，直到这个分箱（阈值）为止，当前的好客户以及坏客户的累计占比之差最大，也就是这个阈值能够最大程度区分好坏样本
    。如果我们以这个阈值作为划分条件，能够达到模型最好的效果。比如我们的例子中以得分3作为阈值，低于3的认为是坏客户，那么模型能够拒绝掉86%的坏客户，当然这时候也会拒绝掉38%的好客户。这个结果是模型能够达到的最好结果。
    利用这些数据能够得到图9所示的KS曲线。图10是KS值的业务评价标准，一般认为KS<0.2时模型效果很差，无法使用。

    Best-KS分箱实际的计算方式跟模型KS一样，只是这里的分箱不是模型评分，而是特征的分箱。具体的步骤如下：
    (1)将特征取值按从小到大排序，每一个值作为一个分箱
    (2)计算每一个分箱的KS值
    (3)找到最大KS值对应的分箱，即特征值，以该特征值作为划分依据将数据划分成左右两份数据SET1和SET2（低于该特征值以及高于该特征值）
    (4)按照第三步递归划分左右两个数据集，直到满足终止条件（一般以KS值低于某个阈值或分箱数达到预设的值）

    :return:
    """
    data = pd.read_csv("./res/germancredit.csv")
    data['creditability'] = data['creditability'].apply(lambda x: 1 if x == 'bad' else 0)
    bins = 5
    df = data[['duration', 'creditability']] \
        .rename(columns={'creditability': 'target', 'duration': 'bins'})
    samples_num = len(df)
    cut_points_lst = []

    def best_ks_cut(df):

        if len(cut_points_lst) - 1 < bins:
            left, right, cut_point = cal_KS(df)
            cut_points_lst.append(cut_point)
            # 确保分箱后每箱的样本不少于总体的5%
            if len(left) > int(samples_num * 0.05) and len(right) > int(samples_num * 0.05):
                best_ks_cut(right)
                best_ks_cut(left)
            elif len(left) > int(samples_num * 0.05):
                best_ks_cut(left)
            elif len(right) > int(samples_num * 0.05):
                best_ks_cut(right)
            else:
                pass

    best_ks_cut(df)
    # 得到所有的切分点进行排序，在最小值前和最大值后分别插入负无穷和正无穷，作为分箱的边界点
    cut_points_lst.sort()
    cut_points_lst.insert(0, float('-inf'))
    cut_points_lst.insert(len(cut_points_lst), float('inf'))

    # 根据切点进行分箱
    df = pd.DataFrame(data=pd.cut(x=data['duration'], bins=cut_points_lst)).reset_index() \
        .rename(columns={'index': 'sample', 'duration': 'bins'})
    df['target'] = data['creditability'].astype(int)

    bad_rate = (df.groupby('bins').agg({'target': 'sum'}) / df.groupby('bins').agg({'target': 'count'})) \
        .reset_index().rename(columns={'target': 'bad_rate'})
    df_counts = pd.DataFrame(data=df['bins'].value_counts()).reset_index() \
        .rename(columns={'index': 'bins', 'bins': 'sample_num'})

    # 形成用于绘图的数据，包括分箱区间，箱内样本数以及箱内坏客户占比
    plot_df = pd.merge(df_counts, bad_rate, on='bins').sort_values(by='bins')
    plot_df['bins'] = plot_df['bins'].apply(lambda x: str(x))

    plot_bins(bad_rate=plot_df.loc[:, ['bins', 'bad_rate']]
              , samples_num=plot_df.loc[:, ['bins', 'sample_num']])


def tree_bin():
    """
    决策树分箱就是以需要进行离散化的特征以及目标变量训练决策树模型。利用生成的决策树的分支节点来作为特征分箱的依据。由于在决策树生成的过程中，每一次的分支都是基于分支后的“增益”。
    比如ID3使用信息增益，C4.5使用信息增益率以及CART使用基尼指数等。通过计算最佳“增益”来确定分支的阈值。
    所以，利用决策树中的分支阈值来对特征进行分箱，能够最大限度地使得分箱中的好坏客户样本分布更加合理（好客户更多或者坏客户更多）。这样也就能够从不同分箱的角度来区分好坏客户，有利于后续建模分析。
    以下代码以sklearn中提供的DecisionTreeClassifier来训练决策树，然后获取决策树的节点分支的阈值来作为分箱的依据。
    图13是生成的决策树，可以看到除了叶子节点外都会一个分支的阈值。当一个样本进入模型时，会根据这个生成的决策树规则一步一步走到某一个叶子节点。
    对于分类问题，其最终的类别就是该叶子节点中训练样本的类别的众数。由我们生成的决策最终得到的划分阈值是[8.5, 15.5, 19.0, 34.5, 43.5]。
    :return:
    """
    data = pd.read_csv("./res/germancredit.csv")
    data['creditability'] = data['creditability'].apply(lambda x: 1 if x == 'bad' else 0)
    df = data[['duration', 'creditability']] \
        .rename(columns={'creditability': 'target', 'duration': 'bins'})

    clf = DecisionTreeClassifier(criterion='entropy', min_samples_leaf=0.02, max_leaf_nodes=6)
    clf.fit(np.array(df['bins']).reshape(len(df), 1), df['target'])
    cut_points = []
    node_count = clf.tree_.node_count
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    threshold = clf.tree_.threshold

    for i in range(node_count):
        # 该节点是叶子节点，不存在分支
        if children_left[i] != children_right[i]:
            # 将分支节点加入分箱边界
            cut_points.append(threshold[i])

    cut_points.sort()
    cut_points = [df['bins'].min() - 0.1] + cut_points + [df['bins'].max() + 0.1]

    df = pd.DataFrame(data=pd.cut(x=data['duration'], bins=cut_points)).reset_index() \
        .rename(columns={'index': 'sample', 'duration': 'bins'})
    df['target'] = data['creditability'].astype(int)

    bad_rate = (df.groupby('bins').agg({'target': 'sum'}) / df.groupby('bins').agg({'target': 'count'})) \
        .reset_index().rename(columns={'target': 'bad_rate'})
    df_counts = pd.DataFrame(data=df['bins'].value_counts()).reset_index() \
        .rename(columns={'index': 'bins', 'bins': 'sample_num'})

    # 形成用于绘图的数据，包括分箱区间，箱内样本数以及箱内坏客户占比
    plot_df = pd.merge(df_counts, bad_rate, on='bins').sort_values(by='bins')
    plot_df['bins'] = plot_df['bins'].apply(lambda x: str(x))

    plot_bins(bad_rate=plot_df.loc[:, ['bins', 'bad_rate']]
              , samples_num=plot_df.loc[:, ['bins', 'sample_num']])
    # plot_tree(clf,
    # feature_names=['bins'],
    # filled=True)
    # plt.show()


def plot_bins(bad_rate, samples_num):
    """
    可视化分箱结果
    :param bad_rate:
    :param samples_num:
    :return:
    """
    plt.figure(figsize=(15, 15))
    plt.subplot(111)
    plt.bar(samples_num['bins'], samples_num['sample_num'], label='samples_num', color='#003547')
    plt.xticks(rotation=360, fontsize=30)
    plt.yticks(fontsize=30)
    plt.rc('legend', fontsize=30)
    plt.legend(loc='upper left', )
    # 次坐标轴绘制折线图
    plt.twinx()
    plt.plot(bad_rate['bins'], bad_rate['bad_rate'], lw='4', color='#E1523D', label='bad_rate', marker='o')
    plt.xticks(rotation=360, fontsize=30)
    plt.yticks(fontsize=30)
    plt.rc('legend', fontsize=30)
    plt.legend(loc='upper right')
    plt.show()


# 计算各个分箱方法的IV值，可以在上述的各个分箱函数最后调用，如cal_iv(df,"等距分箱")，df是经过pd.cut之后的结果
def cal_iv(df, method):
    """
    分箱的效果需要怎么衡量呢？
    分箱主要的目的在于提升模型整体的稳定性以及提升模型的整体的预测能力（拟合非线性数据）。那么，我们分箱后最直接能够衡量的就是特征对于模型的做出准确预测的贡献了。
    所以，我们常用信息量IV（Information Value）来衡量特征的整体预测能力。其值越大，表明我们分箱的方法更合理，能够使得特征具有更强的预测能力。
    IV可以理解为，为了知道一个样本是好客户还是坏客户，我们需要收集信息（特征），如果这些信息足够多且有用（IV大），则我们就能够更有把握去判断样本的好坏。
    分箱的结果相当于调整了特征整体能够提供的信息量以提升其预测能力，最终能提升到何种程度就需要用IV来量化了。
    网络上有许多关于IV值的理论介绍，这里不多加赘述。仅提供本案例中用于计算IV值的代码以供参考
    。此外，分箱的效果有时也需要符合单调性的原则。这一点在梅子行老师的《智能风控 Python金融风险管理与评分卡建模》中也有强调。
    这里的单调性是指每一个分箱中坏客户的占比要呈现单调递增或递减，具体取决于业务含义
    。这也是前面的分箱可视化中也展示了每个分箱的坏客户占比的折线图的原因
    。当然，分箱后的单调性是否一定要遵从可能还是存在争议的，这个不是本文的重点。感兴趣的读者可以参考下面这两篇文章。
    :param df: 
    :param method: 
    :return: 
    """
    df['bad'] = list(map(lambda x: 1 if x == 1 else 0, df['target']))
    df['good'] = list(map(lambda x: 1 if x == 0 else 0, df['target']))
    bad_total = df['bad'].sum()
    good_total = df['good'].sum()
    iv_df = df.groupby(['bins']).agg({'bad': 'sum', 'good': 'sum'}).reset_index()
    iv_df['woe_i'] = np.log(iv_df['bad'] / iv_df['good']) - np.log((bad_total / good_total))
    iv_df['iv_i'] = iv_df['woe_i'] * (iv_df['bad'] / bad_total - iv_df['good'] / good_total)
    # print('WOE:{:.2f}\nIV:{:.2f}'.format(iv_df['woe_i'].sum(),iv_df['iv_i'].sum()))
    print('{}\nWOE:{:.2f}\nIV:{:.2f}'.format(method, iv_df['woe_i'].sum(), iv_df['iv_i'].sum()))


if __name__ == '__main__':
    # 等距分箱
    # equal_span()

    # 等频分箱
    # equal_freq()

    # 聚类分箱
    # kmeans_bin()

    # 卡方分箱
    # chi_bins()

    # Best-KS分箱
    KS_bin()

    # 决策树分箱
    # tree_bin()
