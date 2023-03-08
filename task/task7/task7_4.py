# Date: 2023/3/1 下午10:56
# 请编写代码，验证self就是实例本身

class P:
    def __init__(self):
        print(self)


p = P()
print(p)
