# Date: 2023/3/7 下午2:57
# tell返回指针当前所在的位置
# 对于中文来讲，每次读取到的一个汉字实际上占用了两个字符
with open('test.txt', 'r') as f:
    print(f.read(3))
    print(f.tell())
    print(f.read(2))
    print(f.tell())

# truncate可以对源文件进行截取操作
obj1 = open('test.txt', 'r')
print(obj1.read())
obj1.close()

print('----------截取之后的数据---------')
obj2 = open('test.txt', 'r+')
obj2.truncate(15)  # 保留前15个字符
print(obj2.read())
obj2.close()
