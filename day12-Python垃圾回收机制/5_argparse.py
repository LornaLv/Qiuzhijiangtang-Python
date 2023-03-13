# Date: 2023/3/13 下午6:42
import argparse

# 创建一个解析器对象
parse = argparse.ArgumentParser(prog='my-我自己的程序', usage='%(prog)s [options] usage',
                                description='my-编写自定义命令行的文件', epilog='my-epilog')

# 添加位置参数（必选参数）
parse.add_argument('name', type=str, help='你自己的名字')
parse.add_argument('birth', type=str, help='你的生日')
parse.add_argument('age', type=str, help='你的年龄')
print(parse.print_help())

# 添加可选参数
# parse.add_argument('-s', '--sex', action='append', type=str, help='你的性别')
# 限定范围
parse.add_argument('-s', '--sex', default='男', choices=['男', '女', 'male', 'female'], type=str, help='你的性别')
result = parse.parse_args()  # 开始解析参数
print(result.name, result.age, result.sex)
