# Date: 2023/3/4 下午3:29
# except 在捕获错误异常的时候 只要根据具体的错误类型来捕获的
# 用一个块 可以捕获多个不同类型的异常
# Exception 可以捕获所有的异常，当对出现的问题或者错误不确定的情况下，可以使用Exception
print('-------try...except语句-------')
try:
    # print(b)
    li = [12, 2, 3]
    print(li[6])
except NameError as msg:
    # 捕获到错误，才执行except的内容
    print(msg)
except IndexError as msg:
    print(msg)
else:
    print('当Try里面的代码，没有出现异常的情况下，我才会执行')

print('人生苦短，我学Python')


def A(s):
    return 10 / int(s)


def B(s):
    return A(s) * 2


def main():
    try:
        A('0')
    except Exception as msg:
        print(msg)


try:
    int('avb')
except Exception as msg:
    print(msg)
    pass
finally:
    print('会释放文件的资源，数据库连接是资源等等')
    print('不管有没有出错都执行的代码块')
