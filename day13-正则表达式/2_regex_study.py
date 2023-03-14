# Date: 2023/3/14 上午9:13
# 通过python中的re模块的使用最终掌握正则表达式的常用匹配规则
# group（num）可以获取匹配的数据，如果有多个匹配结果的话，那么会以元组的形式，存放到group对象中
# 此时我们可以通过下标去获取
import re

strData = 'Python is the best language in the world'
# res = re.match('python', strData, re.I)  # 第三个参数I表示忽略大小写
res = re.match('(.*) is (.*?) .*', strData, re.I | re.M)
if res:
    print('匹配成功')
    # print(res)
    print(res.groups())
    print(res.group())
else:
    print('匹配失败')
    print(res)
    print(res.group())
