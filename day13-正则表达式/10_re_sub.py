# Date: 2023/3/14 下午7:14
# re.sub实现目标的搜索和查找
# re.subn实现目标的搜索和查找,并以元组形式返回被替换的数量
import re

data = 'Python是很受欢迎的语言python python python 你最好'
pattern = '[a-zA-Z]+'  # 字符集的范围   +代表前导字符模式出现1次以上
res = re.sub(pattern, 'java', data)
print(res)
resn = re.subn(pattern, 'java', data)
print(resn)