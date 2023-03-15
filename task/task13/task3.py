# Date: 2023/3/15 上午10:55
# 验证邮箱126,163邮箱：6-18个字符，可以使用字母、数字、下划线，需以字母开头
import re

reobj = re.compile('[a-zA-Z]\w{5,17}(@126.com|@163.com)')
res1 = reobj.match('a100000000000233e6@126.com')
if res1:
    print(res1.group())
else:
    print('邮箱格式错误')
