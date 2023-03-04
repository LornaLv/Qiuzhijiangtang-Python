# Date: 2023/3/3 上午10:10
'''
使用私有属性的场景
1、把特定的一个属性隐藏起来，不想让类的外部进行直接调用
2、我想保护这个属性，不想让属性的值随意的改变
3、保护这个属性，不想让派生类（子类）去继承
'''


class Person:
    def __init__(self):
        self.__name = '李四'  # 加两个下划线，将此属性私有化，私有化之后就不能在外部访问了，在类的内部是可以访问的
        self.age = 30

    def __str__(self):
        return f'{self.__name}的年龄是{self.age}'


class Student(Person):
    def printInfo(self):
        print(self.age)

    pass


xl = Person()
print(xl)
# print(xl.name)  # 是通过实例对象，在外部访问 不能访问私有属性
stu = Student()
print(stu)
print(stu.name)
