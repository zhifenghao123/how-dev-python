# Python 对文件的IO操作
'''
读文件
过程
（1）找到文件
（2）打开文件
（3）读取文件的内容
（4）关闭文件
'''
def basic_016_01():
    '''
    （1）找到文件
    绝对路径：从根目录开始链接的路径
    相对路径：不是从根目录开始链接的路径

    path = r"file.txt"
    '''

    '''
    （2）打开文件
        1）原型
        def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
        2）参数
            file：要打开的文件的路径
            mode：打开方式
            encoding：编码格式
            errors：错误处理方式（ignore表示直接忽略）
        3）返回值
            文件描述符，从当前的位置操作当前打开的文件
        4）打开方式
            方式	说明
            r	以只读的方式打开文件，文件的引用(描述符)将会被放在文件开头
            rb	以二进制格式打开只读文件，文件的引用(描述符)将会被放在文件开头
            r+	以读写的方式打开文件，文件的引用(描述符)将会被放在文件开头
            w	以只写的方式打开文件，如果该文件存在，则将其内容覆盖，如果文件不存在则会创建该文件
            wb	以二进制格式打开只写文件，如果该文件存在，则将其内容覆盖，如果文件不存在则会创建该文件
            w+	以读写的方式打开文件，如果该文件存在，则将其内容覆盖，如果文件不存在则会创建该文件
            a	打开一个文件用于追加内容，如果该文件存在，文件描述符会被放到文件的末尾，如果文件不存在则会创建该文件
            a+	打开一个文件用于读写，如果该文件存在，文件描述符会被放到文件的末尾，如果文件不存在则会创建该文件
        
            #打开普通文件
            fp = open(path, "r")
            #打开二进制文件
            fp = open(path, "rb")
            #指定编码格式
            fp = open(path, "r", encoding="utf-8")
            #指定错误处理方式
            fp = open(path, "r", encoding="utf-8", errors="ignore")
    '''

    '''
    （3）读取文件的内容
        1）读取文件的全部内容
            str1 = fp.read()
            print(str1)
        2）读取指定字节数的内容
            str2 = fp.read(4)
            print(str2)
        3）读取整行内容(包括\n字符)
            str3 = fp.readline()
            print("*"+str3+"*")
        4）读取指定字节数内容
            str4 = fp.readline(13)
            print("*"+str4+"*")
        5）读取所有行并返回一个列表，列表中的元素是每行内容
            list5 = fp.readlines()
            print(list5)
    '''

    '''
    （4）关闭文件
        1）注意
        文件使用过后必须关闭
        2）原因
        释放资源，系统能打开的文件个数是有限制的，所以需要释放相应文件的文件描述符
        3）关闭方式
        程序结束自动关闭：程序结束时会释放文件对象的空间，文件会关闭，但是不建议这样来做，最好手动关闭
        手动关闭：调用代码关闭

        fp.close()
    '''
    try:
        fp = open("testdata/python_file_1.txt", "r")
        print(fp.read())
    finally:
        if fp:
            fp.close()

    with open("testdata/python_file_1.txt", "r") as fp:
        print(fp.read())

'''
写文件
过程
（1）找到文件
（2）打开文件
（3）将内容写入缓冲区，此时内容没有写入文件
（4）刷新缓冲区，直接把缓存区中的数据立刻写入文件
    刷新缓冲区方式：1）程序结束；2）关闭文件；3）手动刷新（ fp.flush() ）；4）缓冲区满了；5）遇到\n
（5）关闭文件
'''
def basic_016_02():
    try:
        fp = open("file.txt", "w")
        fp.write("cool man")
    finally:
        if fp:
            fp.close()

    with open("file.txt", "w") as fp:
        fp.write("cool man")


'''
编码与解码
'''
def basic_016_03():
    #编码
    with open("file.txt", "wb") as fp:
        s = "sunck is a good man凯"
        s = s.encode("utf-8")
        fp.write(s)

    #解码
    with open("file.txt", "rb") as fp:
        s = fp.read()
        s = s.decode("utf-8")
        print(s)

'''
特殊的读写
'''
def basic_016_04():
    '''
    list、tuple、dict、set的文件操作
    pickle模块
    持久化保存对象，将list、tuple、dict、set等数据序列化存储到文件
    '''
    import pickle
    user = {"account": "sunck", "passwd": "666"}
    with open("testdata/python_file_2.txt", "wb") as fp:
        pickle.dump(user, fp)

    with open("testdata/python_file_2.txt", "rb") as fp:
        user = pickle.load(fp)
    print(user, type(user))

if __name__ == '__main__':
    #basic_016_01()
    #basic_016_02()
    #basic_016_03()
    basic_016_04()