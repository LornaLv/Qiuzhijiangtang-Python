# Date: 2023/3/15 上午11:48
# 请使用正则将文本中的s替换成S，请写Python代码完成匹配替换
import re

str = 'Save your heart for someone who cares'
res = re.subn('s', 'S', str)
print(res)
