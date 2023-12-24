# Python 对linux系统操作
'''
os中常用属性和方法
(1)作用
    包含了基本的操作系统功能，提供了非常丰富的方法用来处理文件和目录
(2)
    1）属性
    名称	说明
    name	操作系统的类型，nt表示windows，posix表示Linux、Unix
    uname	获取操作系统的信息，linux、Unix下使用
    environ	获取系统中的环境变量，environ.get()可以获取环境变量的值
    curdir	返回当前的目录
    2）方法
    名称	说明
    getcwd()	返回当前工作目录的绝对路径
    listdir()	返回指定目录下的所有文件和目录
    mkdir()	创建指定目录，注意目录已经存在时会报错，目录路径中存在不存在的层级时报错
    rmdir()	删除目录，注意目录不存在则报错
    rename()	重命名
    stat()	获取文件属性
    remove()	删除普通文件
    system()	运行shell命令
'''
def basic_018_01():
    import os

    # 操作系统的类型
    # nt     windows
    # posix  Linux、Unix
    print(os.name)
    # 获取操作系统的信息，linux、Unix下使用
    print(os.uname())
    # 获取系统中的环境变量
    print(os.environ)
    # 获取指定环境变量的值
    print(os.environ.get("PATH"))

    # 返回当前的目录
    print(os.curdir)

    # 返回当前工作目录的绝对路径
    print(os.getcwd())

    # 返回指定目录下的所有文件和目录
    print(os.listdir(r"testdata"))

    # 创建指定目录，注意目录已经存在时会报错，目录路径中存在不存在的层级时报错
    os.mkdir(r"testdata/temp")
    os.mkdir(r"testdata/temp/a/b")

    # 删除目录，注意目录不存在则报错
    #os.rmdir(r"testdata\temp\a\b")

    # 重命名
    #os.rename(r"testdata\python_file_1.txt", r"testdata\python_file_1-1.txt")

    # 获取文件属性
    print(os.stat(r"testdata/python_file_2.txt"))

    # 删除普通文件
    #os.remove(r"testdata\python_file_1.txt")

    # 运行shell命令
    #os.system("notepad")
    #os.system("shutdown -s -t 10")
    #os.system("shutdown -a")
    os.system("ls")


'''
os.path中常用方法
操作文件和目的函数一部分在os模块中，还有一部分在os.path中

名称	说明
abspath	返回指定路径的绝对路径
join	拼接路径（不论是否存在）
split	拆分路径（不论是否存在）
splitdrive	以路径第一个’/'为分隔，分隔驱动器名与路径
splitext	获取文件的扩展名（不论是否存在）
basename	获取目录或文件名（不论是否存在）
getsize	获取属性
getctime	获取属性
isdir	判断是否是目录
isfile	判断是否是文件
exists	判断目录和文件是否存在
isabs	判断是否是绝对路径（不论是否存在）
'''
def basic_018_02():
    import os

    # 返回指定路径的绝对路径
    print(os.path.abspath("."))

    # 拼接路径（不论是否存在）
    print(os.path.join(r"testdata/temp", "a.txt"))

    # 拆分路径（不论是否存在）
    print(os.path.split(r"testdata/temp"))
    print(os.path.split(r"testdata/python_file_2.txt"))
    # 以路径第一个'/'为分隔，分隔驱动器名与路径
    print(os.path.splitdrive(r"/usr/local"))
    print(os.path.splitdrive(r"/usr/local/sunck.txt"))
    # 获取文件的扩展名（不论是否存在）
    print(os.path.splitext(r"testdata/python_file_2.txt"))
    print(os.path.splitext(r"testdata/python_file_2"))

    # 获取目录名（不论是否存在）
    print(os.path.basename(r"usr/local"))
    # 获取文件名（不论是否存在）
    print(os.path.basename(r"testdata/python_file_2.txt"))

    # 获取属性
    print(os.path.getsize(r"testdata/python_file_2.txt"))
    print(os.path.getctime(r"testdata/python_file_2.txt"))

    # 判断是否是目录
    print(os.path.isdir(r"testdata/temp"))
    print(os.path.isdir(r"testdata/python_file_2.txt"))

    # 判断是否是文件
    print(os.path.isfile(r"testdata/temp"))
    print(os.path.isfile(r"testdata/python_file_2.txt"))

    # 判断目录和文件是否存在
    print(os.path.exists(r"testdata/temp"))
    print(os.path.exists(r"testdata/python_file_2.txt"))


    # 判断是否是绝对路径（不论是否存在）
    print(os.path.isabs(r"./testdata/temp"))
    print(os.path.isabs(r"/usr/local"))


if __name__ == '__main__':
    basic_018_01()
    basic_018_02()