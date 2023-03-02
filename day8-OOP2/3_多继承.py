# Date: 2023/3/2 上午10:58
class shenxian:
    def fly(self):
        print('神仙都会飞')


class Monkey:
    def eat(self):
        print('猴子喜欢吃桃子')


class Sunwukong(shenxian, Monkey):
    pass


s = Sunwukong()
s.eat()
s.fly()


# 当多个父类中存在相同方法的时候，应该调用哪一个
class D(object):
    def eat(self):
        print('D.eat')


class C(D):
    def eat(self):
        super(C, self).eat()
        print('C.eat')


class B(D):
    pass


class A(B, C):
    pass


a = A()
a.eat()
print(A.__mro__)  # 可以显示类的依次继承关系
