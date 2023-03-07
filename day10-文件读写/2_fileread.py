# Date: 2023/3/6 下午10:20
# 读数据操作
f = open('test.txt', 'r')
print(f.read(10))
# print(f.read())  # read 从头读到尾
print(f.readline())
print(f.readline())  # readline读一行数据
print(f.readlines())  # 按行读取
f.close()
print('---------------------')

# with的使用
# 优点：自动释放打开关联的对象
with open('test1.txt', 'r') as f:
    print(f.read())

# 小结
'''
文件读写的几种操作方式:
read：r  r+  rb  rb+
      r  r+：只读，使用普通读取场景
      rb  rb+：适用于文件、图片、视频、音频，这样的文件读取
write：w    w+   wb+    wb   a   ab
      w   wb+   w+：每次都会创建文件
      二进制读写的时候要注意编码问题，默认情况下写入文件的编码是GBK
      a    ab   a+：在原有文件的基础之上【文件指针的末尾】去追加，并不会每次都去创建新的文件
'''
