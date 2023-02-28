# Date: 2023/2/27 下午9:25
# 元组是一种不可变得的序列，用（）创建元组
print('-------------------------------')
t = ('abcd', 89, 9.13, 'peter', 'python', [11, 22, 33])
print(type(t))
print(t)

print('----------------元组的查询---------------')
for item in t:
    print(item, end=' ')
print('')
print(t[2:4])
print(t[::-1])
print(t[::-2])
print(t[-2:-1:])
print(t[-4:-1:])

print('----------------对元组中的可变列表进行修改---------------')
t[5][2] = 9999
print(t)

print('当元组中只有一个数据项的时候，必须要在数据项的最后加一个逗号')
t1 = (1,)
print(type(t1))
t2 = tuple(range(10))
print(type(t2))
print(t2.count(8)) #可以统计元素出现的次数
