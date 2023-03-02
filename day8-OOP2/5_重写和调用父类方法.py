# Date: 2023/3/2 下午1:53
# 为什么要重写，父类的方法已经不满足子类的需要，那么子类就可以重写父类或者完善父类的方法

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('汪汪叫')


class kejiquan(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, color)
        super().__init__(name, color)  # super是自动找到父类，进而调用方法
        self.height = 30
        self.weight = 5
        pass

    def bark(self):  # 属于重写父类的方法
        super().bark()
        print(f'{self.name}叫的跟神一样')

    def __str__(self):
        return f'{self.name}的身高为{self.height}cm，体重为{self.weight}kg'


kj1 = kejiquan('柯基', 'yellow')
kj1.bark()
print(kj1)
