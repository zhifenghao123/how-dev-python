# Python 迭代器与生成器
'''
可迭代对象
（1）概念
可以直接作用于for循环的对象统称为可迭代对象(Iterable)
（2）可以直接作用于for循环的数据类型
    1）集合数据类型(list、tuple、dict、set、string)
    2）generator
        a、生成器
        b、带yield的generator function
'''
def basic_014_01():
    # from collections import Iterable python3.11 已经废弃collections
    from typing import Iterable
    # 格式
    # isinstance(obj, type)：判断obj是否属于type类型

    print(isinstance([], Iterable))
    print(isinstance((), Iterable))
    print(isinstance({}, Iterable))
    print(isinstance("", Iterable))
    print(isinstance(range(10), Iterable))
    print(isinstance(100, Iterable))

'''
迭代器
（1）概念
    可以被next()函数调用并返回一个值的对象为迭代器对象
    迭代器不但可以用于for，还可以用于next()
（2）为什么list、tuple、dict、string、set等数据类型不是Iterator？
    Iterator对象表示的是一个流数据，Iterator对象可以被next()调用并返回一个数据，直到抛出StopIteration异常错误则停止。
    可以把数据流看成一个有序的序列，但是不确定这个序列的长度，只能通过next()函数不断计算求值，Iterator可以表示一个无限大的数据流，而list等永远不可能存储无限的数据
'''
def basic_014_02():
    # 转成Iterator对象
    li = [1, 2, 3, 4, 5]
    g = iter(li)
    print(g, type(g))
    print(next(g))
    print(next(g))

'''
列表生成式
    列表推导式提供了从序列创建列表的简单途径。
'''
def basic_014_03():
    #循环生成列表,缺点：循环比较繁琐
    li = []
    for i in range(1, 11):
        li.append(pow(i, 2))
    print(li)

    '''
    1）列表推导式---一般形式
    '''
    li2 = [x * x for x in range(1, 11)]
    print(li2)

    '''
    2）列表推导式---一添加判断
    '''
    li3 = [x * x for x in range(1, 11) if x % 2 == 0]
    print(li3)

    '''
    3）列表推导式---一般形式
    '''
    li4 = [x + y for x in "ABC" for y in "123"]
    print(li4)

'''
生成器
（1）概述
    推导的算法比较复杂，用给列表生成式的for循环无法实现的时候，可以选择使用函数得到生成器
（2）注意
    1）函数时顺序执行，遇到return语句后最后一行代码就返回
    2）如果想让一个函数变为生成器函数，只需将函数中的return改为yield
    3）执行生成器函数不会执行函数代码，得到一个生成器
    4）在每次调用next()的时候，会执行生成器函数，遇到yield语句就返回，如果再次执行next()
'''
def basic_014_04():
    # 函数
    def func1():
        print("haozhifeng is a good man")
        print("haozhifeng is a nice man")
        print("haozhifeng is a cool man")
        print("haozhifeng is a handsome man")
        return 1

    # 生成器函数
    def func2():
        print("haozhifeng is a good man")
        print("haozhifeng is a nice man")
        print("haozhifeng is a cool man")
        print("haozhifeng is a handsome man")
        yield 2

    def func3():
        print("haozhifeng is a good man")
        yield 1
        print("haozhifeng is a nice man")
        yield 2
        print("haozhifeng is a cool man")
        yield 3
        print("haozhifeng is a handsome man")
        yield 4

    res1 = func1()
    res2 = func2()
    res3 = func3()
    print(res1, type(res1))
    print(res2, type(res2))
    print(res3, type(res3))

    print("------------------")
    print(next(res3))
    print(next(res3))
    print(next(res3))
    print(next(res3))

    def func4():
        for i in range(1, 11):
            yield pow(i, 2)

    g2 = func4()
    for x in g2:
        print("-----------", x)


if __name__ == '__main__':
    #basic_014_01()
    #basic_014_02()
    #basic_014_03()
    basic_014_04()