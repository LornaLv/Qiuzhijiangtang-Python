# Date: 2023/3/14 下午4:28
import re

# ^：匹配字符串开头
result1 = re.match('^p.*', 'python is the best language')
print(result1.group())
result2 = re.match('^p\w{5}', 'python is the best language')
print(result2.group())

# $：匹配字符串结尾
result3 = re.match('\w{5,15}@163.com$', 'admin123@163.com')
print(result3.group())
