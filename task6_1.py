# Date: 2023/3/1 下午2:46
# 求三组连续自然数的和：求出1到10、20到30、35到45到三个和

def sum(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum


print('1-10的和为：', sum(1, 10))
print('10-20的和为：', sum(10, 20))
print('35-45的和为：', sum(35, 45))


a = int(input('请输入你想要的起始数据：'))
b = int(input('请输入你想要的终止数据：'))
sum = print(f'{a}到{b}的和为：{sum(a, b)}')
