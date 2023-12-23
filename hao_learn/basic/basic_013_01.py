# 流程控制-循环控制
'''
遍历字典
'''
def basic_013_01():
    stu = {"name": "zutuanxue_com", "age": 18, "sex": "男", "height": 173.5, "weight":80, "id": 1}
    '''
    遍历字典的key
    '''
    for key in stu:
        print(key, stu[key])

    '''
    遍历字典元素
    '''
    for value in stu.values():
        print(value)


    '''
    遍历字典的Key和Value
    '''
    for key, value in stu.items():
        print(key, value)

    '''
    枚举遍历，可以得到类似下标的顺序值，但是注意，字典是无序的
    '''
    for index, key in enumerate(stu):
        print(index, key)

'''
遍历set集合
'''
def basic_013_02():
    s = set([1,2,3,4,5])
    for key in s:
        print("--------", key)

    for index, key in enumerate(s):
        print(index, key)



if __name__ == '__main__':
    basic_013_01()
    basic_013_02()