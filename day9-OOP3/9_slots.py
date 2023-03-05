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


# 当子类未声明__slots__时，那么是不会继父类的__slots__，此时子类是可以随意的属性赋值的
# 子类声明__slots__的情况下，继承父类的__slots__，也就是子类的__slots__范围是为其自身+父类的__slots__
class subStudent(Student):
    pass


ln = subStudent()
ln.gender = '女'
print(ln.gender)
