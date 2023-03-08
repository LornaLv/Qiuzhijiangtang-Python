# Date: 2023/2/27 上午10:37
'''
猜年龄小游戏，三点需求:
1、允许用户最多尝试三次
2、每尝试三次后，如果还没有猜对，就问用户是否还想继续玩，如果回答Y或y，就继续让其猜三次，以此往复，如果回答N或n，就退出程序
3、如果猜对了，就直接退出
'''

import random

age = random.randint(1, 100)
print('我的年龄在1-100岁之间，你猜猜我多大了？')


def guessage():
    for i in range(3):
        guess = int(input(f'您一共有三次机会，第{i + 1}次猜测：'))

        if guess == age:
            print(f'你猜对了，我今年{age}岁了')
            break
        else:
            print('你猜错啦')

        if i == 2:
            choose = input('你还要继续猜吗？Y/N')
            if choose == 'Y' or choose == 'y':
                guessage()
            elif choose == 'N' or choose == 'n':
                break
            else:
                print('选择错误，您已退出')
guessage()


'''

# while True:
for i in range(3):
    guess = int(input('我的年龄在15-60岁之间，你猜猜我多大了？'))
    if 15 <= guess <= 60:
        if guess == age:
            print(f'你猜对了，我的年龄是{age}岁')
            break
        else:
            print('猜错啦，请继续猜测')
            if i == 2:
                choose = input('你还要继续猜吗？Y/N')
                if choose == 'Y' or choose == 'y':
                    continue
                elif choose == 'N' or choose == 'n':
                    break
                else:
                    print('选择错误，您已退出')
    else:
        print('我的年龄在15-60之间！')
'''
