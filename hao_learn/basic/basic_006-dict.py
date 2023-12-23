# Python基本数据类型-字典
'''
（1）概念
    使用键值对(key-value)的形式存储数据，具有极快的查找速度
（2）特性
    1）字典中的key必须唯一
    2）键值对是无序的
    3）key必须是不可变对象
        a：字符串、数字都是不可变的，可以作为key（一般为字符串）
        b：列表是可变的，不能作为key
'''
def basic_006_01():
    '''
    （1）创建
    定义格式：字典名 = {key1:value1, key2:value2,……,keyn:valuen}
    '''
    # 创建一个字典保存一个学生信息
    stu1 = {"name": "zutuanxue", "age": 18, "sex": "男", "height": 173.5, "weight": 80, "id": 1}
    stu2 = {"name": "liudh", "age": 57, "sex": "男", "height": 180, "weight": 75, "id": 2}

    stus = [stu1, stu2]

    '''
    （2）访问字典的值
    '''
    stu3 = {"name": "zutuanxue", "age": 18, "sex": "男", "height": 173.5, "weight": 80, "id": 1}
    # 获取  字典名[key]
    print(stu3["name"])
    # print(stu3["money"]) #获取不存在的属性值会报错

    # 获取  字典名.get(key)
    print(stu3.get("age"))
    print(stu3.get("money"))  # 获取不存在的属性会得到None
    money = stu3.get("money")
    if money:
        print("money = %d" % money)
    else:
        print("没有money属性")

    '''
    （3）添加键值对
    '''
    # 添加键值对，没有的键会添加，有的会修改
    stu3["nikeName"] = "kaige"
    stu3["age"] = 16

    '''
    （4）删除
    '''
    stu3.pop("nikeName")
    print(stu3)


if __name__ == '__main__':
    basic_006_01()