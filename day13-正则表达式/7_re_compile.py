# Date: 2023/3/14 下午6:44
# compile：re模块中的编译方法，可以把一个字符串编译成字节码
# 优点：在使用正则表达式进行match操作时，python会将字符串转换成正则表达式对象
# 而使用compile，只需要完成一次转换即可，以后再使用模式转换的话，无需重复转换
import re

print('------方法一------')
reobj = re.compile('\d{4}')
# 开始去使用模式对象reobj
rs = reobj.match('123456')
print(rs.group())

print('------方法二------')
print(re.match('\d{4}', '12345678').group())
