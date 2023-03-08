# Date: 2023/3/1 下午3:07
# 指定一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个’独一无二‘的数字

print('------第一种方法：固定输入-------')
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 0, 0, 1, 2, 3, 5, 6, 6]
print(l)
list1 = []  # 存储l中所有元素去除一次后剩下的所有元素
list2 = []  # 存储l中出现过的所有元素

for item in l:
    if item not in list2:
        list2.append(item)
    else:
        list1.append(item)

set2 = set(list2)
set1 = set(list1)
print('列表中独一无二的数字为：', set2 - set1)

print('-------第二种方法：自定义输入---------')


def find():
    lst = []  # 存储输入的所有数字的列表
    l = input('请输入您要输入的所有数字，其中只有一个元素出现过一次（每个数字以空格分隔）：')
    lst = l.split(' ')
    # print(lst)

    list1 = []  # 存储l中所有元素去除一次后剩下的所有元素
    list2 = []  # 存储l中出现过的所有元素

    for item in lst:
        if int(item) not in list2:
            list2.append(int(item))
        else:
            list1.append(int(item))
    set2 = set(list2)
    set1 = set(list1)
    # print(set2)
    # print(set1)
    print('您所给出的列表中独一无二的数字为：', set2 - set1)


find()
