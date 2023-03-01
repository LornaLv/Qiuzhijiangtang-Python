# Date: 2023/2/28 下午6:44
# Python中使用lambda关键字创造匿名函数，所谓匿名即这个函数没有名字不用def关键字创建标准的函数
'''
lambda 参数1、参数2、参数3：表达式
特点：
（1）使用lambda关键字去创建函数
（2）没有名字的函数
（3）匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是语句
（4）匿名函数自带return，而这个return点结果就是表达式计算后的结果
'''


def computer(x, y):
    return x + y


print(computer(1, 3))

print('-----------对应的匿名函数-----------')
m = lambda x, y: x + y
# 通过变量去调用匿名函数
print(m(32, 89))

m1 = lambda a, b, c: a * b * c
print(m1(1, 8, 45))

print('-----------lambda与三元运算-----------')
age = 18
print('可以参军' if age > 18 else '继续上学')
panduan = (lambda x, y: x if x > y else y)(19, 90)  #直接的调用
print(panduan)
# print(panduan(89, 38))
