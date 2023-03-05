# Date: 2023/3/5 下午10:54
'''
创建一个Animal类，实例化一个cat对象
请给cat对象动态绑定一个run方法
给类绑定一个类属性colour
给类绑定一个类方法打印字符串’OK‘
'''
import types


class Animal:
    pass


def run(self):
    print('跑跑跑')


@classmethod
def printInfo(cls):
    print('OK')


cat = Animal()
cat.run = types.MethodType(run, cat)  # 动态绑定run方法
cat.run()

Animal.colour = '黑色'  # 给类绑定一个类属性colour
print(cat.colour)

Animal.printInfo = printInfo  # 给类绑定一个类方法打印字符串’OK‘
Animal.printInfo()
