# Date: 2023/3/14 下午6:53
import re

data = '我爱伟大的祖国，I love China，中国是一个伟大的国家'
res = re.search('China', data)
print(res)
print(res.group())
print(data[22])
