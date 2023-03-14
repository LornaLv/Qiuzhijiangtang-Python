# Date: 2023/3/14 下午7:04
import re

data = '我是中国人，我爱中国，我很骄傲，I love China'
res = re.findall('我.', data)
print(res)

search = re.search('我.', data)
print(search.group())

reobj=re.compile('我.')
print(reobj.search(data))
print(reobj.findall(data))