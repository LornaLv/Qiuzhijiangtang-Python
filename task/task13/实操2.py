# Date: 2023/3/15 上午11:54
'''
<span>
    三生三世，十里桃花
</span>
<span>
    九州海上牧云记
</span>
<span>
    莫斯科行动
</span>
请使用正则将<span>标签中的全部内容匹配出来
'''
import re

Tag = '<span>三生三世，十里桃花</span><span>九州海上牧云记</span><span>莫斯科行动</span>'
res = re.match(r'<(.+)>(.+)<(/\1)><(.+)>(.+)<(/\1)><(.+)>(.+)<(/\1)>', Tag)
print(res.group())
print(res.group(0))
for i in range(10):
    print(res.group(i))
