# Date: 2023/3/1 下午10:55
# Task1：Python中如何通过类创建对象，请用代码举例说明
# Task2：如何在类中定义一个函数方法，请用代码举例说明
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(f'{self.name}的年龄是{self.age}')


p = Person('xiaolv', 21)
p.printInfo()
