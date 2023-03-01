# Date: 2023/3/1 上午11:14
print('--------------all()----------------')
print(all([None]))
print(all(()))
print(all([1, 2, 3, False]))
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

print('--------------any()----------------')
print(any([]))
print(any(()))
print(any([1, 2, 3, False]))
print(any([1, 2, 3]))
print(any([1, 2, 3, 0]))

print('--------------sorted()/sort()----------------')
l = [2, 543, 231, 435, 25, 79, 34]
l.sort()
print(l)
l1 = [2, 543, 231, 435, 25, 79, 34]
print(sorted(l1, reverse=True))  # sorted返回一个新的列表

print('--------------zip()----------------')
# 用来打包的
s1 = ['a', 'b', 'c']
s2 = ['你', '我', '他']
print(list(zip(s1)))
ziplist = zip(s1, s2)  # 会把序列中对应的索引位置的元素存储为一个元组
print(list(ziplist))

print('--------------enumerate()----------------')
listobj = ['a', 'b', 'c']
for index, item in enumerate(listobj, 5):  # 可以自由定义下标值
    print(index, item)
dictobj={}
dictobj['name']='lv'
dictobj['age']='21'
dictobj['pos']='student'
print(dictobj)
for item in enumerate(dictobj):
    print(item)

print('--------------zip()----------------')


def printBookInfo():
    books = []  # 存储所有的图书信息
    id = input('请输入编号,每个项以空格分割:')
    Bookname = input('请输入书名,每个项以空格分割:')
    Bookpos = input('请输入位置,每个项以空格分割:')
    author = input('请输入作者,每个项以空格分割:')
    idlist = id.split(' ')
    booknamelist = Bookname.split(' ')
    bookposlist = Bookpos.split(' ')
    authorlist = author.split(' ')
    bookInfo = zip(idlist, booknamelist, bookposlist, authorlist)  # 打包处理
    for bookItem in bookInfo:
        '''遍历图书信息，进行存储'''
        dictInfo = {'编号': bookItem[0], '书名': bookItem[1], '所在书架位置': bookItem[2], '作者': bookItem[3]}
        books.append(dictInfo)
    for item in books:
        print(item)


printBookInfo()
