# Date: 2023/3/5 下午10:53
'''
创建一个类，并定义两个私有化属性，提供一个获取属性的方法，和设置属性的方法。
利用property属性给调用者提供属性方式的调用获取和设置私有属性方法的方式。
'''


class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self):
        name = input('请输入你的姓名：')
        self.__name = name

    def set_age(self, age):
        age = input('请输入你的年龄：')
        if 0 < self.__age < 120:
            self.__age = age
        else:
            print('年龄设置失败')

    def __str__(self):
        return f'{self.__name}的年龄是{self.__age}岁'


class Student:
    def __init__(self):
        self.__name = '张三'
        self.__score = 90

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @name.setter
    def score(self, score):
        self.__score = score

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        print(f'{self.__name}的得分是：{self.__score}')


xw = Student()
xw()
print(xw)
