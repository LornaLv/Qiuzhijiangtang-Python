# Date: 2023/3/6 下午7:17
# 抽象出来一个飞机基类
import pygame.image
from pygame.locals import *
import random


class BasePlane(object):
    def __init__(self, screen, imagePath):
        '''
        初始化基类函数
        :param screen: 主窗体对象
        :param imageName: 加载的图片
        '''
        self.screen = screen
        self.image = pygame.image.load(imagePath)
        self.bulletList = []  # 存储所有的子弹
        # 函数原型：pygame.key.set_repeat(delay, interval)
        pygame.key.set_repeat(150, 20)

    def show(self):
        '''
        飞机在主窗口中的显示
        :return:
        '''
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItemlist = []
        for item in self.bulletList:
            if item.judge():
                needDelItemlist.append(item)
        for i in needDelItemlist:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.show()  # 显示子弹的位置
            bullet.move()  # 子弹移动，下次再显示的时候就可以看到子弹修改的位置了

    pass


class HeroPlane(BasePlane):
    def __init__(self, screen):
        '''
        初始化函数
        :param screen:主函数对象
        '''
        super().__init__(screen, '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/images/me1.png')

        self.image = pygame.transform.scale(self.image, (50, 70))
        # 设置飞机的默认位置
        self.x = 287
        self.y = 840

    def moveLeft(self):
        '''
        向左移动
        :return:
        '''
        if self.x > 0:
            self.x -= 10

    def moveRight(self):
        '''
        向右移动
        :return:
        '''
        if self.x < 570:
            self.x += 10

    def moveDown(self):
        '''
        向下移动
        :return:
        '''
        if self.y < 840:
            self.y += 10

    def moveUp(self):
        '''
        向上移动
        :return:
        '''
        if self.y > 0:
            self.y -= 10

    # 发射子弹
    def shootBullet(self):
        # 创建一个新的子弹对象
        newBullet = CommonBullet(self.x, self.y, self.screen, 'hero')
        self.bulletList.append(newBullet)


class EnemyPlane(BasePlane):
    def __init__(self, screen):
        super().__init__(screen, '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/images/enemy1.png')
        # 默认设置一个方向
        self.direction = 'right'
        # 设置飞机的默认位置
        self.x = 0
        self.y = 0

    def shootBullet(self):
        '''
        敌机随机发射子弹
        :return:
        '''
        num = random.randint(1, 5)
        if num == 3:
            newBullet = CommonBullet(self.x, self.y, self.screen, 'enemy')
            self.bulletList.append(newBullet)

    def move(self):
        '''
        敌机移动 随机进行的
        :return:
        '''
        if self.direction == 'right':
            self.x += 10
        elif self.direction == 'left':
            self.x -= 10
        if self.x > 570:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'


class CommonBullet(object):
    '''
    公共的子弹类
    '''

    def __init__(self, x, y, screen, bulletType):
        self.screen = screen
        self.type = bulletType
        if self.type == 'hero':
            self.x = x + 22
            self.y = y - 30
            self.imagePath = '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/images/bullet1.png'
        elif self.type == 'enemy':
            self.x = x + 26
            self.y = y + 36
            self.imagePath = '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/images/bullet2.png'
        self.image = pygame.image.load(self.imagePath)
        self.image = pygame.transform.scale(self.image, (8, 24))

    def move(self):
        '''
        子弹的移动
        :return:
        '''
        if self.type == 'hero':
            self.y -= 40
        elif self.type == 'enemy':
            self.y += 40

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y > 910 or self.y < 0:
            return True
        else:
            return False


# 创建键盘控制函数
def Key_control(hero):
    # 获取键盘事件
    eventlist = pygame.event.get()
    # key_pressed = pygame.key.get_pressed()
    for event in eventlist:
        # 判断是否点击了退出游戏
        if event.type == QUIT:
            print('退出')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                print('left')
                # 控制飞机让其向左移动
                hero.moveLeft()

            elif event.key == K_RIGHT or event.key == K_d:
                print('right')
                # 控制飞机让其向右移动
                hero.moveRight()
            elif event.key == K_UP or event.key == K_w:
                print('up')
                # 控制飞机让其向上移动
                hero.moveUp()
            elif event.key == K_DOWN or event.key == K_s:
                print('down')
                # 控制飞机让其向下移动
                hero.moveDown()
            elif event.key == K_SPACE:
                # 发射子弹
                print('k_Space')
                hero.shootBullet()
        # 更新显示的内容
    pygame.display.update()


# 创建主函数
def main():
    # 1、首先创建一个窗口对象，用来显示内容
    screen = pygame.display.set_mode((624, 910), depth=32)

    # 2、设定一个背景图片
    background = pygame.image.load(
        '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/images/background.png')
    background = pygame.transform.scale(background, (624, 910))

    # 3、设置一个title
    title = pygame.display.set_caption('飞机大战')

    # 4、添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load(
        '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/backgroundmusic.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # -1表示无限循环

    # 5、创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机对象
    enemy = EnemyPlane(screen)

    # 6、把背景图片放到窗口中展示
    while True:
        screen.blit(background, (0, 0))
        # 设定需要显示的飞机图片
        hero.show()
        enemy.show()  # 显示敌机
        enemy.move()  # 敌机移动
        enemy.shootBullet()  # 敌机随机发射子弹
        Key_control(hero)
        # 更新需要显示的内容
        pygame.display.update()
        pygame.time.Clock().tick(5)  # 一秒内循环五次


if __name__ == '__main__':
    main()
