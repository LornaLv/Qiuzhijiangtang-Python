# Date: 2023/3/14 上午9:08
# 通过python中的re模块学习并使用正则表达式的基本知识点
import re

data = 'Python is the best language in the world'
result = re.match('P', data)  # 精确匹配
print(result.group())
