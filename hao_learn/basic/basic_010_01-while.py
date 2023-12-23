# 流程控制-循环语句
'''
while语句
（1）格式
    while 表达式:
        语句
（2）逻辑
    当程序执行到while语句时，首先计算“表达式”的值。如果表达式的值为假则结束整个while语句继续向下执行，如果“表达式”的值为真则执行“语句”，执行完“语句”再次计算“表达式”的值。
    如果表达式的值为假则结束整个while语句继续向下执行，如果“表达式”的值为真则执行“语句”，执行完“语句”再次计算“表达式”的值。如此循环往复直到“表达式”的值为假才停止循环
'''
def basic_010_01():
    num = 1
    sum = 0
    while num <= 100:
        sum = sum + num
        num += 1
    print("sum = %d" % sum)


'''
while-else语句
（1）格式
    while 表达式:
        语句1
    else:
        语句2
（2）逻辑
    当“表达式”的值为假时会执行“语句2”，执行完“语句2”结束整个while-else语句继续向下执行
'''
def basic_010_02():
    num = 1
    sum = 0
    while num <= 5:
        sum = sum + num
        num += 1
    else:
        print("%d不符合条件" % num)
    print("sum = %d" % sum)


if __name__ == '__main__':
    #basic_010_01()
    basic_010_02()
