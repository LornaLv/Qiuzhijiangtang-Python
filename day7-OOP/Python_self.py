# Date: 2023/3/1 下午8:13
class Person:
    def __init__(self, pro):
        self.pro = pro

    def eat(self, name, food):
        self.name=name
        self.food=food
        # print('self=%s'%id(self))
        print('%s喜欢吃%s %s修的专业是%s' % (name, food,name,self.pro))


p = Person('心理学')
# print('p = %s'%id(p))
p.eat('小吕', '草莓')
