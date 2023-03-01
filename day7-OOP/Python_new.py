# Date: 2023/3/1 下午8:41
class Person:
    def __init__(self, pro, name, food):
        self.pro = pro
        self.name = name
        self.food = food
        print('-----init函数的执行-----')

    def __str__(self):
        return '%s喜欢吃%s %s修的专业是%s' % (self.name, self.food, self.name, self.pro)

    def __new__(cls, *args, **kwargs):
        # 创建对象实例的方法，每调用一次，就会生成一个新的对象cls
        # 场景：可以控制创建对象的一些属性限定，经常用来做单例模式的时候来使用
        print('-----new函数的执行-----')
        return object.__new__(cls)  # 在这里是真正创建对象实例的


p = Person('心理学', '小吕', '草莓')
print(p)


'''
__new__和__init__函数的区别：
__new__：类的实例化方法，必须要返回该实例，否则对象就创建不成功
         至少有一个参数，cls，代表要实例化的类，此参数在实例化时，由Python解释器自动提供
         __new__函数执行早于__init__
__init__：用来做数据属性的初始化工作，也可以认为是实例的构造方法，接受类的实例 self 并对其进行构造
'''
