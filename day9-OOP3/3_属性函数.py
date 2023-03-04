# Date: 2023/3/4 下午2:25
class Person(object):
    def __init__(self):
        self.age = 18

    # 实现方式2：通过装饰器的方式去声明
    @property  # 用装饰器修饰，添加属性标识，提供一个getter方法
    def age(self):
        return self.__age

    @age.setter  # 使用装饰器进行装饰，提供一个setter方法
    def age(self, parms):
        if parms < 0:
            print('年龄不能小于0')
        else:
            self.__age = parms


'''
    def get_age(self):
        return self.__age

    def set_age(self, age):

        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age

    # 定义一个类属性，实现通过直接访问属性的形式去访问私有的属性
    age = property(get_age, set_age)
'''

p1 = Person()
print(p1.age)
p1.age = 90
print(p1.age)
