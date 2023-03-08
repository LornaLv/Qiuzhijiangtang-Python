# Date: 2023/3/8 上午9:24
'''
__all__魔术变量的作用：
如果在一个文件中存在__all__变量，那么也就意味着这个变量中的元素，会被from XXX import * 时导入，对于import方式来讲，无所谓有没有，都可以引用
'''
__all__ = ['add', 'diff', 'printInfo']


def add(x, y):
    return x + y


def diff(x, y):
    return x - y


def printInfo():
    return '这是我自定义模块里的方法'


# 测试
if __name__ == '__main__':
    res = add(10, 4)
    print('测试模块的结果：', res)
print(f'模块__name__变量:{__name__}')
