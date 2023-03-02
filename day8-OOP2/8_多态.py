# Date: 2023/3/2 下午3:01
'''
多态：顾名思义就是多种状态、形态，就是同一种行为对于不同的子类【对象】有不同的行为表现
要想实现多态，必须有两个前提需要:
(1)继承：多态必须发生在父类和子类之间
(2)重写：子类重写父类的方法
'''


class Animal(object):
    def say_who(self):
        print('我是一个动物')


class Duck(Animal):
    def say_who(self):
        print('我是一只漂亮的鸭子')


class Dog(Animal):
    def say_who(self):
        print('我是一只哈巴狗')


class Cat(Animal):
    def say_who(self):
        print('我是一只小猫咪')


class Bird(Animal):
    def say_who(self):
        print('我是一只黄鹂鸟')


def commonInvoke(obj):
    obj.say_who()


listObj = [Duck(), Dog(), Cat(), Bird()]
for item in listObj:
    commonInvoke(item)

'''
duck = Duck()
duck.say_who()
dog = Dog()
dog.say_who()
cat = Cat()
cat.say_who()
'''
