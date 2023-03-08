# Date: 2023/3/1 下午10:56
'''
定义一个Animal类：
    （1）用__init__初始化方法为对象添加初始属性，如颜色、名字、年龄
    （2）定义动物方法，如run、eat等方法。如调用eat方法时打印xx在吃东西就可以
    （3）定义一个函数__str__方法，输出对象的所有属性
'''


class Animal:
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name}在跑')

    def eat(self):
        print(f'{self.name}在吃东西')

    def __str__(self):
        return f'{self.name}的颜色是{self.color},他今年{self.age}岁了'


cat = Animal('橘色', '咪咪', 3)
cat.run()
cat.eat()
print(cat)
