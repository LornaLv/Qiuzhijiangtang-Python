# Date: 2023/3/2 下午3:22
'''
类方法：类对象所拥有的方法，需要用装饰器@classmethod来标识为类方法
       对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
       类方法可以通过类对象，实例对象调用
静态方法：类方法所拥有的方法，需要@staticmethod来表示静态方法，静态方法不需要任何参数
为什么要使用静态方法：由于静态方法主要用来存放逻辑性的代码，本身和类以及实例对象没有交互
也就是说，在静态方法中，不会涉及到类中方法和属性的操作
数据资源能够得到有效的充分利用
'''


class People:
    country = '中国'

    # 类方法，需要用classmethod修饰
    @classmethod
    def get_country(self):
        return self.country  # 访问类属性
        pass

    @classmethod
    def change_country(self):
        self.country = '中国中国中国'
        return self.country
        pass

    @staticmethod
    def getdata():
        return People.country
        pass


p = People()
print(f'通过类对象引用：{People.get_country()}')  # 通过类对象直接引用
print(f'通过实例对象访问：{p.get_country()}')
print(f'通过类方法修改类属性：{p.change_country()}')
print(f'通过类对象调用静态方法：{People.getdata()}')
print(f'通过实例对象调用静态方法：{p.getdata()}')

import time


class TimeTest:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())

    @staticmethod
    def Add(x, y):
        return x + y


print(TimeTest.showTime())
print(TimeTest.Add(10, 90))
