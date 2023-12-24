# Python 对目录的操作
'''
递归遍历目录
'''
def basic_017_01():
    # 返回所有文件的绝对路径
    def traverseDir(dirPath):
        absPathList = []
        import os

        filesList = os.listdir(dirPath)
        for fileName in filesList:
            absPath = os.path.join(dirPath, fileName)
            if os.path.isdir(absPath):
                # 目录
                absPathList += traverseDir(absPath)
            else:
                # 文件
                # print(absPath)
                absPathList.append(absPath)
        return absPathList

    absPathList = traverseDir(r"../../")
    print(absPathList)
    print(len(absPathList))
    # for absPath in absPathList:
    #     print(absPath)

'''
栈模拟递归遍历目录
'''
def basic_016_02():
    def traverseDir(dirPath):
        import os
        absPathList = []
        myStack = []
        myStack.append(dirPath)

        while len(myStack) != 0:
            path = myStack.pop()

            fileList = os.listdir(path)
            for fileName in fileList:
                absPath = os.path.join(path, fileName)
                if os.path.isdir(absPath):
                    myStack.append(absPath)
                else:
                    absPathList.append(absPath)
        return absPathList

    absPathList = traverseDir(r"../../")
    print(absPathList)
    print(len(absPathList))


'''
队列模拟递归遍历目录
'''
def basic_016_03():
    def traverseDir(dirPath):
        import os
        from collections import deque
        absPathList = []

        q = deque([])
        q.append(dirPath)

        while len(q) != 0:
            path = q.popleft()

            fileList = os.listdir(path)
            for fileName in fileList:
                absPath = os.path.join(path, fileName)
                if os.path.isdir(absPath):
                    q.append(absPath)
                else:
                    absPathList.append(absPath)
                    # yield absPath
        return absPathList

    absPathList = traverseDir(r"../../")
    print(absPathList)
    print(len(absPathList))

if __name__ == '__main__':
    basic_017_01()
    #basic_017_02()
    #basic_017_03()