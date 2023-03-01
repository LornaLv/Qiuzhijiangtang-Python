# Date: 2023/3/1 下午12:27
# set 不支持索引和切片，是一个无序且不重复的容器
# 类似于字典 但是只有键，没有value
# 创建集合
dict1 = {}
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(type(set1))
print(type(dict1))

print('--------添加元素：add--------')
set1.add('python')
print(set1)

print('--------清空元素：clear--------')
set1.clear()
print(set1)

print('--------两个集合的差集：difference--------')
set1 = {2, 3, 4, 5, 6}
print(set1.difference(set2))
print(set1 - set2)

print('--------两个集合的交集：intersection--------')
print(set1.intersection(set2))
print(set1 & set2)

print('--------两个集合的并集：union--------')
print(set1.union(set2))
print(set1 | set2)

print('--------移除元素：pop--------')
print(set1.pop())
print(set1)

print('--------移除指定数据：discard--------')
print(set1.discard(3))
print(set1)

print('--------更新数据：update--------')
print(set1.update(set2))
print(set1)
