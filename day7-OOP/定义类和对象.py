# Date: 2023/3/1 下午7:00
'''
类结构：类名、属性、方法
class 类名:
    属性
    方法
'''


class Person:
    # 人的特征
    name = '小明'
    age = 29

    # 人的行为
    def eat(self):
        print('大口吃饭')

    def run(self):
        print('飞快地跑')


person = Person()
person.eat()
person.run()
print(person.age)
