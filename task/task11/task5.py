# Date: 2023/3/8 下午1:59
'''
有两个磁盘文件A和B，各存放一行字母，要求把这两个文件中的信息合并（按字母顺序），输出到一个新文件C中
'''
# with open('./File/A.txt', 'r') as fa:
#     print(fa.read())
#
# with open('./File/B.txt', 'r') as fb:
#     print(fb.read())

fa = open('./File/A.txt', 'r')
print(fa.read())
fb = open('./File/B.txt', 'r')
print(fb.read())


# with open('./File/C.txt', 'w') as f:
#     content1 = fa.read()
#     f.write(content1)
    # content2 = fb.read()
    # f.write(content2)