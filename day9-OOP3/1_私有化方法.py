# Date: 2023/3/4 下午2:01
# 方法私有化，只需在方法前加__
class Animal:
    def __eat(self):
        print('吃东西')

    def run(self):
        self.__eat()  # 在此调用私有化的方法
        print('飞快地跑')


class Bird(Animal):
    pass


b = Bird()
# b.eat()
b.run()
