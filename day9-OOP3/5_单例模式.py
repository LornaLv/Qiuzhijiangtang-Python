# Date: 2023/3/4 下午3:06
'''
单例模式是一种常用的软件设计模式    目的：确保某一个类只有一个实例存在
如果希望在某个系统中，某个类只能出现一个实例的时候，那么这个单例对象就满足要求
'''


# 创建一个单例对象，基于__new__去实现的（推荐的一种）
class Databaseclass(object):
    def __new__(cls, *args, **kwargs):
        # cls.instance=cls.__new__(cls) 不能使用自身的new方法，容易造成一个深度递归，应该调用父类的new方法
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


db1 = Databaseclass()
db2 = Databaseclass()
print(db1, id(db1))
print(db2, id(db2))
