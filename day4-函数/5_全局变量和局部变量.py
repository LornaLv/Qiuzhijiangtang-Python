# Date: 2023/2/28 下午5:47

name = 'xiaolv'


def printInfo():
    name = 'Peter'
    print(name)


def TestMethod():
    # print(name)
    pass


def changeGlobal():
    # 在函数内部要想对全局变量修改，使用global声明
    global name
    name = 'lvlv'


printInfo()
changeGlobal()
print(name)
