# Date: 2023/3/2 上午10:50
class Animal:
    def eat(self):
        print('大口吃')

    def drink(self):
        print('大口喝')


class Dog(Animal):
    def wwj(self):
        print('小狗汪汪叫')


class Cat(Animal):
    def mmj(self):
        print('小猫喵喵叫')


d = Dog()
d.wwj()
d.drink()
d.eat()
c = Cat()
