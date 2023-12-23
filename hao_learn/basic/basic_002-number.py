# Python基本数据类型-Number
'''
整数、浮点数、布尔、复数
'''
def basic_002_01():
    '''
    （1）整数
        python可以处理任意大小的整数，包含复数
    '''
    '''1）普通定义'''
    # 普通定义
    num1 = 10
    # id(变量名)：可以查看变量的内存地址
    # hex(十进制数字)：将十进制数字转为十六进制数字(0x为开头，不是数据内容部分)
    print(id(num1), hex(id(num1)))
    # type(变量名)：可以查看变量的类型，int表示整数数字
    print(type(num1))

    '''2）连续定义'''
    # 连续定义
    num2 = num3 = num4 = 5

    '''3）交互定义'''
    # 交互定义
    num5, num6 = 1, 2

    '''4）探究地址问题'''
    # 探究地址问题(小整数对象【-5~256】)
    # 多个变量等于小整数对象，则这些变量的地址相同，因为小整数经常使用，这样的话可以节省空间和提升效率
    num7 = 1
    num8 = 1
    print(id(num7), id(num8))  # 地址相同
    num9 = 501
    num10 = 501
    print(id(num9), id(num10))  # 地址不相同，需要在Linux下执行

    '''
    （2）浮点数
        由整数部分和小数部分组成，运算可能有四舍五入的误差
    '''
    num1 = 0.123434645
    num2 = 0.2
    print(num1 + num2)
    print(type(num1), hex(id(num1)))
    print(num1)

    '''
    （3）布尔值
        一个布尔类型的变量只有True、False两种值
        作用：作为真假的判断 
    '''
    a = True
    b = False
    print(a, b)

#  print
def basic_002_02():
    '''print'''
    height = 173.555
    print("haozhifeng is a good man!His height is %f" % (height))
    print("haozhifeng is a good man!His height is %.2f" % (height))
    age = 18
    print("haozhifeng is a nice man!He is *%d* years old" % (age))
    print("haozhifeng is a nice man!He is *%4d* years old" % (age))
    print("haozhifeng is a nice man!He is *%-4d* years old" % (age))

#  Python基本数据类型-Number数学函数
def basic_002_03():
    # 求绝对值
    num1 = 5
    num2 = abs(num1)
    print("num2 = %s" % (num2))
    # 求多个数中的最大值
    num3 = max(2, 3, 5, 6, 1, 5, 77, 54, 2)
    print("num3 = %s" % (num3))
    # 求多个数中的最小值
    print(min(2, 3, 5, 6, 1, 5, 77, 54, 2))
    # 求x的y次方   pow(x, y)
    print(pow(2, 3))
    # 四舍五入
    # round(x[, n])  【round(x)   round(x, n)】
    # 对x进行四舍五入，n表示保留小数点后的多少位
    print(round(3.1415926))
    print(round(3.1415926, 4))


    # 导入数学模块
    import math
    # 向上取整
    print(math.ceil(10.2))
    # 向下取整
    print(math.floor(10.9))
    # 得到浮点数的小数部分和整数部分
    # 得到的是一个元组，元组的第一个元素为小数部分，第二个元素为整数部分
    print(math.modf(10.3))
    # 开平方
    print(math.sqrt(10))

    # 导入随机模块
    import random
    # choice(seq)
    # 从序列（集合）中随机获取一个元素
    print(random.choice([1, 2, 4, 3, 5, 6, 7, 8, 9, 0]))
    # randrange([start,]stop[,step])
    # randrange(start,stop,step)
    # randrange(start,stop)
    # randrange(stop)
    # start：指定范围的开始值，包含在范围内，默认从0开始
    # stop：指定范围的结束值，不包含在范围内
    # step：指定阶跃值，默认为1
    print(random.randrange(1, 10, 2))
    print(random.randrange(1, 10))
    # random()
    # 随机生成一个实数，范围在[0, 1)之间，得到的是浮点数
    print(random.random())
    # uniform(x, y)
    # 随机生成一个实数，范围在[x, y]之间，得到一个浮点数
    print(random.uniform(3, 7))
    # randint(start, stop)
    # 在指定范围[start, stop]内得到一个整数
    print(random.randint(1, 4))

if __name__ == '__main__':
    #basic_002_01()
    #basic_002_02()
    basic_002_03()
