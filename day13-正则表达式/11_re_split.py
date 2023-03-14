# Date: 2023/3/14 下午7:20
import re

data = '百度，腾讯，阿里，华为'
rs = re.split(',', data)
print(type(rs))
print(rs)
