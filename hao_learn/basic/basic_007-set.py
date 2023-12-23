# Python基本数据类型-集合
'''
（1）特性：与dict类似，是一组key的集合(不存储value)
（2）本质：无序和无重复的集合
'''
def basic_007_01():
    '''
      （1）创建
    '''
    # 创建：需要用一个list或者tuple作为输入集合
    s1 = set([1, 2, 3, 4, 5])
    print(s1, type(s1))
    s2 = set((1, 2, 3, 4, 5))
    print(s2, type(s2))
    s3 = set("zutuanxue")
    print(s3, type(s3))

    '''
    （2）作用
    '''
    # 作用：列表去重
    li1 = [1, 2, 4, 6, 7, 5, 4, 3, 22, 2, 3, 46, 7, 8, 1, 3, 5]
    s4 = set(li1)
    li2 = list(s4)
    print(li2)


    '''
    （3）添加
    '''
    s5 = set([1, 2, 3, 4, 5])
    # 不能直接插入一个数字元素
    # s5.update(6) # 报错
    # s5.update([6,7,8])
    # s5.update((6,7,8))
    # s5.update("678")
    s5.update([(6, 7, 8)])
    print(s5)

    '''
    （4）删除
    '''
    s6 = set([1, 2, 3, 4, 5])
    # 从左侧开始删除
    data = s6.pop()
    print(data, s6)
    # 按元素删除，如果元素不存在报KeyError的异常
    s6.remove(4)
    # s6.remove(7)
    print(s6)

    '''
    （6）遍历
    '''
    s7 = set([1, 2, 3, 4, 5])
    for key in s7:
        print("--------", key)

    for index, key in enumerate(s7):
        print(index, key)

# 交集与并集
def basic_007_02():
    s8 = set([1, 2, 3, 4, 5])
    s9 = set([3, 4, 5, 6, 7])
    # 交集
    print(s8 & s9)
    # 并集
    print(s8 | s9)

if __name__ == '__main__':
    basic_007_01()
    basic_007_02()