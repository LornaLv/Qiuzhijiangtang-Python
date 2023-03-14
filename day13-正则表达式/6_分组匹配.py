# Date: 2023/3/14 下午4:56
import re

# |：匹配左右任意一个表达式
print('1、---------|：匹配左右任意一个表达式')
string = 'wywsqhdfdk888'
rs1 = re.match('(wywsqhdfdk88|wywsqhdfdk888)', string)
print(rs1.group())

# (ab)：将括号中字符作为一个分组
print('2、---------(ab)：将括号中字符作为一个分组')
# 匹配电话号码 xxxx-123456789
rs2 = re.match('([0-9]*)-(\d*)', '0355-234567891')
print(rs2.group())
print(rs2.group(0))
print(rs2.group(1))
print(rs2.group(2))

# \num：引用分组num匹配到的字符串
# html的标签都是成对出现的，这样匹配规则html就可以引用组来实现，避免重复写
print('3、---------\\num：引用分组num匹配到的字符串')
htmlTag = '<html><h1>测试数据</h1></html>'
res3 = re.match(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag)
print(res3.group())
print(res3.group(0))
print(res3.group(1))
print(res3.group(2))
print(res3.group(3))

# (?P<名字>)：分组起别名.
# (?P=name)：引用别名为name分组匹配到的字符串
print('4、---------(?P)：分组起别名')
print('5、---------(?P=name)：引用别名为name分组匹配到的字符串')
htmlTag1 = '<div><h1>www.baidu.com</h1></div>'
res4 = re.match(r'<(?P<div>\w*)><(?P<h1>\w*)>.*</(?P=h1)></(?P=div)>', htmlTag1)
print(res4.group())
print(res4.group(0))
print(res4.group(1))
print(res4.group(2))
