# Date: 2023/3/2 上午10:22
class Animal:
    def __init__(self, name):
        self.name = name
        print('这是构造初始化__init__()方法')

    def __del__(self):
        print('当在某个作用域下面 没有被使用【引用】的情况下 解析器会自动的调用此函数 来释放内存空间')
        print('这是析构方法__del__()')


cat = Animal('咪咪')
del cat  # 手动清理删除对象
# print(cat)
