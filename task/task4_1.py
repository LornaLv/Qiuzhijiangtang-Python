# Date: 2023/2/28 上午10:37
'''
写函数，接收n个数字，求这些参数数字的和
'''


def sum(n):
    sum = 0
    for i in range(n):
        num = int(input(f'请输入第{i + 1}个数字:'))
        sum += num
    return sum


print('--------------方法一--------------')
n = int(input('请输入你要输入的数字的个数：'))
print(f'您输入的这{n}个数的和为：', sum(n))


def sumFunc(*args):
    result = 0
    for item in args:
        result += item
    return result


print('--------------方法二--------------')
rs = sumFunc(1, 2, 3, 4)
print(f'rs={rs}')
