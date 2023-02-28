# Date: 2023/2/28 下午1:30
'''
写函数，检查传入字典的每一个value的长度，如果大于2,那么仅保留前两个长度的内容，并将新内容返回给调用者
PS：字典中的value只能是字符串或列表
'''


def check(d):
    result = {}
    for key, value in d.items():
        if len(value) > 2:
            result[key] = value[:2]
        else:
            result[key] = value
    return result


# d=dict(input('请输入你想要输入的内容：'))
d = {'name': 'xiaolvvvvvvvvvvvvvvvv', 'age': '24', 'hobby': 'shaudhsauihdusaihdusiah'}
print(check(d))
