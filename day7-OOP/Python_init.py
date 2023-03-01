# Date: 2023/3/1 下午7:58
class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self,food):
        print(self.name + '喜欢吃'+food)


xq = People('小齐', 27, '男')
xq.eat('香蕉和苹果')
print(xq.name, xq.gender, xq.age)

'''
xl = People()
xl.eat()
xl.gender = '女'
xl.age = 20
xl.name = '小丽'
'''
