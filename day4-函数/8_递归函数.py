# Date: 2023/2/28 下午7:10
# 求阶乘
import os


def jiecheng(n):
    print('------------循环------------')
    result = 1
    for item in range(1, n + 1):
        result *= item
    return result


print('5的阶乘：', jiecheng(5))

print('------------递归------------')


def digui(n):
    if n == 1:
        return 1
    else:
        return n * digui(n - 1)


print('5的阶乘：', digui(6))

print('---------------递归案例：模拟实现，树形结构的遍历---------------')


def findFile(file_path):
    listRs = os.listdir(file_path)  # 得到该路径下所有的文件夹
    for fileItem in listRs:
        full_path = os.path.join(file_path, fileItem)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            findFile(full_path)  # 如果是一个文件夹，再次递归
        else:
            print(fileItem)
    else:
        return


# 调用搜索文件夹对象
findFile('/home/lvshaolin/桌面/Python/求知讲堂Python/day3-列表、字典、元组')
