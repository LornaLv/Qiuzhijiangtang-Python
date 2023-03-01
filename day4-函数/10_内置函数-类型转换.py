# Date: 2023/3/1 上午10:54
print('转换二进制：', bin(10))
print('转换十六进制：', hex(89))

t = (1, 2, 3, 4)
print('元组t:', t, '\t', type(t))
print('元组转列表：', list(t), '\t', type(list(t)))

# 字典操作
d = dict()
print(type(d))
d['name'] = 'xiaoming'
d['age'] = 18
print(d)

# bytes转换
print(bytes('我喜欢Python', encoding='utf-8'))
