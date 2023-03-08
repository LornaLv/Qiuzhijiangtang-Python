# Date: 2023/3/5 下午10:51
'''
编写一段代码完成下面要求：
定义一个Person类，类中要有初始化方法，方法中要有人的姓名、年龄两个私有属性
提供获取用户信息的函数
提供获取私有属性的方法
提供可以设置私有属性的方法
设置年龄段范围在（0-120）的方法，如果不在这个范围，不能设置成功
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
