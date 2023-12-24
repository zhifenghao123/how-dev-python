# Python代码异常
'''
try...except...
（1）格式
    try:
        语句t
    except 错误表示码1 as e:
        语句1
    except 错误表示码2 as e:
        语句2
    ...
    except 错误表示码n as e:
        语句n
（2）作用
    用来检测“语句t”的错误，从而让except语句捕获异常进行处理
（3）逻辑
    1）如果“语句t”执行时发送异常，就跳回到执行try并执行一个匹配该异常的except子句，异常处理结束就结束整个try……except语句(除非处理异常时又引发了新的异常)
    2）如果“语句t”执行时发送异常，但是却没有匹配的except子句，异常提交到上一级try,或者到程序的最上层
    3）如果“语句t”执行时没有异常，就不会匹配except子句。结束整个try……except……语句继续向下执行

'''
def basic_015_01():
    #基本使用
    try:
        1 / 0
    except ZeroDivisionError as e:
        print("----------1")
        print(e, type(e))
        print(str(e))
    except KeyError as e:
        print("----------2")

    #特殊使用
    #使用except而不带任何错误表示码，捕获任意的异常
    try:
        1 / 0
    except:
        print("有错误")

    #使用except而带有多种错误表示码，同时匹配多种异常，只要符合其中之一即可捕获
    try:
        1 / 0
    except (ZeroDivisionError, KeyError, AttributeError) as e:
        print("------")

    #使用注意事项
    #python中的错误表示码实际上是类，所有的错误类都继承自BaseException，所以在使用时注意父类会将子类错误一网打尽
    try:
        1 / 0
    except BaseException as e:
        print("------1")
    except ZeroDivisionError as e:
        print("------2")
    #跨多层调用，main里调用f2，f2里调用f1，在f1里出错了，只需要再main里捕获就可以处理
    def f1():
        ret = 1 / 0
        return ret

    def f2():
        f1()

    try:
        f2()
    except ZeroDivisionError as e:
        print("----------")

'''
try...except...else
（1）格式
    try:
        语句t
    except 错误表示码1 as e:
        语句1
    except 错误表示码2 as e:
        语句2
    ...
    except 错误表示码n as e:
        语句n
    else:
        语句e
（2）逻辑
    1）如果“语句t”执行时发送异常，就跳回到执行try并执行一个匹配该异常的except子句，异常处理结束就结束整个try……except……else语句(除非处理异常时又引发了新的异常)
    2）如果“语句t”执行时发送异常，但是却没有匹配的except子句，异常提交到上一级try,或者到程序的最上层
    3）如果“语句t”执行时没有异常，就不会匹配except子句。如果有else语句则执行“语句e”,执行完则结束整个try……except……else语句继续向下执行
'''
def basic_015_02():
    try:
        1 / 0
    except ZeroDivisionError as e:
        print("************")
    else:
        print("---------")


'''
try...except...finally
（1）格式
    try:
        语句t
    except 错误表示码1 as e:
        语句1
    except 错误表示码2 as e:
        语句2
    ...
    except 错误表示码n as e:
        语句n
    finally:
        语句f
（2）作用
    无论try中的语句是否发生异常，都将执行“语句f”
'''
def basic_015_03():
    try:
        1 / 1
    except ZeroDivisionError as e:
        print("************")
    finally:
        print("---------")



if __name__ == '__main__':
    basic_015_01()
    basic_015_02()
    basic_015_03()