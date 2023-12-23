# 流程控制-if判断语句
'''
if语句
（1）格式
    表达式:
        语句
（2）逻辑
    当程序运行到if语句时，首先计算“表达式”的值，如果“表达式”的值为真，则执行“语句”。如果“表达式”的值为假，则结束if语句继续向下执行
'''
def basic_009_01():
    if 1:
        print("haozhifeng is a good man")
        print("haozhifeng is a nice man")
    if 1:
        print("haozhifeng is a good man")
        # 语句嵌套
        if 1 - 1:
            print("haozhifeng is a cool man")


'''
if-else语句
（1）格式
    if 表达式:
        语句1
    else:
        语句2
（2）逻辑
    当程序运行到if-else语句时，首先计算“表达式”的值。如果“表达式”的值为真，则执行“语句1”，执行完“语句1”结束整个if-else语句继续向下执行。
    如果“表达式”的值为假，则执行“语句2”，执行完“语句2”结束整个if-else语句继续向下执行
'''
def basic_009_02():
    if 0:
        print("haozhifeng is a good man")
    else:
        print("haozhifeng is a nice man")

'''
if-elif-else语句
（1）格式
    if 表达式1:
        语句1
    elif 表达式2:
        语句2
    elif 表达式3:
        语句3
    ……
    elif 表达式n:
        语句n
    else:
        语句e
        
    注意：最后的else部分可有可无
（2）逻辑
    当程序运行到if-elif-else语句时，首先计算“表达式1”的值，如果“表达式1”的值为真则执行“语句1”，执行完“语句1”则结束整个if-elif-else语句继续向下执行。
    如果“表达式1”的值为假则计算“表达式2”的值，如果“表达式2”的值为真则执行“语句2”，执行完“语句2”则结束整个if-elif-else语句继续向下执行。
    如果“表达式2”的值为假则计算“表达式3”的值，如此直到某个表达式的值为假才停止，如果没有表达式为真且有else语句则执行“语句e”，否则结束整个if-elif-else语句继续向下执行
'''
def basic_009_03():
    num = int(input())

    # 使用if-elif-else语句
    if num == 1:
        print("星期一")
    elif num == 2:
        print("星期二")
    elif num == 3:
        print("星期三")
    elif num == 4:
        print("星期四")
    elif num == 5:
        print("星期五")
    elif num == 6:
        print("星期六")
    elif num == 7:
        print("星期日")
    else:
        print("输入有误")

if __name__ == '__main__':
    #basic_009_01()
    #basic_009_02
    basic_009_03()