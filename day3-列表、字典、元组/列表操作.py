# Date: 2023/2/27 下午8:45
# 可修改，用[]表示
print('-------------------------------')
lst = [1, 2, 3, '你好']
print('列表的长度（列表中的数据个数）：', len(lst))
print(type(lst))

print('-------------------------------')
list1 = ['abcd', 785, 12.23, 'qiuzhi', True]
print('输出完整的列表：', list1)
print('取第一个元素：', list1[0])
print('取第2-3个元素：', list1[1:3:1])
print('从第三个元素开始，到最后：', list1[2::])
print('倒序输出：', list1[::-1])
print('输出多次列表中的数据：', list1 * 3)

print('---------------插入----------------')
list1.append('xiaolv')
print(list1)
list1.append(['111', 2222])
print(list1)
list1.insert(1, 'ccc')
print(list1)
rsData = list(range(10))  # 强制转换为list对象
print(type(rsData))
list1.extend(rsData)  # 批量添加
print(list1)

print('---------------修改----------------')
print('修改之前：', lst)
lst[0] = 'Peter'
print('修改之后：', lst)

print('---------------删除----------------')
lst2 = list(range(1, 50))
print('修改之前：', lst2)
del lst2[5]
print('修改之后：', lst2)
del lst2[3:20:1]
print('批量删除：', lst2)
lst2.remove(26)
print('移除指定的元素：', lst2)
lst2.pop(3)
print('移除指定索引的元素：', lst2)
