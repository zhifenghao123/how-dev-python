import matplotlib.pyplot as plt

def pyplot_pie_test():
    """
    matplotlib 饼图绘制
    :return:
    """

    # 设置字体以便支持中文
    plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 防止中文乱码
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    # 设置图片大小和分辨率
    plt.figure(figsize=(9, 6), dpi=100)
    x = [217, 743, 426]
    labels = ['走路去', '自行车', '公交车']
    explode = [0, 0.01, 0]

    # _, _, autotexts = plt.pie(x=x, labels=labels, shadow=1, autopct='%.1f%%', explode=explode)

    # 绘制饼图
    _, _, autotexts = plt.pie(x=x,
                explode=explode,
                labels=labels,  # 添加教育水平标签
                colors=['#9999ff', '#ff9999', '#7777aa'],  # 设置饼图颜色自定义填充颜色
                autopct='%.2f%%',  # 设置百分比的格式，这里保留2位小数
                pctdistance=0.8,  # 设置百分比标签与圆心的距离
                labeldistance=1.2,  # 设置教育水平标签与圆心的距离
                startangle=180,  # 设置饼图的初始角度
                radius=1.5,  # 设置饼图的半径
                counterclock=False,  # 是否逆时针，这里设置为顺时针方向
                wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},
                # 设置饼图内外边界属性值
                textprops={'fontsize': 12, 'color': 'k'},
                # 设置文本标签属性值
                center=(2, 2),  # 设置饼图的原点
                frame=0)  # 是否显示饼图图框，这里没有显示

    # 将饼图中的字体改为白色
    for autotext in autotexts:
        autotext.set_color('white')
    plt.title('三种去学校的方式')
    plt.show()

if __name__ == '__main__':
    pyplot_pie_test()