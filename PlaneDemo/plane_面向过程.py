# Date: 2023/3/6 上午10:22
import pygame  # 引入第三方模块
from pygame.locals import *


def main():
    # 首先创建一个窗口对象，用来显示内容
    screen = pygame.display.set_mode((350, 500), depth=32)

    # 设定一个背景图片
    background = pygame.image.load(
        '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/images/background.png')

    # 设置一个title
    title = pygame.display.set_caption('飞机大战')

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load(
        '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/backgroundmusic.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # -1表示无限循环

    # 载入玩家的飞机图片
    hero = pygame.image.load(
        '/home/lvshaolin/桌面/Python/求知讲堂Python/PlaneDemo/feijidazhan/images/me1.png')
    hero = pygame.transform.scale(hero, (50, 70))

    # 初始玩家的位置
    x, y = 0, 0

    # 设置要显示的内容
    while True:
        screen.blit(background, (0, 0))
        # screen.blit(pygame.transform.scale(background,size=(0,0)))
        screen.blit(hero, (x, y))
        # 获取键盘事件
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == QUIT:
                print('退出')
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    print('left')
                    if x > 0:
                        x -= 5
                elif event.key == K_RIGHT or event.key == K_d:
                    print('right')
                    if x < 310:
                        x += 5
                elif event.key == K_SPACE:
                    print('k_Space')
        # 更新显示的内容
        pygame.display.update()


if __name__ == '__main__':
    main()
