# Date: 2023/2/27 下午6:27
print('-------------------------------')
test = 'Python'
print('第一个字符%s:' % (test[0]))
for item in test:
    print(item, end=' ')
print('')

print('-------------------------------')
name = 'peter'
print('首字母大写:', name.capitalize())  # 首字母大写

print('-------------------------------')
a = '   l      v      '
print('去除前后空格:', a.strip())  # 去除前后空格
print('去除左边空格:', a.lstrip())  # 去除左边空格
print('去除右边空格:', a.rstrip())  # 去除右边空格

print('-------------------------------')
dataStr = 'I love Python'
print('查找指定字符/字符串在序列中的位置：', dataStr.find('love'))
print('查找索引，返回的是下标值：', dataStr.index('v'))

print('-------------------------------')
print('字符串是否以n结尾：', dataStr.endswith('n'))
print('字符串是否以n开头：', dataStr.startswith('n'))

print('-------------------------------')
print('转换成大写：', dataStr.upper())
print('转换成小写：', dataStr.lower())

print('-------------------------------')
strMsg = 'hello world'
print(strMsg)
print(strMsg[0:5:1])  # 切片：左闭右开
print(strMsg[6::])
print(strMsg[::-1])
