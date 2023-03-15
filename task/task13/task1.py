# Date: 2023/3/15 上午8:55
# 长度为8-10的用户密码（以字母开头，包含字母、数字、下划线）
import re

res = re.match('[a-zA-Z]\w{7,9}','a12345_67879' )
if res:
    print(res.group())
else:
    print('密码错误')
