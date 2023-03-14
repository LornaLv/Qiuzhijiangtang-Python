# Date: 2023/3/14 上午10:19
import re

# （1）.点的使用,匹配规则是除了换行符之外的字符
print('------------.点的使用------------')
data = 'aaaaa'
res1 = re.match('..', data)
print(res1.group())
res2 = re.match('...', data)
print(res2.group())
res3 = re.match('....', data)
print(res3.group())

print('------------------------')
pattern = '小.'
names = '李达', '小明', '小丽', '小吴'
for name in names:
    res = re.match(pattern, name)
    if res:
        print(res.group())

# （2）[]的使用,匹配规则是匹配中括号中的任意一个字符
print('------------[]的使用------------')
str1 = 'hello'
res4 = re.match('[eh]', str1)
print(res4.group())

pattern1 = '[abc]'  # 使用中括号括起来的内容，代表一个集合，代表匹配集合内的任意一个字符，[abc]代表可以匹配 a b c
data1 = 'a', 'b', 'c', 'e', 'wyw'
for data in data1:
    result = re.match(pattern1, data)
    if result:
        print('匹配成功%s' % result.group())

print('------------------------')
pattern2 = '[a-z]'  # 可以简写一个范围
data2 = 'a', 'b', 'c', 'e', 'wyw'
for data in data2:
    result = re.match(pattern2, data)
    if result:
        print('匹配成功%s' % result.group())

# （3）\d，匹配一个数字，即0-9
print('-----------\d，匹配一个数字，即0-9-------------')
data3 = '12345abcdef'
print(re.match('\d\d\d\d', data3).group())

# （4）\D，匹配非数字，即不是数字
print('-----------\D，匹配非数字，即不是数-------------')
data4 = 'w12345abcdef'
print(re.match('\D', data4).group())

# (5) \s：匹配空白，即空格，tab键
print('-----------\s：匹配空白，即空格，tab键-------------')
data5 = '   w12345abcdef'
print(re.match('\s', data5).group())

# (6) \S：匹配非空白，除空格，tab键之类的
print('-----------\S：匹配非空白，除空格，tab键之类的-------------')
data6 = 'dsgvfdxw12345abcdef'
print(re.match('\S', data6).group())

# (7) \w：匹配单词字符，即a-z、A-Z、0-9、_
print('-----------\w：匹配单词字符，即a-z、A-Z、0-9、_-------------')
data7 = 'w0912345abcdef'
print(re.match('\w\w\w\w\w\w\w', data7).group())

# (8) \W：匹配非单词字符
print('-----------\W：匹配非单词字符-------------')
data8 = '   w12345abcdef'
print(re.match('\W\W\W\W', data8).group())
