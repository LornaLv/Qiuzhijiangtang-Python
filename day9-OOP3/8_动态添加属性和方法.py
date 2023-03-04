# Date: 2023/3/4 下午8:21
import types


def dynamicMethod(self):
    print(f'{self.name}的身高是{self.height},在{self.school}上大学')


@classmethod
def classTest(cls):
    print('这是一个类方法')
@staticmethod
def staticMethod():
    print('这是一个静态方法')

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}今年{self.age}岁了'


print('---------绑定类方法--------')
Student.TestMethod = classTest
Student.TestMethod()
print('----------绑定类方法执行结束----------\n')
print('---------绑定静态方法--------')
Student.staticMethod = staticMethod
Student.staticMethod()
print('----------绑定静态方法执行结束----------\n')

lsl = Student('六十六', 18)
lsl.height = 180  # 动态添加
lsl.printInfo = types.MethodType(dynamicMethod, lsl)  # 动态的绑定方法
print('---------给类对象添加属性---------')
Student.school = '上海大学'
print(lsl.school)
print('\n---------动态的添加实例方法---------')
lsl.printInfo()
# print(lsl)
# print(lsl.height)
print('\n-----------另外一个实例对象，xl-------------')
xl = Student('六十六', 18)
print(xl)
# print(xl.height)
