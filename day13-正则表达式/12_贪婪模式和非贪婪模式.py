# Date: 2023/3/14 下午7:23
# 贪婪模式：默认的匹配规则，在满足条件的情况下尽可能多的匹配到数据
import re

print('------贪婪模式------')
res = re.match('\d{6,9}', '23432432')
print(res.group())

print('------非贪婪模式------')
res = re.match('\d{6,9}?', '23432432')
print(res.group())

print('---------------------')
content = 'aacbacbc'
pattern = re.compile('a.*b')
result = pattern.search(content)
print('贪婪模式：', result.group())

pattern1 = re.compile('a.*?b')
result1 = pattern1.search(content)
print('非贪婪模式：', result1.group())
