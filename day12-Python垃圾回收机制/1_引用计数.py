# Date: 2023/3/9 上午10:28
import sys

# sys.getrefcount()
a = []
print(sys.getrefcount(a))  # 两次
b = a
print(sys.getrefcount(a))  # 三次
c = b
d = b
e = c
f = e
g = d
print(sys.getrefcount(a))  # 八次
