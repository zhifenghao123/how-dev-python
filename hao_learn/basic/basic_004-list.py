# Python基本数据类型-列表
'''
本质：是一个有序集合
'''
def basic_004_01():
    '''
    （1）创建列表
        格式：列表名 = [元素1, 元素2, ……, 元素n]
    '''
    # 创建空列表
    li1 = []
    print(li1, type(li1))

    # 创建带有元素的列表
    # 注意：列表中元素的类型可以不同，但是在今后的开发中一般不存在这种状况
    li2 = [1, 2, 3, 4, 5, "good", True]
    print(li2)

    '''
    （2）列表元素的访问
    '''
    # 列表元素的访问
    li3 = [1, 2, 3, 4, 5]
    # 往列表末尾添加元素
    li3.append(6)
    # 获取元素  列表名[下标]
    print(li3[2])
    # print(li3[9]) #下标超出范围，溢出
    # print(li3[-1]) # 下标可以是负数，-1表示最后一个元素的下标，-2表示倒数第二个，依次类推
    # 修改元素 列表名[下标] = 值
    li3[2] = 33
    # li3[6] = 10 #下标不存在
    print(li3)
    # 截取列表
    print(li3[1:3])
    print(li3[1:])
    print(li3[:3])

    '''
    （3）列表操作
    '''
    # 列表相加（列表组合）
    li4 = [1, 2, 3]
    li5 = [4, 5, 6]
    li6 = li4 + li5
    print(li6)
    # 列表相乘（列表重复）
    li7 = [7, 8, 9]
    li8 = li7 * 3
    print(li7)
    print(li8)
    # 成员判断
    li9 = [1, 2, 3]
    print(1 in li9)
    print(4 in li9)

# 二维列表
def basic_004_02():
    '''
    概念：列表中的元素是一位列表的列表
    本质：一维列表
    '''
    li1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]

    print(li1[1][1])

# 内置功能
def basic_004_03():
    '''
    （1）append(obj)
    在列表的末尾添加一个新的元素
    '''
    li1 = [1, 2, 3, 4, 5]
    li1.append(6)
    li1.append([7, 8, 9])
    print(li1)

    '''
    （2）extend(seq)
    在列表的末尾一次追加多个元素
    '''
    li2 = [1, 2, 3, 4, 5]
    li2.extend([6, 7, 8])
    print(li2)

    '''
    （3）insert(index, obj)
    将元素obj按下标插入列表，不会覆盖原数据，原数据会按顺序后移
    '''
    li3 = [1, 2, 3, 4, 5]
    li3.insert(2, 100)
    print(li3)

    '''
    （4）pop(index=-1)
    移除列表中指定下标出的元素，默认移除最后一个，返回被删掉的数据
    '''
    li4 = [1, 2, 3, 4, 5]
    data = li4.pop()
    print(data, li4)

    '''
    （5）remove(obj)
    移除列表中第一次出现的obj元素
    '''
    li5 = [1, 2, 3, 4, 5, 2, 4, 2, 5, 6, 7]
    li5.remove(2)
    print(li5)

    '''
    （6）clear()
    清空列表
    '''
    li6 = [1, 2, 3, 4, 5]
    li6.clear()
    print(li6)

    '''
    （7）count(obj)
    返回元素obj在列表中出现的次数
    '''
    li7 = [1, 2, 3, 4, 5, 2, 4, 2, 5, 6, 7]
    print(li7.count(2))

    '''
    （8）len(seq)
    返回列表中元素的个数
    '''
    li8 = [1, 2, 3, 4, 5]
    print(len(li8))

    '''
    （9）index(obj)
    在列表中获取元素第一次出现的下标，没有则会抛出ValueError异常
    '''
    li9 = [1, 2, 3, 4, 5, 2, 4, 2, 5, 6, 7]
    print(li9.index(2))

    '''
    （10）max(seq)
    返回列表中最大的元素
    '''
    print(max([2, 3, 4, 1, 4, 6, 7, 3]))

    '''
    （11）min(seq)
    返回列表中最小的元素
    '''
    '''
    （12）reverse()
    列表倒序
    '''
    li10 = [1, 2, 3, 4, 5]
    li10.reverse()
    print(li10)

    '''
    （13）sort()
    根据func函数给定的规则进行列表元素的排序，默认升序
    '''
    li11 = [2, 1, 3, 5, 4]
    li11.sort()
    print(li11)

    '''
    （14）list(seq)
    将其他类型的集合转为列表类型
    '''
    str1 = "baism"
    li12 = list(str1)
    print(li12, type(li12))


# 内存问题
def basic_004_04():
    '''
    （1）赋值
    '''
    # == 与is
    num1 = 1
    num2 = 1
    print(id(num1), id(num2))
    print(num1 == num2)
    print(num1 is num2)
    num3 = 401
    num4 = 401
    print(id(num3), id(num4))
    print(num3 == num4)
    print(num3 is num4)

    #赋值
    a = [1, 2, 3, 4, 5]
    b = a
    print(id(a), id(b))
    print(a == b)
    print(a is b)
    c = [1, 2, 3, 4, 5, [7, 100, 9]]
    d = c
    print(c == d)
    print(c is d)
    c[5][0] = 60
    print(c)
    print(d)

    '''
    浅拷贝
    只拷贝表层元素
    '''
    from copy import copy

    a = [1, 2, 3, 4, 5]
    b = copy(a)
    print(id(a), id(b))
    print(a == b)
    print(a is b)

    c = [1, 2, 3, [4, 5, 6]]
    d = copy(c)
    print(id(c), id(d))
    print(c == d)
    print(c is d)
    print(id(c[3]), id(d[3]))
    print(c[3] == d[3])
    print(c[3] is d[3])

    '''
    深拷贝
    注意：不论深拷贝还是浅拷贝都会在内存中生成一片新的内容空间(把拷贝的内容在内存中重新创建一份)
    两者有区别的前提：元素中有另外的列表
    说明：深拷贝在内存中重新创建所有子元素
    '''
    from copy import deepcopy

    a = [1, 2, 3, 4, 5]
    b = deepcopy(a)
    print(id(a), id(b))
    print(a == b)
    print(a is b)

    c = [1, 2, 3, 4, 5, [6, 7, 8]]
    d = deepcopy(c)
    print(id(c), id(d))
    print(c == d)
    print(c is d)
    print(id(c[5]), id(d[5]))
    print(c[5] == d[5])
    print(c[5] is d[5])


if __name__ == '__main__':
    basic_004_01()
    basic_004_02()
    basic_004_03()
    basic_004_04()
