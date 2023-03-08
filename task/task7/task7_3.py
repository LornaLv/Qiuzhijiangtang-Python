# Date: 2023/3/1 下午10:55
# 定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加上颜色属性
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def colors(self):
        print(f'{self.name}的颜色是{self.color}')


apple = Fruit('苹果', '红色')
orange = Fruit('橘子', '橙色')
watermelon = Fruit('西瓜', '绿色和黑色')
apple.colors()
orange.colors()
watermelon.colors()
