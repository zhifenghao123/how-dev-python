# Python基本数据类型-字符串
def basic_003_01():
    '''
    （1）字符串是以单引号或者双引号括起来的任意文本
        注意：
        1）引号本身是一种表现形式，不属于字符串的内容
        2）如果字符串本身带单引号，外侧用双引号包裹起来（“he’s a good man”）
    '''
    str1 = 'zutuanxue is a good man'
    str2 = "zutuanxue is a nice man"

    '''
    （2）多行字符
    以三个单引号 或者 三个双引号 引起来的任意文本
    '''
    str3 = '''
    good
    nice
    cool
    handsome'''

    str4 = """
    good
    nice
    cool
    handsome"""
    print(str3)
    print(str4)

# 知识点2：Python字符串基本使用
def basic_003_02():
    # 创建字符串
    str1 = str("zutuanxue is a good man")
    # 基本类型字符串在使用是会自动转变为字符串对象类型
    str1 = 'zutuanxue is a nice man'

    # 字符串运算
    str3 = "zutuanxue is a cool man"
    str4 = "zutuanxue is a handsome man"
    # 字符串加法（字符串拼接）
    str5 = str3 + str4
    print("str5= %s" % (str5))
    # 字符串乘法（重复字符串）
    str6 = str3 * 3
    print("str6= %s" % (str6))

    # 成员判断
    str7 = "zutuanxue is a good man"
    print("zutuanxue" in str7)

    # 内容获取
    str8 = "zutuanxue is a good man"
    # 根据下标(索引)获取字符串中的内容，下标从0开始
    # 字符串[下标]
    print(str8[2])
    # 截取字符串中的一部分 字符串[start:stop]   [start, stop)
    print(str8[1:4])
    print(str8[1:])
    print(str8[:4])

# 知识点3：Python字符串格式化打印
def basic_003_03():
    '''
    格式化打印
    %s              %d      %f
    格式化字符串  格式化整数   格式化浮点数字，可指定小数点后的精度
    '''
    name = "zutuanxue"
    age = 18
    height = 175.5
    print("我叫%s，我今年%d岁，身高%f，具体身高%.1f" % (name, age, height, height))

    # 已知print的内容默认是打印在一行的，另一个print会另起一行再打印
    # end默认为\n
    print("zutuanxue is a good", end="*")
    print(" man")

# 知识点4：Python字符串-常用转义字符
def basic_003_04():
    '''
    常用转义字符
    \n          \t          \\          \"       \'
    换行符	 横向制表符	    反斜杠	    双引号	    单引号
    '''
    str12 = "c\\oo\tl is a go\no m\"a'n"
    print(str12)
    # 如果字符串里有很多字符需要转义，就需要加入很多\，为了简化，python允许使用r""表示，""内部的字符串默认不转义
    #  \\\t\\
    print("\\\t\\")
    print("\\\\\\t\\\\")
    print(r"\\\t\\")

# 知识点5：Python字符串-内置功能
def basic_003_05():
    '''
    （1）比较大小
    原理：按顺序从两个字符串中从左侧开始获取字符，比较两个字符，谁的阿斯科玛值大那么就是哪个字符串大，如果相等，则继续比较下一个
    '''
    str1 = "abc"
    str2 = "ab"
    print(str1 > str2)

    '''
    （2）eval()
    原型：eval(str)
    功能：将字符串当成有效的表达式来求值并返回结果
    返回值：计算后得到的数字
    
    注意：字符串本身是不可以改变的
    '''
    num = eval("123")
    print(num, type(num))
    # print(int("12+3")) #报错
    print(eval("12+3"))
    print(eval("+123"))
    print(eval("-123"))
    print(eval("12-3"))
    print(eval("12*3"))

    # 注意：字符串中有非数字字符会报错(数学运算符除外)
    # print(eval("12a3")) #报错
    # print(eval("a123")) #报错
    # print(eval("123a")) #报错
    # 表示的是变量是可以的
    a = "124"
    print(eval("a"))
    # print(eval("a+1")) #报错

    '''
    （3）len(string)
    原型：len(str)
    功能：计算字符串的长度(按字符个数计算)
    参数：一个字符串
    返回值：字符串的长度
    '''
    print(len("zutuanxue is a good man"))
    print(len("zutuanxue is a good man凯"))

    '''
    （4）lower()
    原型：lower()
    功能：将字符串中所有大写英文字母转为小写
    '''
    str1 = "zutuanxue Is a GoOd MAn!"
    str2 = str1.lower()
    print(str1)
    print(str2)

    '''
    （5）upper()
    原型：upper()
    功能：将字符串中所有小写英文字母转为大写
    '''
    str3 = "zutuanxue Is a GoOd MAn!"
    str4 = str3.upper()
    print(str3)
    print(str4)

    '''
    （6）swapcase()
    原型：swapcase()
    功能：将字符串中的大写英文字母转为小写，小写英文字母转为大写
    '''
    str5 = "zutuanxue Is a GoOd MAn!"
    str6 = str5.swapcase()
    print(str5)
    print(str6)

    '''
    （7）capitalize()
    原型：capitalize()
    功能：将字符串中第一个字符转为大写，其余转为小写
    '''
    str7 = "zutuanxue Is a GoOd MAn!"
    str8 = str7.capitalize()
    print(str7)
    print(str8)

    '''
    （8）title()
    原型：title()
    功能：得到“标题化”的字符串，每个单词的首字符大写，其余小写
    '''
    str9 = "zutuanxue Is a GoOd MAn!"
    str10 = str9.title()
    print(str10)

    '''
    （9）center(width[, fillchar])
    功能：返回一个指定width宽度的居中字符串，fillchar为填充字符串，默认为空格
    '''
    print("zutuanxue".center(20, "#"))

    '''
    （10）ljust(width[, fillchar])
    功能：返回一个指定width宽度的左对齐字符串，fillchar为填充字符串，默认为空格
    '''
    print("zutuanxue".ljust(20, "#"))

    '''
    （11）rjust(width, [, fillchar])
    功能：返回一个指定width宽度的右对齐字符串，fillchar为填充字符串，默认为空格
    '''
    print("zutuanxue".rjust(20, "#"))

    '''
    （12）zfill(width)
    功能：返回一个指定width宽度的右对齐字符串，默认填充0
    '''
    print("zutuanxue".zfill(20))

    '''
    （13）count(str[, beg=0[, end=len(string)]])
    功能：返回str在string中出现的次数，如果beg或者end指定则返回指定范围内的出现次数
    '''
    str11 = "zutuanxue is a very very good man very"
    print(str11.count("very"))
    print(str11.count("very", 13))
    print(str11.count("very", 13, 25))

    '''
    （14）find(str[, beg=0[, end=len(string)]])
    功能：检测str是否包含在string中，默认从左到右查找，如果存在则返回第一次出现的下标，否则返回 - 1，如果beg或者end指定则在指定范围内检测
    '''
    str12 = "zutuanxue is a very very good man"
    print(str12.find("very"))
    # print(str12.find("nice"))

    '''
    （15）index(str[, beg=0[, end=len(string)]])
    功能：检测str是否包含在string中，默认从左到右查找，如果存在则返回第一次出现的下标，否则返回异常(报错)，如果beg或者end指定则在指定范围内检测
    '''
    str13 = "zutuanxue is a very very good man"
    print(str13.index("very"))
    # print(str13.index("nice"))

    '''
    （16）rfind(str[, beg=0[, end=len(string)]])
    功能：检测str是否包含在string中，默认从右到左查找，如果存在则返回第一次出现的下标，否则返回 - 1，如果beg或者end指定则在指定范围内检测
    '''
    str12 = "zutuanxue is a very very good man"
    print(str12.rfind("very"))
    # print(str12.rfind("nice"))

    '''
    （17）rindex(str[, beg=0[, end=len(string)]])
    功能：检测str是否包含在string中，默认从右到左查找，如果存在则返回第一次出现的下标，否则返回异常(报错)，如果beg或者end指定则在指定范围内检测
    '''
    str13 = "zutuanxue is a very very good man"
    print(str13.rindex("very"))
    # print(str13.rindex("nice"))

    '''
    （18）lstrip([char])
    功能：截掉字符串左侧指定的字符，默认为空格
    '''
    str14 = "     zutuanxue is a good man"
    str15 = str14.lstrip()
    print(str14)
    print(str15)
    str16 = "######zutuanxue is a good man"
    str17 = str16.lstrip("#")
    print(str16)
    print(str17)

    '''
    （19）rstrip([char])
    功能：截掉字符右左侧指定的字符，默认为空格
    '''
    str18 = "zutuanxue is a good man      "
    str19 = str18.rstrip()
    print(str18, "*")
    print(str19, "*")

    '''
    （20）strip([chars])
    功能：在字符串上执行lstrip和rstrip

    （21）split(str=" "[, num=string.count(str)])
    功能：按照str(默人空格)
    切割字符串，得到一个列表，列表是每个单词的集合
    '''
    str20 = "zutuanxue     is  a good man"
    print(str20.split())
    print(str20.split(" "))
    str21 = "zutuanxue####is##a#good#man"
    print(str21.split("#"))

    '''
    （22）splitlines([keepends])
    功能：按照行(’\r’、’\r\n’、’\n’)切割，如果keepends为False，不包含换行符，否则包含换行符
    '''
    str22 = """good
    nice
    cool
    handsome
    """
    print(str22.splitlines())
    print(str22.splitlines(False))
    print(str22.splitlines(True))

    '''
    （23）join(seq)
    功能：指定字符拼接列表中的字符串元素
    '''
    str23 = "zutuanxue is a good man"
    li = str23.split()
    str24 = "##".join(li)

    '''
    （24）max(str)
    功能：返回字符串中最大的字符
    '''
    print(max("abcdef"))

    '''
    （25）min(str)
    功能：返回字符串中最小的字符
    '''
    print(min("abcdef"))

    '''
    （26）replace(old, new[, max])
    功能：将字符串中的old替换为new，如果没有指定max值，则全部替换，如果指定max值，则替换不超过max次
    '''
    str25 = "zutuanxue is a good good good man"
    str26 = str25.replace("good", "cool")
    print(str26)

    '''
    （27）maketrans()
    功能：创建字符映射的转换表
    '''
    t = str.maketrans("un", "ab")

    '''
    （28）translate(table, deletechars="")
    功能：根据给出的转换表转换字符
    '''
    str27 = "zutuanxue is a good man"
    str28 = str27.translate(t)
    print(str28)

    '''
    （29）isalpha()
    功能：如果字符串至少有一个字符并且所有的字符都是英文字母则返回真，否则返回假
    '''
    print("abc".isalpha())
    print("ab1c".isalpha())

    '''
    （30）isalnum()
    功能：如果字符串至少有一个字符并且所有的字符都是英文字母或数字字符则返回真，否则返回假
    '''
    print("abc1".isalnum())
    print("abc".isalnum())
    print("1234".isalnum())

    '''
    （31）isupper()
    功能：如果字符串至少有一个字符并且所有的字母都是大写字母则返回真，否则返回假
    '''
    print("12AB".isupper())
    print("12ABc".isupper())

    '''
    （32）islower()
    功能：如果字符串至少有一个字符并且所有的字母都是小写字母则返回真，否则返回假
    
    （33）istitle()
    功能：如果字符串是标题化的则返回真，否则返回假
    
    （34）isdigit()
    功能：如果字符串只包含数字则返回真，否则返回假
    '''
    print("1234".isdigit())
    print("1234a".isdigit())
    '''
    （35）isnumeric()
    功能：如果字符串只包含数字则返回真，否则返回假

    （36）isdecimal()
    功能：检测字符串是否只包含十进制数字

    （37）isspace()
    功能：如果字符串只包含空白符则返回真，否则返回假
    '''
    print("".isspace())
    print(" ".isspace())
    print("\t".isspace())
    print("\n".isspace())
    print("\r".isspace())
    print("\r\n".isspace())
    print("   abc".isspace())

    '''
    （38）startswith(str[, beg=0[, end=len(string)]])
    功能：检测字符串是否以str开头，是则返回真，否则返回假，可指定范围

    str29 = "zutuanxue is a good man"
    print(str29.startswith("kaige"))
    
    （39）endswith(suffix, beg=0, end=len(string))
    功能：检测字符串是否以str结尾，是则返回真，否则返回假，可指定范围

    （40）encode(encoding=‘UTF - 8’, errors =‘strict’)
    功能：以encoding指定的编码格式进行编码，如果出错报一个ValueError的异常，除非errors指定的值是ignore或replace
    '''
    str30 = "zutuanxue是一个好男人"
    str31 = str30.encode()
    print(str31, type(str31))

    '''
    （41）bytes.decode(encoding=“utf - 8”, errors =“strict”)
    功能：以encoding指定的格式进行解码，注意解码时使用的格式要与编码时的一致
    '''
    str32 = str31.decode("GBK", errors="ignore")
    print(str32, type(str32))

    '''
    （42）ord()
    功能：获取字符的整数表示
    '''
    print(ord("a"))

    '''
    （43）chr()
    功能：把数字编码转为对应的字符
    '''
    print(chr(97))

    '''
    （44）str()
    功能：转为字符串
    '''
    num1 = 10
    str33 = str(num1)
    print(str33, type(str33))

if __name__ == '__main__':
    basic_003_01()
    basic_003_02()
    basic_003_03()
    basic_003_04()
    basic_003_05()