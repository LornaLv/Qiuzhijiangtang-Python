# Date: 2023/3/7 下午6:19
import os
import shutil

# os.rename('test.txt', 'test重命名.txt')
# os.remove('del.txt') # 删除文件
# os.mkdir('testcj') # 创建文件夹
# os.rmdir('testcj')  # 删除文件夹
# medir只能创建一级目录
# os.mkdir('/home/lvshaolin/桌面/Python/求知讲堂Python/day11-文件读写/lsl/3')  # 不允许创建多级
# os.makedirs('/home/lvshaolin/桌面/Python/求知讲堂Python/day11-文件读写/xl/1/2/3/4')  # 允许多级创建
# os.rmdir('/home/lvshaolin/桌面/Python/求知讲堂Python/day11-文件读写/xl/1/2/3/4')  # rmdir只能删除空目录
# 如果要删除非空目录 就需要调用shutil模块
# shutil.rmtree('/home/lvshaolin/桌面/Python/求知讲堂Python/day11-文件读写/lsl')

# 获取当前目录
print(os.getcwd())
# 路径的拼接
print(os.path.join(os.getcwd(), 'venv'))

print('-----------获取python中的目录列表-老版本用法----------')
# 获取python中的目录列表-老版本用法
listRs = os.listdir('/home/')
for dirname in listRs:
    print(dirname)

print('-----------获取Python中的目录列表-现代版写法----------')
# scandir 和with一起使用，这样上下文管理器会在迭代器遍历完成后自动释放资源
# 获取Python中的目录列表-现代版写法
with os.scandir('/home') as entries:
    for entry in entries:
        print(entry.name)

print('----------------------------------------------')
basePath = '/home/lvshaolin/桌面'
for entry in os.listdir((basePath)):
    if os.path.isdir(os.path.join(basePath, entry)):
        print(entry)
    # if os.path.isfile(os.path.join(basePath, entry)):
    #     print(entry)
