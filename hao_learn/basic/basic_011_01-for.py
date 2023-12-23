# 流程控制-循环语句 for语句
'''
for语句
（1）格式
    for 变量名 in 集合:
        语句
（2）逻辑
    当程序执行到for语句时，按顺序从“集合”中获取元素，“变量”保存当前循环得到的集合中的元素值，再去执行“语句”。如此循环往复，直到取完“集合”中所有元素才停止.
'''
def basic_011_01():
    # 实现多次打印
    for x in [1, 2, 3, 4, 5]:
        print("----------%d" % x)

    '''
    range()
    原型：range([start, ]stop[, step])
    range(stop)
    range(start, stop)
    range(start, stop, step)
    功能：生成列表
    参数：
    start：表示列表起始值，包含， 默认为0
    stop：表示列表结束值，但是不包含
    step：阶跃值， 默认为1
    '''
    sum = 0
    for x in range(1, 101):
        sum += x
    print("sum = %d" % sum)

    #遍历列表
    words = ["good", "nice", "cool", "handsome"]
    # 遍历列表，获取到的是列表中的元素的值
    for word in words:
        print(word)
    # 同时遍历列表的下标和元素
    for index, word in enumerate(words):
        print(index, word)



if __name__ == '__main__':
    basic_011_01()
