# Date: 2023/3/5 下午3:10
# 作用：限制要添加的实例属性，可以节约内存空间
class Student(object):
    __slots__ = ('name', 'age', 'score')

    def __str__(self):
        return f'{self.name}的年龄是{self.age}'


xw = Student()
xw.name = '小王'
xw.age = 18
xw.score = 90  # 没有在范围内，所以报错
# print(xw.__dict__)  # 所有可以用的属性都在这里存储，不足的地方就是占用的内存空间大
print(xw.__slots__)  # 在定义了slots变量之后，Student类的实例已经不能再随便创建不在__slots__定义的属性了
print(xw)
