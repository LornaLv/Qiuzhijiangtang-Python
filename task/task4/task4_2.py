# Date: 2023/2/28 上午11:19
'''
写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
'''


def odd(con):
    newlist = con[::2]
    return newlist


con = list(input('请输入你想传入的列表：').split(','))
print(con)
print(odd(con))
