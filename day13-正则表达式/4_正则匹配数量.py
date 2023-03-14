# Date: 2023/3/14 下午2:50
import re

# （1）*：匹配前一个字符出现0次或者无限次，即可有可无
print('（1）*：匹配前一个字符出现0次或者无限次，即可有可无-------')
res1 = re.match('[A-Z][A-Z]*', 'MDAHSBJHBAJsgfhsdhj')
print(res1.group())

# （2）+：匹配前一个字符出现1次或者无限次，即至少有一次
print('（2）+：匹配前一个字符出现1次或者无限次，即至少有一次-------')
res2 = re.match('[a-zA-Z]+', 'MDAHSBJHBAJsgfhsdhj')
print(res2.group())

# （3）\?：匹配前一个字符出现1次或者0次，即要么有1次，要么没有
print('（3）\?：匹配前一个字符出现1次或者0次，即要么有1次，要么没有-------')
res3 = re.match('[a-zA-Z]+[0-9]?', 'ndxfd54511name')
print(res3.group())

# （4）{m}：匹配前一个字符出现m次
print('（4）{m}：匹配前一个字符出现m次-------')
res4 = re.match('\d{4}', '12057653')
if res4:
    print('匹配成功{}'.format(res4.group()))
else:
    print('匹配失败')

# （5）{m,}：匹配前一个字符至少出现m次
print('（5）{m,}：匹配前一个字符至少出现m次-------')
res5 = re.match('\d{4,}', '12057653')
if res5:
    print('匹配成功{}'.format(res5.group()))
else:
    print('匹配失败')

# （6）{m,n}：匹配前一个字符出现从n到m次
print('（6）{m,n}：匹配前一个字符出现从n到m次-------')
res6 = re.match('\d{4,8}', '1205766779853')
if res6:
    print('匹配成功{}'.format(res6.group()))
else:
    print('匹配失败')

print('匹配变量名------------------------------')
# 匹配符合规范【规则是：不能以数字开头，只能包含字母、数字、下划线】的python变量命名
result = re.match('[a-zA-Z_]+[\w]*', '_11name')
print(result.group())

print('匹配邮箱-----------------------------')
result1 = re.match('[a-zA-Z0-9]{6,11}@163.com', '374q832@163.com')
if result1:
    print('匹配成功:{}'.format(result1.group()))
