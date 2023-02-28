# Date: 2023/2/27 下午9:37
# 字典是由键值对组成的集合，通常采用键来进行数据访问
# 可修改，用{}表示，键必须是不可变得（元组，字符串），每个键是唯一的
print('-------------------------------')
d = {}  # 空字典
print(type(d))
d['name'] = 'lv'  # key:value
d['pos'] = 'student'
d['age'] = 18
print(d)

d1 = {'name': 'cheng', 'age': 19, 'pos': 'student'}
print(d1)
print(len(d1))

print('---------------查找----------------')
print(d['name'])  # 通过 键key 获取对应的 值value
print(d.keys())  # 获取所有的键
print(d.values())  # 获取所有的值
print(d.items())  # 获取所有的键值对
for item in d:
    print(item, end=' ')
for key, value in d.items():
    print('key:', key, end=' ')
    print('value:', value, end=' ')
    print('')

print('---------------修改----------------')
d['name'] = 'xiaolv'
print(d)
d.update({'age': 23, 'height': 1.8})
print(d)

print('---------------删除----------------')
del d['name']
print(d)
d.pop('age')
print(d)

print('---------------排序----------------')
d1 = {'math': 90, 'English': 89, 'Python': 100, 'Java': 99}
print(sorted(d1.items(), key=lambda d1: d1[0]))  # 按照key排序
print(sorted(d1.items(), key=lambda d1: d1[1]))  # 按照value排序
