# Date: 2023/3/1 下午3:00
# 100个和尚吃100个馒头，大和尚一人吃三个馒头，小和尚3个人吃一个馒头，请问大小和尚各多少人
def mantou(m, h):  # m:馒头数，h：和尚数
    for i in range(h + 1):
        if 3 * i + (h - i) / 3 == m:
            print(f'大和尚：{i}，小和尚：{h - i}')
        else:
            print('数据错误')
    pass


mantou(100, 100)
