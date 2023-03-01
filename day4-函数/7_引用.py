# Date: 2023/2/28 下午6:13
a = 1


def func(x):
    print('x的地址：', id(x))
    pass


# 调用函数
print('a的地址：', id(a))
func(a)
