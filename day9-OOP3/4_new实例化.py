# Date: 2023/3/4 下午2:55
# 在新式类中，__new__才是真正的实例化方法，为类提供外壳制造出实例框架，然后调用该框架内的构造方法__init__进行丰满操作
# 比喻建房子，__new__方法，负责开发地皮、打地基、并将原材料保存在工地，而__init__负责从工地取材料建造出地皮开发图纸规定的大楼
class Animal(object):
    def __init__(self):
        self.color = '红色'
        print('init被调用了')

    # 在Python中如果不重写__new__，默认状态如下
    def __new__(cls, *args, **kwargs):
        print('new被调用了')
        return super().__new__(cls, *args, **kwargs)


tiger = Animal()  # 实例化的过程会自动调用__new__去创建实例
