# Date: 2023/3/2 下午12:09
class Grandfather:
    def eat(self):
        print('吃')


class Father(Grandfather):
    def eat(self):
        print('爸爸经常吃海鲜')


class Son(Father):
    pass


s = Son()
print(Son.__mro__)
s.eat()
