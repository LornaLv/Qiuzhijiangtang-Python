# Date: 2023/3/1 下午8:37
class Person:
    def __init__(self, pro, name, food):
        self.pro = pro
        self.name = name
        self.food = food

    def __str__(self):
        return '%s喜欢吃%s %s修的专业是%s' % (self.name, self.food, self.name, self.pro)


p = Person('心理学', '小吕', '草莓')
print(p)
