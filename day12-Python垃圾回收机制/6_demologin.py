# Date: 2023/3/13 下午8:36
import argparse

# 创建一个解析器对象
parse = argparse.ArgumentParser(prog='系统登录', usage='%(prog)s [options] usage',
                                description='系统自定义命令行的文件', epilog='my-epilog')

# 添加位置参数（必选参数）
parse.add_argument('loginType', type=str, help='登录系统类型')

# 添加可选参数
parse.add_argument('-u', dest='user',type=str, help='你的用户名')
parse.add_argument('-p', dest='pwd',type=str, help='你的密码')

# 限定范围
result = parse.parse_args()  # 开始解析参数
if result.user=='root' and result.pwd=='111111':
    print('login success')
else:
    print('login fail')
