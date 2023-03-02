# Date: 2023/3/1 下午9:26
'''
决战紫禁之巅有两个人物，西门吹雪以及叶孤城
属性：name:玩家的名字
     blood:玩家血量
方法：tong() :捅对方一刀，对方掉血10滴
     Kanren():砍对方一刀，对方掉血15滴
     chiyao():吃一颗药，补血10滴
     __str__:打印玩家状态
'''

import random
import time
from operator import methodcaller


class Role(object):
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood

    def tong(self, enemy):
        b = random.randint(5, 10)
        enemy.blood = enemy.blood - b
        print(f'【{self.name}】捅了【{enemy.name}】一刀，【{enemy.name}】掉【{b}】滴血')
        pass

    def Kanren(self, enemy):
        b = random.randint(10, 15)
        enemy.blood = enemy.blood - b
        print(f'【{self.name}】砍了【{enemy.name}】一刀，【{enemy.name}】掉【{b}】滴血')
        pass

    def chiyao(self):
        b = random.randint(1, 5)
        self.blood = self.blood + b
        print(f'【{self.name}】吃了一颗补血药，【{self.name}】加【{b}】滴血')
        pass

    def __str__(self):
        return f'玩家【{self.name}】: 剩余血量【{self.blood}】'
        pass


xi = Role('西门吹雪', 100)
ye = Role('叶孤城', 100)

while True:
    if xi.blood <= 0 or ye.blood <= 0:
        break
    else:
        print('------------------------------------------------')
        # 随机调用带参函数（利用random模块和functools.partial（偏函数））
        c = [methodcaller('tong', ye), methodcaller('Kanren', ye), methodcaller('chiyao')]
        random.choice(c)(xi)
        if xi.blood > 100:
            xi.blood = 100
        if ye.blood > 100:
            ye.blood = 100
        if xi.blood < 0:
            xi.blood = 0
        if ye.blood < 0:
            ye.blood = 0
        print(xi)
        print(ye)
        time.sleep(3)

        print('------------------------------------------------')
        c = [methodcaller('tong', xi), methodcaller('Kanren', xi), methodcaller('chiyao')]
        random.choice(c)(ye)
        if xi.blood > 100:
            xi.blood = 100
        if ye.blood > 100:
            ye.blood = 100
        if xi.blood < 0:
            xi.blood = 0
        if ye.blood < 0:
            ye.blood = 0
        print(xi)
        print(ye)
        time.sleep(3)

print('------------------------------------------------')
if xi.blood==0:
    print(f'对战结果：叶孤城获得胜利，剩余血量{ye.blood}')
else:
    print(f'对战结果：西门吹雪获得胜利，剩余血量{xi.blood}')
