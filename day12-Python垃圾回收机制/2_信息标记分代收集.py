# Date: 2023/3/9 上午11:40
import os
import sys
import psutil
import gc


def showMemSize(tag):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print(f'{tag}memory used：{memory}MB')
    pass


# 验证循环引用的情况
def func():
    showMemSize('初始化：')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    a.append(b)
    b.append(a)
    showMemSize('创建列表对象 a b 之后：')
    print(sys.getrefcount(a))
    print(sys.getrefcount(b))
    pass


func()
showMemSize('完成时候的')
gc.collect()  # 手动释放的
showMemSize('回收后：')
