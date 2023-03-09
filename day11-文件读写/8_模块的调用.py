# Date: 2023/3/8 上午9:25
# from modelTest import add  # 第二种导入

'''
import modelTest  # 第一种导入
res = modelTest.add(1, 4)
print(res)
print(modelTest.diff(90, 78))
'''

from modelTest import *  # 第三种导入

print(add(23, 78))
print(diff(34, 23))
print(printInfo())
