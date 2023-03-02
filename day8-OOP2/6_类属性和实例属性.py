# Date: 2023/3/2 下午3:06
'''
类属性：就是类对象所拥有的属性，它被所有类对象的实例对象所共有，类对象和实例对象可以访问
实例属性：实例对象所拥有的属性，只能通过实例对象访问
'''


class Student:
    name = '小明'  # 属于类属性，就是student类对象所拥有的

    def __init__(self, age):
        self.age = age  # 实例属性


Student.name = 'lsl'
lm = Student(18)
xl = Student(23)
lm.name = '刘德华'
print(f'lm的姓名：{lm.name},lm的年龄：{lm.age}')
print(f'xl的姓名：{xl.name},lm的年龄：{xl.age}')

print('--------通过类对象去访问name---------')
print(Student.name)  # 类名.属性名 的形式

'''
小结：
类属性是可以被类对象和实例对象共同访问使用的
实例属性只能由实例对象所访问
'''
