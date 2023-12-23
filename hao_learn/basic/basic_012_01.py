# 流程控制-循环控制
'''
pass
（1）格式
    if 1:
        pass
（2）作用：当语句要求不希望任何命令或代码来执行时使用
（3）说明：pass语句表示一个空操作，在执行时没有任何的响应，pass的位置最终应该有代码来执行，只不过暂时写不出来可以使用在流程控制和循环语句中
'''
def basic_012_01():
    if 1:
        print("haozhifeng is a good man")
        print("haozhifeng is a nice man")
    if 1:
        print("haozhifeng is a good man")
        # 语句嵌套
        if 1 - 1:
            print("haozhifeng is a cool man")


'''
break
（1）作用：退出循环
    注意：只能跳出距离最近的for或者while循环
'''
def basic_012_02():
    for x in range(3):
        for y in range(5):
            if y == 3:
                break
            print("******", y)
        print("-------", x)

    # while循环语句可以有else子句，表达式为假时会被执行，但是使用break终止while循环后else中的子句不执行
    num = 0
    while num < 8:
        print("num = %d" % num)
        num += 1
        if num == 8:
            break
    else:
        print("--------else")


'''
continue
（1）作用：跳过本次循环后面的剩余语句，然后继续下一次循环
    注意：只能跳过距离最近的for或者while循环
'''


def basic_012_03():
    for x in range(10):
        if x == 5:
            continue
        print("x = %d" % x)

    num = 0
    while num < 10:
        if num == 5:
            num += 1
            continue
        print("num = %d" % num)
        num += 1


if __name__ == '__main__':
    basic_012_03()